__all__ = ["PathFinder", "standby_position"]

import math
import time as pytime
from dataclasses import dataclass
from typing import Callable, Iterable, List, Optional, Tuple, TypeVar, Union

import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord, get_body
from astropy.coordinates.name_resolve import NameResolveError
from astropy.time import Time

from .. import config, utils
from ..typing import CoordFrameType, Number, UnitType
from .convert import CoordCalculator

T = TypeVar("T", Number, u.Quantity)


def standby_position(
    start: Tuple[T, T],
    end: Tuple[T, T],
    *,
    margin: Optional[Union[float, int, u.Quantity]],
    unit: Optional[UnitType] = None,
) -> Tuple[u.Quantity, u.Quantity]:
    """Calculate the standby position taking into account the margin during scanning.

    Parameters
    ----------
    start
        Longitude and latitude of start point.
    end
        Longitude and latitude of end point.
    unit
        Angular unit in which longitude and latitude are given. If they are given as
        ``Quantity``, this parameter will be ignored.

    Examples
    --------
    >>> neclib.coordinates.standby_position(start=(30, 50), end=(32, 50), unit="deg")
    (<Quantity 29. deg>, <Quantity 50. deg>)

    """
    margin = utils.get_quantity(margin, unit=unit)
    start = utils.get_quantity(*start, unit=unit)
    end = utils.get_quantity(*end, unit=unit)
    pa = get_position_angle(start[0], end[0], start[1], end[1])
    margin_lon, margin_lat = margin * np.cos(pa), margin * np.sin(pa)
    return (start[0] - margin_lon, start[1] - margin_lat)


def get_position_angle(start_lon, end_lon, start_lat, end_lat):
    if end_lon == start_lon:
        position_angle = (np.pi / 2 * u.rad) * np.sign(end_lat - start_lat)
    else:
        position_angle = np.arctan((end_lat - start_lat) / (end_lon - start_lon))
        position_angle += (np.pi if end_lon < start_lon else 0) * u.rad
    return position_angle


class Timer:
    def __init__(self):
        self.start = pytime.time()
        self.target = self.start

    def set_offset(self, offset) -> None:
        if not isinstance(offset, (int, float)):
            raise TypeError(f"Offset must be int or float, not {type(offset)}")
        self.target += offset

    def get(self) -> float:
        return self.target

    def __bool__(self) -> bool:
        return True


@dataclass
class ControlStatus:
    controlled: bool
    tight: bool
    start: Optional[float] = None
    stop: Optional[float] = None


