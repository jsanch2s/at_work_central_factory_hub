# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='AttentionMessage.proto',
  package='rockin_msgs',
  serialized_pb='\n\x16\x41ttentionMessage.proto\x12\x0brockin_msgs\"o\n\x10\x41ttentionMessage\x12\x0f\n\x07message\x18\x01 \x02(\t\x12\x14\n\x0ctime_to_show\x18\x02 \x01(\x02\x12\x0c\n\x04team\x18\x03 \x01(\t\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\xd0\x0f\x12\x0c\n\x08MSG_TYPE\x10\x02\x42\x30\n\x16org.rockin.common_msgsB\x16\x41ttentionMessageProtos')



_ATTENTIONMESSAGE_COMPTYPE = descriptor.EnumDescriptor(
  name='CompType',
  full_name='rockin_msgs.AttentionMessage.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=2000,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=112,
  serialized_end=150,
)


_ATTENTIONMESSAGE = descriptor.Descriptor(
  name='AttentionMessage',
  full_name='rockin_msgs.AttentionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='rockin_msgs.AttentionMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_to_show', full_name='rockin_msgs.AttentionMessage.time_to_show', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='team', full_name='rockin_msgs.AttentionMessage.team', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATTENTIONMESSAGE_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=39,
  serialized_end=150,
)

_ATTENTIONMESSAGE_COMPTYPE.containing_type = _ATTENTIONMESSAGE;
DESCRIPTOR.message_types_by_name['AttentionMessage'] = _ATTENTIONMESSAGE

class AttentionMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTENTIONMESSAGE
  
  # @@protoc_insertion_point(class_scope:rockin_msgs.AttentionMessage)

# @@protoc_insertion_point(module_scope)