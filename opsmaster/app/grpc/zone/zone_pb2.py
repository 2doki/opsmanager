# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zone.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nzone.proto\"[\n\x0bZoneRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\t\x12\x12\n\nsvnversion\x18\x05 \x01(\t\"X\n\x0cZoneResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\t\x12\x0e\n\x06result\x18\x05 \x01(\t2/\n\x04Zone\x12\'\n\x06option\x12\x0c.ZoneRequest\x1a\r.ZoneResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'zone_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ZONEREQUEST._serialized_start=14
  _ZONEREQUEST._serialized_end=105
  _ZONERESPONSE._serialized_start=107
  _ZONERESPONSE._serialized_end=195
  _ZONE._serialized_start=197
  _ZONE._serialized_end=244
# @@protoc_insertion_point(module_scope)