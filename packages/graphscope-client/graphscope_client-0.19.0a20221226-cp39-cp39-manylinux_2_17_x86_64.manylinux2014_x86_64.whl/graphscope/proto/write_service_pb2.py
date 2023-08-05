# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graphscope/proto/write_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='graphscope/proto/write_service.proto',
  package='gs.rpc.write_service.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.alibaba.graphscope.proto.writeP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$graphscope/proto/write_service.proto\x12\x17gs.rpc.write_service.v1\"\x14\n\x12GetClientIdRequest\"(\n\x13GetClientIdResponse\x12\x11\n\tclient_id\x18\x01 \x01(\t\"g\n\x11\x42\x61tchWriteRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12?\n\x0ewrite_requests\x18\x02 \x03(\x0b\x32\'.gs.rpc.write_service.v1.WriteRequestPb\")\n\x12\x42\x61tchWriteResponse\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\x03\"?\n\x12RemoteFlushRequest\x12\x13\n\x0bsnapshot_id\x18\x01 \x01(\x03\x12\x14\n\x0cwait_time_ms\x18\x02 \x01(\x03\"&\n\x13RemoteFlushResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x86\x01\n\x0eWriteRequestPb\x12\x38\n\nwrite_type\x18\x01 \x01(\x0e\x32$.gs.rpc.write_service.v1.WriteTypePb\x12:\n\x0b\x64\x61ta_record\x18\x02 \x01(\x0b\x32%.gs.rpc.write_service.v1.DataRecordPb\"\xa8\x02\n\x0c\x44\x61taRecordPb\x12G\n\x11vertex_record_key\x18\x01 \x01(\x0b\x32*.gs.rpc.write_service.v1.VertexRecordKeyPbH\x00\x12\x43\n\x0f\x65\x64ge_record_key\x18\x02 \x01(\x0b\x32(.gs.rpc.write_service.v1.EdgeRecordKeyPbH\x00\x12I\n\nproperties\x18\x03 \x03(\x0b\x32\x35.gs.rpc.write_service.v1.DataRecordPb.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0c\n\nrecord_key\"\xac\x01\n\x11VertexRecordKeyPb\x12\r\n\x05label\x18\x01 \x01(\t\x12S\n\rpk_properties\x18\x02 \x03(\x0b\x32<.gs.rpc.write_service.v1.VertexRecordKeyPb.PkPropertiesEntry\x1a\x33\n\x11PkPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x01\n\x0f\x45\x64geRecordKeyPb\x12\r\n\x05label\x18\x01 \x01(\t\x12\x42\n\x0esrc_vertex_key\x18\x02 \x01(\x0b\x32*.gs.rpc.write_service.v1.VertexRecordKeyPb\x12\x42\n\x0e\x64st_vertex_key\x18\x03 \x01(\x0b\x32*.gs.rpc.write_service.v1.VertexRecordKeyPb\x12\x10\n\x08inner_id\x18\x04 \x01(\x03*>\n\x0bWriteTypePb\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06INSERT\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x32\xc8\x02\n\x0b\x43lientWrite\x12h\n\x0bgetClientId\x12+.gs.rpc.write_service.v1.GetClientIdRequest\x1a,.gs.rpc.write_service.v1.GetClientIdResponse\x12\x65\n\nbatchWrite\x12*.gs.rpc.write_service.v1.BatchWriteRequest\x1a+.gs.rpc.write_service.v1.BatchWriteResponse\x12h\n\x0bremoteFlush\x12+.gs.rpc.write_service.v1.RemoteFlushRequest\x1a,.gs.rpc.write_service.v1.RemoteFlushResponseB&\n\"com.alibaba.graphscope.proto.writeP\x01\x62\x06proto3'
)

_WRITETYPEPB = _descriptor.EnumDescriptor(
  name='WriteTypePb',
  full_name='gs.rpc.write_service.v1.WriteTypePb',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1182,
  serialized_end=1244,
)
_sym_db.RegisterEnumDescriptor(_WRITETYPEPB)

