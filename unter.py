from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Kind(Enum):
    regular = 'regular'
    shared = 'shared'


@dataclass
class StartRide:
    id: str
    kind: Kind
    driver_id: str
    start_time: datetime


@dataclass
class EndRide:
    id: str
    end_time: datetime
    distance: float  # in Km
