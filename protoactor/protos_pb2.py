# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos_pb2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos_pb2.proto',
  package='actor',
  syntax='proto3',
  serialized_pb=_b('\n\x10protos_pb2.proto\x12\x05\x61\x63tor\"\"\n\x03PID\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\x0c\n\nPoisonPill\"$\n\x05Watch\x12\x1b\n\x07watcher\x18\x01 \x01(\x0b\x32\n.actor.PID\"&\n\x07Unwatch\x12\x1b\n\x07watcher\x18\x01 \x01(\x0b\x32\n.actor.PID\"A\n\nTerminated\x12\x17\n\x03who\x18\x01 \x01(\x0b\x32\n.actor.PID\x12\x1a\n\x12\x61\x64\x64ress_terminated\x18\x02 \x01(\x08\"\x06\n\x04Stopb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PID = _descriptor.Descriptor(
  name='PID',
  full_name='actor.PID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='actor.PID.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='actor.PID.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=61,
)


_POISONPILL = _descriptor.Descriptor(
  name='PoisonPill',
  full_name='actor.PoisonPill',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=75,
)


_WATCH = _descriptor.Descriptor(
  name='Watch',
  full_name='actor.Watch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='watcher', full_name='actor.Watch.watcher', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=113,
)


_UNWATCH = _descriptor.Descriptor(
  name='Unwatch',
  full_name='actor.Unwatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='watcher', full_name='actor.Unwatch.watcher', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=153,
)


_TERMINATED = _descriptor.Descriptor(
  name='Terminated',
  full_name='actor.Terminated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='who', full_name='actor.Terminated.who', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address_terminated', full_name='actor.Terminated.address_terminated', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=220,
)


_STOP = _descriptor.Descriptor(
  name='Stop',
  full_name='actor.Stop',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=228,
)

_WATCH.fields_by_name['watcher'].message_type = _PID
_UNWATCH.fields_by_name['watcher'].message_type = _PID
_TERMINATED.fields_by_name['who'].message_type = _PID
DESCRIPTOR.message_types_by_name['PID'] = _PID
DESCRIPTOR.message_types_by_name['PoisonPill'] = _POISONPILL
DESCRIPTOR.message_types_by_name['Watch'] = _WATCH
DESCRIPTOR.message_types_by_name['Unwatch'] = _UNWATCH
DESCRIPTOR.message_types_by_name['Terminated'] = _TERMINATED
DESCRIPTOR.message_types_by_name['Stop'] = _STOP

PID = _reflection.GeneratedProtocolMessageType('PID', (_message.Message,), dict(
  DESCRIPTOR = _PID,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.PID)
  ))
_sym_db.RegisterMessage(PID)

PoisonPill = _reflection.GeneratedProtocolMessageType('PoisonPill', (_message.Message,), dict(
  DESCRIPTOR = _POISONPILL,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.PoisonPill)
  ))
_sym_db.RegisterMessage(PoisonPill)

Watch = _reflection.GeneratedProtocolMessageType('Watch', (_message.Message,), dict(
  DESCRIPTOR = _WATCH,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.Watch)
  ))
_sym_db.RegisterMessage(Watch)

Unwatch = _reflection.GeneratedProtocolMessageType('Unwatch', (_message.Message,), dict(
  DESCRIPTOR = _UNWATCH,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.Unwatch)
  ))
_sym_db.RegisterMessage(Unwatch)

Terminated = _reflection.GeneratedProtocolMessageType('Terminated', (_message.Message,), dict(
  DESCRIPTOR = _TERMINATED,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.Terminated)
  ))
_sym_db.RegisterMessage(Terminated)

Stop = _reflection.GeneratedProtocolMessageType('Stop', (_message.Message,), dict(
  DESCRIPTOR = _STOP,
  __module__ = 'protos_pb2_pb2'
  # @@protoc_insertion_point(class_scope:actor.Stop)
  ))
_sym_db.RegisterMessage(Stop)


# @@protoc_insertion_point(module_scope)