WriteTypePb = enum_type_wrapper.EnumTypeWrapper(_WRITETYPEPB)
UNKNOWN = 0
INSERT = 1
UPDATE = 2
DELETE = 3



_GETCLIENTIDREQUEST = _descriptor.Descriptor(
  name='GetClientIdRequest',
  full_name='gs.rpc.write_service.v1.GetClientIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=85,
)


_GETCLIENTIDRESPONSE = _descriptor.Descriptor(
  name='GetClientIdResponse',
  full_name='gs.rpc.write_service.v1.GetClientIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='gs.rpc.write_service.v1.GetClientIdResponse.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=127,
)


_BATCHWRITEREQUEST = _descriptor.Descriptor(
  name='BatchWriteRequest',
  full_name='gs.rpc.write_service.v1.BatchWriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='gs.rpc.write_service.v1.BatchWriteRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='write_requests', full_name='gs.rpc.write_service.v1.BatchWriteRequest.write_requests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=232,
)


_BATCHWRITERESPONSE = _descriptor.Descriptor(
  name='BatchWriteResponse',
  full_name='gs.rpc.write_service.v1.BatchWriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='gs.rpc.write_service.v1.BatchWriteResponse.snapshot_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=275,
)


_REMOTEFLUSHREQUEST = _descriptor.Descriptor(
  name='RemoteFlushRequest',
  full_name='gs.rpc.write_service.v1.RemoteFlushRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshot_id', full_name='gs.rpc.write_service.v1.RemoteFlushRequest.snapshot_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wait_time_ms', full_name='gs.rpc.write_service.v1.RemoteFlushRequest.wait_time_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=340,
)


_REMOTEFLUSHRESPONSE = _descriptor.Descriptor(
  name='RemoteFlushResponse',
  full_name='gs.rpc.write_service.v1.RemoteFlushResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='gs.rpc.write_service.v1.RemoteFlushResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=380,
)


_WRITEREQUESTPB = _descriptor.Descriptor(
  name='WriteRequestPb',
  full_name='gs.rpc.write_service.v1.WriteRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='write_type', full_name='gs.rpc.write_service.v1.WriteRequestPb.write_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_record', full_name='gs.rpc.write_service.v1.WriteRequestPb.data_record', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=517,
)


_DATARECORDPB_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='gs.rpc.write_service.v1.DataRecordPb.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gs.rpc.write_service.v1.DataRecordPb.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gs.rpc.write_service.v1.DataRecordPb.PropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=753,
  serialized_end=802,
)

_DATARECORDPB = _descriptor.Descriptor(
  name='DataRecordPb',
  full_name='gs.rpc.write_service.v1.DataRecordPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertex_record_key', full_name='gs.rpc.write_service.v1.DataRecordPb.vertex_record_key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edge_record_key', full_name='gs.rpc.write_service.v1.DataRecordPb.edge_record_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='gs.rpc.write_service.v1.DataRecordPb.properties', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATARECORDPB_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='record_key', full_name='gs.rpc.write_service.v1.DataRecordPb.record_key',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=520,
  serialized_end=816,
)


_VERTEXRECORDKEYPB_PKPROPERTIESENTRY = _descriptor.Descriptor(
  name='PkPropertiesEntry',
  full_name='gs.rpc.write_service.v1.VertexRecordKeyPb.PkPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gs.rpc.write_service.v1.VertexRecordKeyPb.PkPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='gs.rpc.write_service.v1.VertexRecordKeyPb.PkPropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=940,
  serialized_end=991,
)

_VERTEXRECORDKEYPB = _descriptor.Descriptor(
  name='VertexRecordKeyPb',
  full_name='gs.rpc.write_service.v1.VertexRecordKeyPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='gs.rpc.write_service.v1.VertexRecordKeyPb.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pk_properties', full_name='gs.rpc.write_service.v1.VertexRecordKeyPb.pk_properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VERTEXRECORDKEYPB_PKPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=991,
)


