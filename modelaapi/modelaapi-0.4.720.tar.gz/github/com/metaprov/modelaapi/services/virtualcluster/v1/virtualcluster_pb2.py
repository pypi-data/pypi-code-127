# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/virtualcluster/v1/virtualcluster.proto
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
from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.services.common.v1 import common_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_common_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgithub.com/metaprov/modelaapi/services/virtualcluster/v1/virtualcluster.proto\x12\x38github.com.metaprov.modelaapi.services.virtualcluster.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\x1a=github.com/metaprov/modelaapi/services/common/v1/common.proto\"\xec\x01\n\x1aListVirtualClustersRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x82\x01\n\x0fvirtualclusters\x18\x03 \x03(\x0b\x32i.github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersRequest.VirtualclustersEntry\x1a\x36\n\x14VirtualclustersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x81\x01\n\x1bListVirtualClustersResponse\x12\x62\n\x0fvirtualclusters\x18\x01 \x01(\x0b\x32I.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualClusterList\"\x18\n\x16VirtualClusterResponse\"|\n\x1b\x43reateVirtualClusterRequest\x12]\n\x0evirtualcluster\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualCluster\"\x1e\n\x1c\x43reateVirtualClusterResponse\"\xac\x01\n\x1bUpdateVirtualClusterRequest\x12]\n\x0evirtualcluster\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualCluster\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1e\n\x1cUpdateVirtualClusterResponse\";\n\x18GetVirtualClusterRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x88\x01\n\x19GetVirtualClusterResponse\x12]\n\x0evirtualcluster\x18\x01 \x01(\x0b\x32\x45.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualCluster\x12\x0c\n\x04yaml\x18\x02 \x01(\t\">\n\x1b\x44\x65leteVirtualClusterRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1e\n\x1c\x44\x65leteVirtualClusterResponse2\xff\t\n\x15VirtualClusterService\x12\xeb\x01\n\x13ListVirtualClusters\x12T.github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersRequest\x1aU.github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/virtualclusters/{namespace}\x12\xe5\x01\n\x14\x43reateVirtualCluster\x12U.github.com.metaprov.modelaapi.services.virtualcluster.v1.CreateVirtualClusterRequest\x1aV.github.com.metaprov.modelaapi.services.virtualcluster.v1.CreateVirtualClusterResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/virtualclusters:\x01*\x12\xec\x01\n\x11GetVirtualCluster\x12R.github.com.metaprov.modelaapi.services.virtualcluster.v1.GetVirtualClusterRequest\x1aS.github.com.metaprov.modelaapi.services.virtualcluster.v1.GetVirtualClusterResponse\".\x82\xd3\xe4\x93\x02(\x12&/v1/virtualclusters/{namespace}/{name}\x12\xa8\x02\n\x14UpdateVirtualCluster\x12U.github.com.metaprov.modelaapi.services.virtualcluster.v1.UpdateVirtualClusterRequest\x1aV.github.com.metaprov.modelaapi.services.virtualcluster.v1.UpdateVirtualClusterResponse\"a\x82\xd3\xe4\x93\x02[\x1aV/v1/virtualclusters/{virtualcluster.metadata.namespace}/{virtualcluster.metadata.name}:\x01*\x12\xf5\x01\n\x14\x44\x65leteVirtualCluster\x12U.github.com.metaprov.modelaapi.services.virtualcluster.v1.DeleteVirtualClusterRequest\x1aV.github.com.metaprov.modelaapi.services.virtualcluster.v1.DeleteVirtualClusterResponse\".\x82\xd3\xe4\x93\x02(*&/v1/virtualclusters/{namespace}/{name}B:Z8github.com/metaprov/modelaapi/services/virtualcluster/v1b\x06proto3')



