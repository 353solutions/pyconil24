# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: unter.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'unter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bunter.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"p\n\x10StartRideRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x04kind\x18\x02 \x01(\x0e\x32\x05.Kind\x12\x11\n\tdriver_id\x18\x03 \x01(\t\x12(\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"X\n\x0e\x45ndRideRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1f\n\x11StartRideResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1d\n\x0f\x45ndRideResponse\x12\n\n\x02id\x18\x01 \x01(\t*?\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x10\n\x0cKIND_REGULAR\x10\x01\x12\x0f\n\x0bKIND_SHARED\x10\x02\x32m\n\x05Unter\x12\x34\n\tStartRide\x12\x11.StartRideRequest\x1a\x12.StartRideResponse\"\x00\x12.\n\x07\x45ndRide\x12\x0f.EndRideRequest\x1a\x10.EndRideResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'unter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KIND']._serialized_start=316
  _globals['_KIND']._serialized_end=379
  _globals['_STARTRIDEREQUEST']._serialized_start=48
  _globals['_STARTRIDEREQUEST']._serialized_end=160
  _globals['_ENDRIDEREQUEST']._serialized_start=162
  _globals['_ENDRIDEREQUEST']._serialized_end=250
  _globals['_STARTRIDERESPONSE']._serialized_start=252
  _globals['_STARTRIDERESPONSE']._serialized_end=283
  _globals['_ENDRIDERESPONSE']._serialized_start=285
  _globals['_ENDRIDERESPONSE']._serialized_end=314
  _globals['_UNTER']._serialized_start=381
  _globals['_UNTER']._serialized_end=490
# @@protoc_insertion_point(module_scope)
