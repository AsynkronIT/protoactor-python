# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: examples/remote_benchmark/messages/protos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protoactor.actor import protos_pb2 as protoactor_dot_actor_dot_protos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='examples/remote_benchmark/messages/protos.proto',
  package='messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/examples/remote_benchmark/messages/protos.proto\x12\x08messages\x1a\x1dprotoactor/actor/protos.proto\"\x07\n\x05Start\")\n\x0bStartRemote\x12\x1a\n\x06Sender\x18\x01 \x01(\x0b\x32\n.actor.PID\"\x06\n\x04Ping\"\x06\n\x04Pongb\x06proto3')
  ,
  dependencies=[protoactor_dot_actor_dot_protos__pb2.DESCRIPTOR,])




_START = _descriptor.Descriptor(
  name='Start',
  full_name='messages.Start',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=92,
  serialized_end=99,
)


_STARTREMOTE = _descriptor.Descriptor(
  name='StartRemote',
  full_name='messages.StartRemote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Sender', full_name='messages.StartRemote.Sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=101,
  serialized_end=142,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='messages.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=144,
  serialized_end=150,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='messages.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=152,
  serialized_end=158,
)

_STARTREMOTE.fields_by_name['Sender'].message_type = protoactor_dot_actor_dot_protos__pb2._PID
DESCRIPTOR.message_types_by_name['Start'] = _START
DESCRIPTOR.message_types_by_name['StartRemote'] = _STARTREMOTE
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Start = _reflection.GeneratedProtocolMessageType('Start', (_message.Message,), {
  'DESCRIPTOR' : _START,
  '__module__' : 'examples.remote_benchmark.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.Start)
  })
_sym_db.RegisterMessage(Start)

StartRemote = _reflection.GeneratedProtocolMessageType('StartRemote', (_message.Message,), {
  'DESCRIPTOR' : _STARTREMOTE,
  '__module__' : 'examples.remote_benchmark.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.StartRemote)
  })
_sym_db.RegisterMessage(StartRemote)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'examples.remote_benchmark.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.Ping)
  })
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'examples.remote_benchmark.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.Pong)
  })
_sym_db.RegisterMessage(Pong)


# @@protoc_insertion_point(module_scope)