_EDGERECORDKEYPB = _descriptor.Descriptor(
  name='EdgeRecordKeyPb',
  full_name='gs.rpc.write_service.v1.EdgeRecordKeyPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='gs.rpc.write_service.v1.EdgeRecordKeyPb.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_vertex_key', full_name='gs.rpc.write_service.v1.EdgeRecordKeyPb.src_vertex_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst_vertex_key', full_name='gs.rpc.write_service.v1.EdgeRecordKeyPb.dst_vertex_key', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inner_id', full_name='gs.rpc.write_service.v1.EdgeRecordKeyPb.inner_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=994,
  serialized_end=1180,
)

_BATCHWRITEREQUEST.fields_by_name['write_requests'].message_type = _WRITEREQUESTPB
_WRITEREQUESTPB.fields_by_name['write_type'].enum_type = _WRITETYPEPB
_WRITEREQUESTPB.fields_by_name['data_record'].message_type = _DATARECORDPB
_DATARECORDPB_PROPERTIESENTRY.containing_type = _DATARECORDPB
_DATARECORDPB.fields_by_name['vertex_record_key'].message_type = _VERTEXRECORDKEYPB
_DATARECORDPB.fields_by_name['edge_record_key'].message_type = _EDGERECORDKEYPB
_DATARECORDPB.fields_by_name['properties'].message_type = _DATARECORDPB_PROPERTIESENTRY
_DATARECORDPB.oneofs_by_name['record_key'].fields.append(
  _DATARECORDPB.fields_by_name['vertex_record_key'])
_DATARECORDPB.fields_by_name['vertex_record_key'].containing_oneof = _DATARECORDPB.oneofs_by_name['record_key']
_DATARECORDPB.oneofs_by_name['record_key'].fields.append(
  _DATARECORDPB.fields_by_name['edge_record_key'])
_DATARECORDPB.fields_by_name['edge_record_key'].containing_oneof = _DATARECORDPB.oneofs_by_name['record_key']
_VERTEXRECORDKEYPB_PKPROPERTIESENTRY.containing_type = _VERTEXRECORDKEYPB
_VERTEXRECORDKEYPB.fields_by_name['pk_properties'].message_type = _VERTEXRECORDKEYPB_PKPROPERTIESENTRY
_EDGERECORDKEYPB.fields_by_name['src_vertex_key'].message_type = _VERTEXRECORDKEYPB
_EDGERECORDKEYPB.fields_by_name['dst_vertex_key'].message_type = _VERTEXRECORDKEYPB
DESCRIPTOR.message_types_by_name['GetClientIdRequest'] = _GETCLIENTIDREQUEST
DESCRIPTOR.message_types_by_name['GetClientIdResponse'] = _GETCLIENTIDRESPONSE
DESCRIPTOR.message_types_by_name['BatchWriteRequest'] = _BATCHWRITEREQUEST
DESCRIPTOR.message_types_by_name['BatchWriteResponse'] = _BATCHWRITERESPONSE
DESCRIPTOR.message_types_by_name['RemoteFlushRequest'] = _REMOTEFLUSHREQUEST
DESCRIPTOR.message_types_by_name['RemoteFlushResponse'] = _REMOTEFLUSHRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequestPb'] = _WRITEREQUESTPB
DESCRIPTOR.message_types_by_name['DataRecordPb'] = _DATARECORDPB
DESCRIPTOR.message_types_by_name['VertexRecordKeyPb'] = _VERTEXRECORDKEYPB
DESCRIPTOR.message_types_by_name['EdgeRecordKeyPb'] = _EDGERECORDKEYPB
DESCRIPTOR.enum_types_by_name['WriteTypePb'] = _WRITETYPEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetClientIdRequest = _reflection.GeneratedProtocolMessageType('GetClientIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTIDREQUEST,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.GetClientIdRequest)
  })
_sym_db.RegisterMessage(GetClientIdRequest)

GetClientIdResponse = _reflection.GeneratedProtocolMessageType('GetClientIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTIDRESPONSE,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.GetClientIdResponse)
  })
_sym_db.RegisterMessage(GetClientIdResponse)

