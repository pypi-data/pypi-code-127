# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/runbook/v1/runbook.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_team_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?github.com/metaprov/modelaapi/services/runbook/v1/runbook.proto\x12\x31github.com.metaprov.modelaapi.services.runbook.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/team/v1alpha1/generated.proto\"\xf4\x01\n\x13ListRunBooksRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x62\n\x06labels\x18\x02 \x03(\x0b\x32R.github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x14ListRunBooksResponse\x12S\n\x08runbooks\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.RunBookList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"f\n\x14\x43reateRunBookRequest\x12N\n\x07runbook\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.RunBook\"\x17\n\x15\x43reateRunBookResponse\"\x96\x01\n\x14UpdateRunBookRequest\x12N\n\x07runbook\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.RunBook\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x17\n\x15UpdateRunBookResponse\"4\n\x11GetRunBookRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"r\n\x12GetRunBookResponse\x12N\n\x07runbook\x18\x01 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.team.v1alpha1.RunBook\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"7\n\x14\x44\x65leteRunBookRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteRunBookResponse2\x98\x08\n\x0eRunBookService\x12\xc1\x01\n\x0cListRunBooks\x12\x46.github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksRequest\x1aG.github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/runbooks/{namespace}\x12\xbb\x01\n\rCreateRunBook\x12G.github.com.metaprov.modelaapi.services.runbook.v1.CreateRunBookRequest\x1aH.github.com.metaprov.modelaapi.services.runbook.v1.CreateRunBookResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/runbooks:\x01*\x12\xc2\x01\n\nGetRunBook\x12\x44.github.com.metaprov.modelaapi.services.runbook.v1.GetRunBookRequest\x1a\x45.github.com.metaprov.modelaapi.services.runbook.v1.GetRunBookResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/runbooks/{namespace}/{name}\x12\xf0\x01\n\rUpdateRunBook\x12G.github.com.metaprov.modelaapi.services.runbook.v1.UpdateRunBookRequest\x1aH.github.com.metaprov.modelaapi.services.runbook.v1.UpdateRunBookResponse\"L\x82\xd3\xe4\x93\x02\x46\x1a\x41/v1/runbooks/{runbook.metadata.namespace}/{runbook.metadata.name}:\x01*\x12\xcb\x01\n\rDeleteRunBook\x12G.github.com.metaprov.modelaapi.services.runbook.v1.DeleteRunBookRequest\x1aH.github.com.metaprov.modelaapi.services.runbook.v1.DeleteRunBookResponse\"\'\x82\xd3\xe4\x93\x02!*\x1f/v1/runbooks/{namespace}/{name}B3Z1github.com/metaprov/modelaapi/services/runbook/v1b\x06proto3')



_LISTRUNBOOKSREQUEST = DESCRIPTOR.message_types_by_name['ListRunBooksRequest']
_LISTRUNBOOKSREQUEST_LABELSENTRY = _LISTRUNBOOKSREQUEST.nested_types_by_name['LabelsEntry']
_LISTRUNBOOKSRESPONSE = DESCRIPTOR.message_types_by_name['ListRunBooksResponse']
_CREATERUNBOOKREQUEST = DESCRIPTOR.message_types_by_name['CreateRunBookRequest']
_CREATERUNBOOKRESPONSE = DESCRIPTOR.message_types_by_name['CreateRunBookResponse']
_UPDATERUNBOOKREQUEST = DESCRIPTOR.message_types_by_name['UpdateRunBookRequest']
_UPDATERUNBOOKRESPONSE = DESCRIPTOR.message_types_by_name['UpdateRunBookResponse']
_GETRUNBOOKREQUEST = DESCRIPTOR.message_types_by_name['GetRunBookRequest']
_GETRUNBOOKRESPONSE = DESCRIPTOR.message_types_by_name['GetRunBookResponse']
_DELETERUNBOOKREQUEST = DESCRIPTOR.message_types_by_name['DeleteRunBookRequest']
_DELETERUNBOOKRESPONSE = DESCRIPTOR.message_types_by_name['DeleteRunBookResponse']
ListRunBooksRequest = _reflection.GeneratedProtocolMessageType('ListRunBooksRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTRUNBOOKSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTRUNBOOKSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksRequest)
  })
_sym_db.RegisterMessage(ListRunBooksRequest)
_sym_db.RegisterMessage(ListRunBooksRequest.LabelsEntry)

ListRunBooksResponse = _reflection.GeneratedProtocolMessageType('ListRunBooksResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRUNBOOKSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.ListRunBooksResponse)
  })
_sym_db.RegisterMessage(ListRunBooksResponse)

CreateRunBookRequest = _reflection.GeneratedProtocolMessageType('CreateRunBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATERUNBOOKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.CreateRunBookRequest)
  })
_sym_db.RegisterMessage(CreateRunBookRequest)