class PathFinder(CoordCalculator):
    """望遠鏡の軌道を計算する

    Parameters
    ----------
    location
        Location of observatory.
    pointing_param_path
        Path to pointing parameter file.
    pressure
        Atmospheric pressure at the observation environment.
    temperature
        Temperature at the observation environment.
    relative_humidity
        Relative humidity at the observation environment.
    obswl
        Observing wavelength.

    Attributes
    ----------
    location: EarthLocation
        Location of observatory.
    pressure: Quantity
        Atmospheric pressure, to compute diffraction correction.
    temperature: Quantity
        Temperature, to compute diffraction correction.
    relative_humidity: Quantity or float
        Relative humidity, to compute diffraction correction.
    obswl: Quantity
        Observing wavelength, to compute diffraction correction.
    obsfreq: Quantity
        Observing frequency of EM-wave, to compute diffraction correction.

    Examples
    --------
    >>> location = EarthLocation("138.472153deg", "35.940874deg", "1386m")
    >>> path = "path/to/pointing_param.toml"
    >>> pressure = 850 * u.hPa
    >>> temperature = 290 * u.K
    >>> humid = 0.5
    >>> obsfreq = 230 * u.GHz
    >>> finder = neclib.coordinates.PathFinder(
    ...     location, path, pressure=pressure, temperature=temperature,
    ...     relative_humidity=humid, obsfreq=obsfreq)

    """

    command_unit_duration_sec = 1

    @property
    def unit_n_cmd(self) -> int:
        """Number of commands to be calculated in ``self.command_unit_duration_sec``."""
        return int(self.command_unit_duration_sec * config.antenna_command_frequency)

    @property
    def unit_index(self) -> List[float]:
        return [i / (self.unit_n_cmd - 1) for i in range(self.unit_n_cmd)]

    def time_index(self, start_time: float) -> List[float]:
        start_time += config.antenna_command_offset_sec
        return [
            start_time + i / (config.antenna_command_frequency - 1)
            for i in range(self.unit_n_cmd)
        ]

    def functional(
        self,
        lon: Callable[[float], T],
        lat: Callable[[float], T],
        frame: CoordFrameType,
        *,
        unit: Optional[UnitType] = None,
        n_cmd: Union[int, float],
        mode: ControlStatus,
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        """Calculate the path of antenna movement from any function.

        Parameters
        ----------
        lon
            Function that returns longitude. The function should accept single argument;
            auxiliary variable of value between 0 and 1.
        lat
            Function that returns latitude.
        frame
            Frame in which the coordinates are given.
        unit
            Angular unit in which longitude and latitude are given. If they are given as
            ``Quantity``, this parameter will be ignored.
        n_cmd
            Number of commands. The path will be calculated supplying arithmetic
            sequence of auxiliary variable, which first term is 0, last is 1, number of
            members is ``n_cmd``.
        time
            Start time manager. If ``None``, current time will be used. No consideration
            for ``antenna_command_offset_sec`` is required.

        Returns
        -------
        Az, El, Time
            Tuple of conversion result, azimuth, elevation and time.

        Examples
        --------
        >>> def lon(x):
        ...     return 30 + x * 2
        >>> def lat(x):
        ...     return 50
        >>> path = finder.functional(lon, lat, frame="altaz", unit="deg", n_cmd=1000)
        >>> next(path)
        (<Quantity [30., 30.1, 30.2, ...] deg>, <Quantity [50., 50., 50., ...] deg>,
        [1610612736.0, 1610612736.1, 1610612736.2, ...])

        """
        time = time or Timer()
        start = time.get() + config.antenna_command_offset_sec
        time.set_offset(n_cmd / config.antenna_command_frequency)

        mode.start = start
        mode.stop = time.get() + config.antenna_command_offset_sec

        for seq in range(math.ceil(n_cmd / self.unit_n_cmd)):
            idx = [seq * self.unit_n_cmd + j for j in range(self.unit_n_cmd)]
            param = [_idx / n_cmd for _idx in idx]
            param = list(filter(lambda x: x <= 1, param))
            idx = idx[: len(param)]
            if (seq == math.ceil(n_cmd / self.unit_n_cmd) - 1) and (param[-1] < 1):
                param.append(1)
                idx.append(idx[-1] + (param[-1] - param[-2]) * n_cmd)

            lon_for_this_seq = [lon(p) for p in param]
            lat_for_this_seq = [lat(p) for p in param]
            t_for_this_seq = [
                start + (i / config.antenna_command_frequency) for i in idx
            ]

            yield *self.get_altaz(
                lon=lon_for_this_seq,
                lat=lat_for_this_seq,
                frame=frame,
                unit=unit,
                obstime=t_for_this_seq,
            ), mode

    def linear(
        self,
        start: Tuple[T, T],
        end: Tuple[T, T],
        frame: CoordFrameType,
        *,
        speed: Union[float, int, u.Quantity],
        unit: Optional[UnitType] = None,
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        """望遠鏡の直線軌道を計算する

        Parameters
        ----------
        start
            Longitude and latitude of start point.
        end
            Longitude and latitude of end point.
        frame
            Coordinate frame, in which longitude and latitude are given.
        speed
            Telescope drive speed.
        unit
            Angular unit in which longitude and latitude are given. If they are given as
            ``Quantity``, this parameter will be ignored.

        Returns
        -------
        Az, El, Time
            Tuple of calculated azimuth, elevation and time commands.

        Examples
        --------
        >>> finder.linear(
            start=(0, 0), end=(0.05, 0), frame="altaz", speed=0.5, unit=u.deg
        )
        [<Quantity [-1.47920569, -1.46920569, -1.45920569, -1.44920569, -1.43920569,
           -1.42920569] deg>, <Quantity [-1.88176239, -1.88176188, -1.88176136,
           -1.88176084, -1.88176032, -1.8817598 ] deg>, array([1.66685637e+09,
           1.66685637e+09, 1.66685637e+09, 1.66685637e+09,
           1.66685637e+09, 1.66685637e+09])]

        """
        time = time or Timer()

        start = utils.get_quantity(*start, unit=unit)
        end = utils.get_quantity(*end, unit=unit)
        speed = utils.get_quantity(speed, unit=end[0].unit / u.s)
        distance = ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5
        n_cmd = (distance / speed) * (config.antenna_command_frequency * u.Hz)

        def lon(x):
            return start[0] + x * (end[0] - start[0])

        def lat(x):
            return start[1] + x * (end[1] - start[1])

        mode = ControlStatus(controlled=True, tight=True)
        yield from self.functional(
            lon, lat, frame, unit=unit, n_cmd=float(n_cmd), time=time, mode=mode
        )

    def accelerate_to(
        self,
        start: Tuple[T, T],
        end: Tuple[T, T],
        frame: CoordFrameType,
        *,
        speed: Union[float, int, u.Quantity],
        unit: Optional[UnitType] = None,
        margin: Union[float, int, u.Quantity],
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        margin_start = standby_position(start, end, margin=margin, unit=unit)
        margin_end = utils.get_quantity(*start, unit=unit)
        margin = utils.get_quantity(margin, unit=unit)
        speed = utils.get_quantity(speed, unit=margin.unit / u.s)

        position_angle = get_position_angle(
            margin_start[0], margin_end[0], margin_start[1], margin_end[1]
        )

        # マージン部分の座標計算 加速度その1
        a = (speed**2) / (2 * margin)

        # マージン部分の座標計算 加速度その2
        # a_az = config.antenna_max_acceleration_az
        # a_el = config.antenna_max_acceleration_el
        # a = (a_az**2 + a_el**2) ** (1 / 2)

        required_time = ((2 * margin) / a) ** (1 / 2)
        n_cmd = required_time.to_value("s") * config.antenna_command_frequency

        def lon(x):
            t = x * required_time
            a_lon = a * np.cos(position_angle)
            return margin_start[0] + a_lon * t**2 / 2

        def lat(x):
            t = x * required_time
            a_lat = a * np.sin(position_angle)
            return margin_start[1] + a_lat * t**2 / 2

        time = time or Timer()
        mode = ControlStatus(controlled=True, tight=False)
        yield from self.functional(
            lon, lat, frame, unit=unit, n_cmd=n_cmd, time=time, mode=mode
        )

    def linear_with_acceleration(
        self,
        start: Tuple[T, T],
        end: Tuple[T, T],
        frame: CoordFrameType,
        *,
        speed: Union[float, int, u.Quantity],
        unit: Optional[UnitType] = None,
        margin: Union[float, int, u.Quantity],
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()
        yield from self.accelerate_to(
            start, end, frame, speed=speed, unit=unit, margin=margin, time=time
        )
        yield from self.linear(start, end, frame, speed=speed, unit=unit, time=time)

    def offset_linear(
        self,
        start: Tuple[T, T],
        end: Tuple[T, T],
        frame: CoordFrameType,
        *,
        reference: Tuple[T, T, CoordFrameType],
        speed: Union[float, int, u.Quantity],
        unit: Optional[UnitType] = None,
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()

        start = utils.get_quantity(*start, unit=unit)
        end = utils.get_quantity(*end, unit=unit)

        kwargs = dict(
            frame=reference[2],
            obstime=Time(time.get(), format="unix"),
            location=self.location,
        )
        _ = kwargs.update(unit=unit) if unit is not None else ...
        ref = SkyCoord(*reference[:2], **kwargs).transform_to(frame)
        start = (ref.data.lon + start[0], ref.data.lat + start[1])
        end = (ref.data.lon + end[0], ref.data.lat + end[1])

        yield from self.linear(start, end, frame, speed=speed, unit=unit, time=time)

    def offset_linear_with_acceleration(
        self,
        start: Tuple[T, T],
        end: Tuple[T, T],
        frame: CoordFrameType,
        *,
        reference: Tuple[T, T, CoordFrameType],
        speed: Union[float, int, u.Quantity],
        unit: Optional[UnitType] = None,
        margin: Union[float, int, u.Quantity],
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()

        start = utils.get_quantity(*start, unit=unit)
        end = utils.get_quantity(*end, unit=unit)
        speed = utils.get_quantity(speed, unit=f"{unit}/s")
        required_time = (((start - end) ** 2).sum() ** 0.5 / speed).to_value("s")

        kwargs = dict(
            frame=reference[2],
            obstime=Time(time.get(), format="unix"),
            location=self.location,
        )
        _ = kwargs.update(unit=unit) if unit is not None else ...
        ref = SkyCoord(*reference[:2], **kwargs).transform_to(frame)
        start = (ref.data.lon + start[0], ref.data.lat + start[1])

        kwargs.update(obstime=Time(time.get() + required_time, format="unix"))
        ref = SkyCoord(*reference[:2], **kwargs).transform_to(frame)
        end = (ref.data.lon + end[0], ref.data.lat + end[1])  # NO TRACKING

        yield from self.accelerate_to(
            start, end, frame, speed=speed, unit=unit, margin=margin, time=time
        )
        yield from self.linear(start, end, frame, speed=speed, unit=unit, time=time)

    def offset_track(
        self,
        offset: Tuple[T, T],
        frame: CoordFrameType,
        *,
        reference: Tuple[T, T, CoordFrameType],
        unit: Optional[UnitType] = None,
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()
        mode = ControlStatus(controlled=True, tight=False)

        kwargs = dict(location=self.location)
        kwargs.update(unit=unit) if unit is not None else ...
        d_lon, d_lat = utils.get_quantity(*offset[:2], unit=unit)

        def get_offset_applied(t):
            t = Time(t, format="unix")
            ref_lon = np.broadcast_to(reference[0], t.shape)
            ref_lat = np.broadcast_to(reference[1], t.shape)
            kwargs.update(obstime=t)
            relative_to = SkyCoord(ref_lon, ref_lat, frame=reference[2], **kwargs)
            relative_to = relative_to.transform_to(frame)
            _d_lon = np.broadcast_to(d_lon, t.shape) * d_lon.unit
            _d_lat = np.broadcast_to(d_lat, t.shape) * d_lat.unit
            return relative_to.spherical_offsets_by(_d_lon, _d_lat)

        def lon(x):
            target_data = target.data.lon
            if target_data.size == 1:
                return target_data
            return np.interp(x, self.unit_index, target_data)

        def lat(x):
            target_data = target.data.lat
            if target_data.size == 1:
                return target_data
            return np.interp(x, self.unit_index, target_data)

        while True:
            start_time = time.get()
            t = self.time_index(start_time)
            target = get_offset_applied(t)

            yield from self.functional(
                lon, lat, target.frame.name, n_cmd=self.unit_n_cmd, time=time, mode=mode
            )

    def track(
        self,
        lon: T,
        lat: T,
        frame: CoordFrameType,
        *,
        unit: Optional[UnitType] = None,
        time: Optional[Timer] = None,
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()
        mode = ControlStatus(controlled=True, tight=False)
        while True:
            yield from self.functional(
                lambda _: lon,
                lambda _: lat,
                frame,
                unit=unit,
                n_cmd=self.unit_n_cmd,
                time=time,
                mode=mode,
            )

    def track_by_name(
        self, name: str, *, time: Optional[Timer] = None
    ) -> Iterable[Tuple[u.Quantity, u.Quantity, List[float], ControlStatus]]:
        time = time or Timer()
        mode = ControlStatus(controlled=True, tight=False)

        def get_coord(name: str, t: List[float]):
            t = Time(t, format="unix")
            try:
                return get_body(name, t, self.location)
            except KeyError:
                return SkyCoord.from_name(name, frame="icrs")

        def lon(x):
            coord_data = coord.data.lon
            if coord_data.size == 1:
                return coord_data
            return np.interp(x, self.unit_index, coord_data)

        def lat(x):
            coord_data = coord.data.lat
            if coord_data.size == 1:
                return coord_data
            return np.interp(x, self.unit_index, coord_data)

        while True:
            start_time = time.get()
            t = self.time_index(start_time)
            try:
                coord = get_coord(name, t)
            except NameResolveError:
                self.logger.error(f"Cannot resolve {name!r}")
                return f"Cannot resolve {name!r}"

            yield from self.functional(
                lon, lat, coord.frame.name, n_cmd=self.unit_n_cmd, time=time, mode=mode
            )
