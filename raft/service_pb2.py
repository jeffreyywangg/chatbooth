# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"<\n\x16RaftRequestVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\t\"\'\n\x17RaftRequestVoteResponse\x12\x0c\n\x04vote\x18\x01 \x01(\x08\":\n\x16RaftUpdateStateRequest\x12\x12\n\nreplica_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"9\n\x13\x41uthenticateRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"-\n\x0bListRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07request\x18\x02 \x01(\t\"<\n\x0bSendRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"\x1f\n\x0e\x44\x65liverRequest\x12\r\n\x05token\x18\x01 \x01(\t\"0\n\rDeleteRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"3\n\x0eStringResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08response\x18\x02 \x01(\t\" \n\rEmptyResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xfb\x02\n\x0eMessageService\x12\x46\n\x0fRaftRequestVote\x12\x17.RaftRequestVoteRequest\x1a\x18.RaftRequestVoteResponse\"\x00\x12<\n\x0fRaftUpdateState\x12\x17.RaftUpdateStateRequest\x1a\x0e.EmptyResponse\"\x00\x12\x37\n\x0c\x41uthenticate\x12\x14.AuthenticateRequest\x1a\x0f.StringResponse\"\x00\x12\'\n\x04List\x12\x0c.ListRequest\x1a\x0f.StringResponse\"\x00\x12&\n\x04Send\x12\x0c.SendRequest\x1a\x0e.EmptyResponse\"\x00\x12-\n\x07\x44\x65liver\x12\x0f.DeliverRequest\x1a\x0f.StringResponse\"\x00\x12*\n\x06\x44\x65lete\x12\x0e.DeleteRequest\x1a\x0e.EmptyResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RAFTREQUESTVOTEREQUEST._serialized_start=17
  _RAFTREQUESTVOTEREQUEST._serialized_end=77
  _RAFTREQUESTVOTERESPONSE._serialized_start=79
  _RAFTREQUESTVOTERESPONSE._serialized_end=118
  _RAFTUPDATESTATEREQUEST._serialized_start=120
  _RAFTUPDATESTATEREQUEST._serialized_end=178
  _AUTHENTICATEREQUEST._serialized_start=180
  _AUTHENTICATEREQUEST._serialized_end=237
  _LISTREQUEST._serialized_start=239
  _LISTREQUEST._serialized_end=284
  _SENDREQUEST._serialized_start=286
  _SENDREQUEST._serialized_end=346
  _DELIVERREQUEST._serialized_start=348
  _DELIVERREQUEST._serialized_end=379
  _DELETEREQUEST._serialized_start=381
  _DELETEREQUEST._serialized_end=429
  _STRINGRESPONSE._serialized_start=431
  _STRINGRESPONSE._serialized_end=482
  _EMPTYRESPONSE._serialized_start=484
  _EMPTYRESPONSE._serialized_end=516
  _MESSAGESERVICE._serialized_start=519
  _MESSAGESERVICE._serialized_end=898
# @@protoc_insertion_point(module_scope)