CreateRunBookResponse = _reflection.GeneratedProtocolMessageType('CreateRunBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERUNBOOKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.CreateRunBookResponse)
  })
_sym_db.RegisterMessage(CreateRunBookResponse)

UpdateRunBookRequest = _reflection.GeneratedProtocolMessageType('UpdateRunBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERUNBOOKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.UpdateRunBookRequest)
  })
_sym_db.RegisterMessage(UpdateRunBookRequest)

UpdateRunBookResponse = _reflection.GeneratedProtocolMessageType('UpdateRunBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERUNBOOKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.UpdateRunBookResponse)
  })
_sym_db.RegisterMessage(UpdateRunBookResponse)

GetRunBookRequest = _reflection.GeneratedProtocolMessageType('GetRunBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNBOOKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.GetRunBookRequest)
  })
_sym_db.RegisterMessage(GetRunBookRequest)

GetRunBookResponse = _reflection.GeneratedProtocolMessageType('GetRunBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRUNBOOKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.GetRunBookResponse)
  })
_sym_db.RegisterMessage(GetRunBookResponse)

DeleteRunBookRequest = _reflection.GeneratedProtocolMessageType('DeleteRunBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERUNBOOKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.DeleteRunBookRequest)
  })
_sym_db.RegisterMessage(DeleteRunBookRequest)

DeleteRunBookResponse = _reflection.GeneratedProtocolMessageType('DeleteRunBookResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERUNBOOKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.runbook.v1.runbook_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.runbook.v1.DeleteRunBookResponse)
  })
_sym_db.RegisterMessage(DeleteRunBookResponse)

_RUNBOOKSERVICE = DESCRIPTOR.services_by_name['RunBookService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/metaprov/modelaapi/services/runbook/v1'
  _LISTRUNBOOKSREQUEST_LABELSENTRY._options = None
  _LISTRUNBOOKSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _RUNBOOKSERVICE.methods_by_name['ListRunBooks']._options = None
  _RUNBOOKSERVICE.methods_by_name['ListRunBooks']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/runbooks/{namespace}'
  _RUNBOOKSERVICE.methods_by_name['CreateRunBook']._options = None
  _RUNBOOKSERVICE.methods_by_name['CreateRunBook']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/runbooks:\001*'
  _RUNBOOKSERVICE.methods_by_name['GetRunBook']._options = None
  _RUNBOOKSERVICE.methods_by_name['GetRunBook']._serialized_options = b'\202\323\344\223\002!\022\037/v1/runbooks/{namespace}/{name}'
  _RUNBOOKSERVICE.methods_by_name['UpdateRunBook']._options = None
  _RUNBOOKSERVICE.methods_by_name['UpdateRunBook']._serialized_options = b'\202\323\344\223\002F\032A/v1/runbooks/{runbook.metadata.namespace}/{runbook.metadata.name}:\001*'
  _RUNBOOKSERVICE.methods_by_name['DeleteRunBook']._options = None
  _RUNBOOKSERVICE.methods_by_name['DeleteRunBook']._serialized_options = b'\202\323\344\223\002!*\037/v1/runbooks/{namespace}/{name}'
  _LISTRUNBOOKSREQUEST._serialized_start=253
  _LISTRUNBOOKSREQUEST._serialized_end=497
  _LISTRUNBOOKSREQUEST_LABELSENTRY._serialized_start=452
  _LISTRUNBOOKSREQUEST_LABELSENTRY._serialized_end=497
  _LISTRUNBOOKSRESPONSE._serialized_start=500
  _LISTRUNBOOKSRESPONSE._serialized_end=632
  _CREATERUNBOOKREQUEST._serialized_start=634
  _CREATERUNBOOKREQUEST._serialized_end=736
  _CREATERUNBOOKRESPONSE._serialized_start=738
  _CREATERUNBOOKRESPONSE._serialized_end=761
  _UPDATERUNBOOKREQUEST._serialized_start=764
  _UPDATERUNBOOKREQUEST._serialized_end=914
  _UPDATERUNBOOKRESPONSE._serialized_start=916
  _UPDATERUNBOOKRESPONSE._serialized_end=939
  _GETRUNBOOKREQUEST._serialized_start=941
  _GETRUNBOOKREQUEST._serialized_end=993
  _GETRUNBOOKRESPONSE._serialized_start=995
  _GETRUNBOOKRESPONSE._serialized_end=1109
  _DELETERUNBOOKREQUEST._serialized_start=1111
  _DELETERUNBOOKREQUEST._serialized_end=1166
  _DELETERUNBOOKRESPONSE._serialized_start=1168
  _DELETERUNBOOKRESPONSE._serialized_end=1191
  _RUNBOOKSERVICE._serialized_start=1194
  _RUNBOOKSERVICE._serialized_end=2242
# @@protoc_insertion_point(module_scope)