BatchWriteRequest = _reflection.GeneratedProtocolMessageType('BatchWriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHWRITEREQUEST,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.BatchWriteRequest)
  })
_sym_db.RegisterMessage(BatchWriteRequest)

BatchWriteResponse = _reflection.GeneratedProtocolMessageType('BatchWriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHWRITERESPONSE,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.BatchWriteResponse)
  })
_sym_db.RegisterMessage(BatchWriteResponse)

RemoteFlushRequest = _reflection.GeneratedProtocolMessageType('RemoteFlushRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEFLUSHREQUEST,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.RemoteFlushRequest)
  })
_sym_db.RegisterMessage(RemoteFlushRequest)

RemoteFlushResponse = _reflection.GeneratedProtocolMessageType('RemoteFlushResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEFLUSHRESPONSE,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.RemoteFlushResponse)
  })
_sym_db.RegisterMessage(RemoteFlushResponse)

WriteRequestPb = _reflection.GeneratedProtocolMessageType('WriteRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUESTPB,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.WriteRequestPb)
  })
_sym_db.RegisterMessage(WriteRequestPb)

DataRecordPb = _reflection.GeneratedProtocolMessageType('DataRecordPb', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATARECORDPB_PROPERTIESENTRY,
    '__module__' : 'graphscope.proto.write_service_pb2'
    # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.DataRecordPb.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _DATARECORDPB,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.DataRecordPb)
  })
_sym_db.RegisterMessage(DataRecordPb)
_sym_db.RegisterMessage(DataRecordPb.PropertiesEntry)

VertexRecordKeyPb = _reflection.GeneratedProtocolMessageType('VertexRecordKeyPb', (_message.Message,), {

  'PkPropertiesEntry' : _reflection.GeneratedProtocolMessageType('PkPropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _VERTEXRECORDKEYPB_PKPROPERTIESENTRY,
    '__module__' : 'graphscope.proto.write_service_pb2'
    # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.VertexRecordKeyPb.PkPropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _VERTEXRECORDKEYPB,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.VertexRecordKeyPb)
  })
_sym_db.RegisterMessage(VertexRecordKeyPb)
_sym_db.RegisterMessage(VertexRecordKeyPb.PkPropertiesEntry)

EdgeRecordKeyPb = _reflection.GeneratedProtocolMessageType('EdgeRecordKeyPb', (_message.Message,), {
  'DESCRIPTOR' : _EDGERECORDKEYPB,
  '__module__' : 'graphscope.proto.write_service_pb2'
  # @@protoc_insertion_point(class_scope:gs.rpc.write_service.v1.EdgeRecordKeyPb)
  })
_sym_db.RegisterMessage(EdgeRecordKeyPb)


DESCRIPTOR._options = None
_DATARECORDPB_PROPERTIESENTRY._options = None
_VERTEXRECORDKEYPB_PKPROPERTIESENTRY._options = None

_CLIENTWRITE = _descriptor.ServiceDescriptor(
  name='ClientWrite',
  full_name='gs.rpc.write_service.v1.ClientWrite',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1247,
  serialized_end=1575,
  methods=[
  _descriptor.MethodDescriptor(
    name='getClientId',
    full_name='gs.rpc.write_service.v1.ClientWrite.getClientId',
    index=0,
    containing_service=None,
    input_type=_GETCLIENTIDREQUEST,
    output_type=_GETCLIENTIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='batchWrite',
    full_name='gs.rpc.write_service.v1.ClientWrite.batchWrite',
    index=1,
    containing_service=None,
    input_type=_BATCHWRITEREQUEST,
    output_type=_BATCHWRITERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='remoteFlush',
    full_name='gs.rpc.write_service.v1.ClientWrite.remoteFlush',
    index=2,
    containing_service=None,
    input_type=_REMOTEFLUSHREQUEST,
    output_type=_REMOTEFLUSHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTWRITE)

DESCRIPTOR.services_by_name['ClientWrite'] = _CLIENTWRITE

# @@protoc_insertion_point(module_scope)
