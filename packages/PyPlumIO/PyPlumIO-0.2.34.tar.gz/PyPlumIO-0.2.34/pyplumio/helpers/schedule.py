"""Contains schedule helpers."""


from collections.abc import Iterable, MutableMapping
from dataclasses import dataclass
import datetime as dt
import math
from typing import TYPE_CHECKING, Final, Iterator, List, Literal, Tuple

from pyplumio.const import (
    ATTR_PARAMETER,
    ATTR_SCHEDULE,
    ATTR_SWITCH,
    ATTR_TYPE,
    STATE_OFF,
    STATE_ON,
)
from pyplumio.helpers.factory import factory
from pyplumio.helpers.typing import DeviceDataType
from pyplumio.structures.schedules import ATTR_SCHEDULES

if TYPE_CHECKING:
    from pyplumio.devices import Device
else:
    Device = object

TIME_FORMAT: Final = "%H:%M"
START_OF_DAY: Final = "00:00"
END_OF_DAY: Final = "00:00"

STATE_NIGHT: Final = STATE_OFF
STATE_DAY: Final = STATE_ON


def _parse_interval(start: str, end: str) -> Tuple[int, int]:
    """Parse interval string."""
    start_dt = dt.datetime.strptime(start, TIME_FORMAT)
    end_dt = dt.datetime.strptime(end, TIME_FORMAT)
    start_of_day_dt = dt.datetime.strptime(START_OF_DAY, TIME_FORMAT)
    if end_dt == start_of_day_dt:
        # Upper bound of interval is midnight.
        end_dt += dt.timedelta(days=1)

    if end_dt <= start_dt:
        raise ValueError(
            f"Invalid interval ({start}, {end}). Lower boundary must be less than upper."
        )

    start_index = math.floor((start_dt - start_of_day_dt).total_seconds() // (60 * 30))
    stop_index = math.floor((end_dt - start_of_day_dt).total_seconds() // (60 * 30))

    return start_index, stop_index


def _collect_schedule_data(name: str, device: Device) -> DeviceDataType:
    """Return schedule data collected from the device."""
    switch_key = f"schedule_{name}_{ATTR_SWITCH}"
    parameter_key = f"schedule_{name}_{ATTR_PARAMETER}"

    return {
        ATTR_TYPE: name,
        ATTR_SWITCH: device.data[switch_key],
        ATTR_PARAMETER: device.data[parameter_key],
        ATTR_SCHEDULE: device.data[ATTR_SCHEDULES][name],
    }


class ScheduleDay(MutableMapping):
    """Represents single day of schedule."""

    _intervals: List[bool]

    def __init__(self, intervals: List[bool]):
        """Initialize new schedule day object."""
        self._intervals = intervals

    def __repr__(self) -> str:
        """Return serializable representation of the class."""
        return f"ScheduleDay({self._intervals})"

    def __len__(self) -> int:
        """Return schedule length."""
        return len(self._intervals)

    def __iter__(self) -> Iterator[bool]:
        """Return iterator."""
        return self._intervals.__iter__()

    def __getitem__(self, index):
        """Return item."""
        return self._intervals.__getitem__(index)

    def __delitem__(self, index) -> None:
        return self._intervals.__delitem__(index)

    def __setitem__(self, index, value) -> None:
        return self._intervals.__setitem__(index, value)

    def append(self, item) -> None:
        """Append value to interval."""
        self._intervals.append(item)

    def set_state(
        self,
        state: Literal["off", "on"],
        start: str = START_OF_DAY,
        end: str = END_OF_DAY,
    ) -> None:
        """Set state for interval."""
        index, stop_index = _parse_interval(start, end)
        while index < stop_index:
            self._intervals[index] = state == STATE_ON
            index += 1

    def set_on(self, start: str = START_OF_DAY, end: str = END_OF_DAY) -> None:
        """Set on state for interval."""
        self.set_state(STATE_ON, start, end)

    def set_off(self, start: str = START_OF_DAY, end: str = END_OF_DAY) -> None:
        """Set off state for interval."""
        self.set_state(STATE_OFF, start, end)

    @property
    def intervals(self) -> List[bool]:
        """Return intervals."""
        return self._intervals


@dataclass
class Schedule(Iterable):
    """Represents weekly schedule."""

    name: str
    device: Device
    monday: ScheduleDay
    tuesday: ScheduleDay
    wednesday: ScheduleDay
    thursday: ScheduleDay
    friday: ScheduleDay
    saturday: ScheduleDay
    sunday: ScheduleDay

    def __iter__(self) -> Iterator[ScheduleDay]:
        """Return list of days."""
        return (
            self.sunday,
            self.monday,
            self.tuesday,
            self.wednesday,
            self.thursday,
            self.friday,
            self.saturday,
        ).__iter__()

    def commit(self) -> None:
        """Commit changes to the device."""
        self.device.queue.put_nowait(
            factory(
                "frames.requests.SetScheduleRequest",
                recipient=self.device.address,
                data=_collect_schedule_data(self.name, self.device),
            )
        )