_LISTVIRTUALCLUSTERSREQUEST = DESCRIPTOR.message_types_by_name['ListVirtualClustersRequest']
_LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY = _LISTVIRTUALCLUSTERSREQUEST.nested_types_by_name['VirtualclustersEntry']
_LISTVIRTUALCLUSTERSRESPONSE = DESCRIPTOR.message_types_by_name['ListVirtualClustersResponse']
_VIRTUALCLUSTERRESPONSE = DESCRIPTOR.message_types_by_name['VirtualClusterResponse']
_CREATEVIRTUALCLUSTERREQUEST = DESCRIPTOR.message_types_by_name['CreateVirtualClusterRequest']
_CREATEVIRTUALCLUSTERRESPONSE = DESCRIPTOR.message_types_by_name['CreateVirtualClusterResponse']
_UPDATEVIRTUALCLUSTERREQUEST = DESCRIPTOR.message_types_by_name['UpdateVirtualClusterRequest']
_UPDATEVIRTUALCLUSTERRESPONSE = DESCRIPTOR.message_types_by_name['UpdateVirtualClusterResponse']
_GETVIRTUALCLUSTERREQUEST = DESCRIPTOR.message_types_by_name['GetVirtualClusterRequest']
_GETVIRTUALCLUSTERRESPONSE = DESCRIPTOR.message_types_by_name['GetVirtualClusterResponse']
_DELETEVIRTUALCLUSTERREQUEST = DESCRIPTOR.message_types_by_name['DeleteVirtualClusterRequest']
_DELETEVIRTUALCLUSTERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteVirtualClusterResponse']
ListVirtualClustersRequest = _reflection.GeneratedProtocolMessageType('ListVirtualClustersRequest', (_message.Message,), {

  'VirtualclustersEntry' : _reflection.GeneratedProtocolMessageType('VirtualclustersEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersRequest.VirtualclustersEntry)
    })
  ,
  'DESCRIPTOR' : _LISTVIRTUALCLUSTERSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersRequest)
  })
_sym_db.RegisterMessage(ListVirtualClustersRequest)
_sym_db.RegisterMessage(ListVirtualClustersRequest.VirtualclustersEntry)

ListVirtualClustersResponse = _reflection.GeneratedProtocolMessageType('ListVirtualClustersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVIRTUALCLUSTERSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.ListVirtualClustersResponse)
  })
_sym_db.RegisterMessage(ListVirtualClustersResponse)

VirtualClusterResponse = _reflection.GeneratedProtocolMessageType('VirtualClusterResponse', (_message.Message,), {
  'DESCRIPTOR' : _VIRTUALCLUSTERRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.VirtualClusterResponse)
  })
_sym_db.RegisterMessage(VirtualClusterResponse)

CreateVirtualClusterRequest = _reflection.GeneratedProtocolMessageType('CreateVirtualClusterRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIRTUALCLUSTERREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.CreateVirtualClusterRequest)
  })
_sym_db.RegisterMessage(CreateVirtualClusterRequest)

CreateVirtualClusterResponse = _reflection.GeneratedProtocolMessageType('CreateVirtualClusterResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIRTUALCLUSTERRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.CreateVirtualClusterResponse)
  })
_sym_db.RegisterMessage(CreateVirtualClusterResponse)

UpdateVirtualClusterRequest = _reflection.GeneratedProtocolMessageType('UpdateVirtualClusterRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIRTUALCLUSTERREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.UpdateVirtualClusterRequest)
  })
_sym_db.RegisterMessage(UpdateVirtualClusterRequest)

UpdateVirtualClusterResponse = _reflection.GeneratedProtocolMessageType('UpdateVirtualClusterResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIRTUALCLUSTERRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.UpdateVirtualClusterResponse)
  })
_sym_db.RegisterMessage(UpdateVirtualClusterResponse)

GetVirtualClusterRequest = _reflection.GeneratedProtocolMessageType('GetVirtualClusterRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVIRTUALCLUSTERREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.GetVirtualClusterRequest)
  })
_sym_db.RegisterMessage(GetVirtualClusterRequest)

GetVirtualClusterResponse = _reflection.GeneratedProtocolMessageType('GetVirtualClusterResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVIRTUALCLUSTERRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.GetVirtualClusterResponse)
  })
_sym_db.RegisterMessage(GetVirtualClusterResponse)

DeleteVirtualClusterRequest = _reflection.GeneratedProtocolMessageType('DeleteVirtualClusterRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVIRTUALCLUSTERREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.DeleteVirtualClusterRequest)
  })
_sym_db.RegisterMessage(DeleteVirtualClusterRequest)

