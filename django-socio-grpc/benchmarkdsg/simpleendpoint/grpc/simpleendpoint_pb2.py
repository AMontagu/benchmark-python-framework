# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: simpleendpoint/grpc/simpleendpoint.proto
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
    'simpleendpoint/grpc/simpleendpoint.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(simpleendpoint/grpc/simpleendpoint.proto\x12\x1b\x62\x65nchmarkdsg.simpleendpoint\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"?\n)SimpleServiceGetBiggerFileAsBytesResponse\x12\x12\n\nfile_bytes\x18\x01 \x01(\x0c\"A\n*SimpleServiceGetBiggerFileAsStringResponse\x12\x13\n\x0b\x66ile_string\x18\x01 \x01(\t\"Z\n*SimpleServiceGetBiggerFileAsStructResponse\x12,\n\x0b\x66ile_struct\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\",\n\x1cSimpleServiceGetCharResponse\x12\x0c\n\x04\x63har\x18\x01 \x01(\t\"@\n*SimpleServiceGetSmallerFileAsBytesResponse\x12\x12\n\nfile_bytes\x18\x01 \x01(\x0c\"B\n+SimpleServiceGetSmallerFileAsStringResponse\x12\x13\n\x0b\x66ile_string\x18\x01 \x01(\t\"[\n+SimpleServiceGetSmallerFileAsStructResponse\x12,\n\x0b\x66ile_struct\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\xe3\x06\n\x17SimpleServiceController\x12x\n\x14GetBiggerFileAsBytes\x12\x16.google.protobuf.Empty\x1a\x46.benchmarkdsg.simpleendpoint.SimpleServiceGetBiggerFileAsBytesResponse\"\x00\x12z\n\x15GetBiggerFileAsString\x12\x16.google.protobuf.Empty\x1aG.benchmarkdsg.simpleendpoint.SimpleServiceGetBiggerFileAsStringResponse\"\x00\x12z\n\x15GetBiggerFileAsStruct\x12\x16.google.protobuf.Empty\x1aG.benchmarkdsg.simpleendpoint.SimpleServiceGetBiggerFileAsStructResponse\"\x00\x12^\n\x07GetChar\x12\x16.google.protobuf.Empty\x1a\x39.benchmarkdsg.simpleendpoint.SimpleServiceGetCharResponse\"\x00\x12z\n\x15GetSmallerFileAsBytes\x12\x16.google.protobuf.Empty\x1aG.benchmarkdsg.simpleendpoint.SimpleServiceGetSmallerFileAsBytesResponse\"\x00\x12|\n\x16GetSmallerFileAsString\x12\x16.google.protobuf.Empty\x1aH.benchmarkdsg.simpleendpoint.SimpleServiceGetSmallerFileAsStringResponse\"\x00\x12|\n\x16GetSmallerFileAsStruct\x12\x16.google.protobuf.Empty\x1aH.benchmarkdsg.simpleendpoint.SimpleServiceGetSmallerFileAsStructResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simpleendpoint.grpc.simpleendpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIMPLESERVICEGETBIGGERFILEASBYTESRESPONSE']._serialized_start=132
  _globals['_SIMPLESERVICEGETBIGGERFILEASBYTESRESPONSE']._serialized_end=195
  _globals['_SIMPLESERVICEGETBIGGERFILEASSTRINGRESPONSE']._serialized_start=197
  _globals['_SIMPLESERVICEGETBIGGERFILEASSTRINGRESPONSE']._serialized_end=262
  _globals['_SIMPLESERVICEGETBIGGERFILEASSTRUCTRESPONSE']._serialized_start=264
  _globals['_SIMPLESERVICEGETBIGGERFILEASSTRUCTRESPONSE']._serialized_end=354
  _globals['_SIMPLESERVICEGETCHARRESPONSE']._serialized_start=356
  _globals['_SIMPLESERVICEGETCHARRESPONSE']._serialized_end=400
  _globals['_SIMPLESERVICEGETSMALLERFILEASBYTESRESPONSE']._serialized_start=402
  _globals['_SIMPLESERVICEGETSMALLERFILEASBYTESRESPONSE']._serialized_end=466
  _globals['_SIMPLESERVICEGETSMALLERFILEASSTRINGRESPONSE']._serialized_start=468
  _globals['_SIMPLESERVICEGETSMALLERFILEASSTRINGRESPONSE']._serialized_end=534
  _globals['_SIMPLESERVICEGETSMALLERFILEASSTRUCTRESPONSE']._serialized_start=536
  _globals['_SIMPLESERVICEGETSMALLERFILEASSTRUCTRESPONSE']._serialized_end=627
  _globals['_SIMPLESERVICECONTROLLER']._serialized_start=630
  _globals['_SIMPLESERVICECONTROLLER']._serialized_end=1497
# @@protoc_insertion_point(module_scope)
