from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KIND_UNSPECIFIED: _ClassVar[Kind]
    KIND_REGULAR: _ClassVar[Kind]
    KIND_SHARED: _ClassVar[Kind]
KIND_UNSPECIFIED: Kind
KIND_REGULAR: Kind
KIND_SHARED: Kind

class StartRideRequest(_message.Message):
    __slots__ = ("id", "kind", "driver_id", "time")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: Kind
    driver_id: str
    time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[Kind, str]] = ..., driver_id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EndRideRequest(_message.Message):
    __slots__ = ("id", "distance", "time")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    distance: float
    time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., distance: _Optional[float] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartRideResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EndRideResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