DeleteVirtualClusterResponse = _reflection.GeneratedProtocolMessageType('DeleteVirtualClusterResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVIRTUALCLUSTERRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.virtualcluster.v1.virtualcluster_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.virtualcluster.v1.DeleteVirtualClusterResponse)
  })
_sym_db.RegisterMessage(DeleteVirtualClusterResponse)

_VIRTUALCLUSTERSERVICE = DESCRIPTOR.services_by_name['VirtualClusterService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/metaprov/modelaapi/services/virtualcluster/v1'
  _LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY._options = None
  _LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY._serialized_options = b'8\001'
  _VIRTUALCLUSTERSERVICE.methods_by_name['ListVirtualClusters']._options = None
  _VIRTUALCLUSTERSERVICE.methods_by_name['ListVirtualClusters']._serialized_options = b'\202\323\344\223\002!\022\037/v1/virtualclusters/{namespace}'
  _VIRTUALCLUSTERSERVICE.methods_by_name['CreateVirtualCluster']._options = None
  _VIRTUALCLUSTERSERVICE.methods_by_name['CreateVirtualCluster']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/virtualclusters:\001*'
  _VIRTUALCLUSTERSERVICE.methods_by_name['GetVirtualCluster']._options = None
  _VIRTUALCLUSTERSERVICE.methods_by_name['GetVirtualCluster']._serialized_options = b'\202\323\344\223\002(\022&/v1/virtualclusters/{namespace}/{name}'
  _VIRTUALCLUSTERSERVICE.methods_by_name['UpdateVirtualCluster']._options = None
  _VIRTUALCLUSTERSERVICE.methods_by_name['UpdateVirtualCluster']._serialized_options = b'\202\323\344\223\002[\032V/v1/virtualclusters/{virtualcluster.metadata.namespace}/{virtualcluster.metadata.name}:\001*'
  _VIRTUALCLUSTERSERVICE.methods_by_name['DeleteVirtualCluster']._options = None
  _VIRTUALCLUSTERSERVICE.methods_by_name['DeleteVirtualCluster']._serialized_options = b'\202\323\344\223\002(*&/v1/virtualclusters/{namespace}/{name}'
  _LISTVIRTUALCLUSTERSREQUEST._serialized_start=338
  _LISTVIRTUALCLUSTERSREQUEST._serialized_end=574
  _LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY._serialized_start=520
  _LISTVIRTUALCLUSTERSREQUEST_VIRTUALCLUSTERSENTRY._serialized_end=574
  _LISTVIRTUALCLUSTERSRESPONSE._serialized_start=577
  _LISTVIRTUALCLUSTERSRESPONSE._serialized_end=706
  _VIRTUALCLUSTERRESPONSE._serialized_start=708
  _VIRTUALCLUSTERRESPONSE._serialized_end=732
  _CREATEVIRTUALCLUSTERREQUEST._serialized_start=734
  _CREATEVIRTUALCLUSTERREQUEST._serialized_end=858
  _CREATEVIRTUALCLUSTERRESPONSE._serialized_start=860
  _CREATEVIRTUALCLUSTERRESPONSE._serialized_end=890
  _UPDATEVIRTUALCLUSTERREQUEST._serialized_start=893
  _UPDATEVIRTUALCLUSTERREQUEST._serialized_end=1065
  _UPDATEVIRTUALCLUSTERRESPONSE._serialized_start=1067
  _UPDATEVIRTUALCLUSTERRESPONSE._serialized_end=1097
  _GETVIRTUALCLUSTERREQUEST._serialized_start=1099
  _GETVIRTUALCLUSTERREQUEST._serialized_end=1158
  _GETVIRTUALCLUSTERRESPONSE._serialized_start=1161
  _GETVIRTUALCLUSTERRESPONSE._serialized_end=1297
  _DELETEVIRTUALCLUSTERREQUEST._serialized_start=1299
  _DELETEVIRTUALCLUSTERREQUEST._serialized_end=1361
  _DELETEVIRTUALCLUSTERRESPONSE._serialized_start=1363
  _DELETEVIRTUALCLUSTERRESPONSE._serialized_end=1393
  _VIRTUALCLUSTERSERVICE._serialized_start=1396
  _VIRTUALCLUSTERSERVICE._serialized_end=2675
# @@protoc_insertion_point(module_scope)
