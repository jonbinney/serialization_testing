# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='messages.proto',
  package='protobuf_v_ros',
  serialized_pb='\n\x0emessages.proto\x12\x0eprotobuf_v_ros\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\x12\t\n\x01w\x18\x04 \x02(\x02\"`\n\x04Pose\x12\'\n\x08position\x18\x01 \x02(\x0b\x32\x15.protobuf_v_ros.Point\x12/\n\x0borientation\x18\x02 \x02(\x0b\x32\x1a.protobuf_v_ros.Quaternion')




_POINT = descriptor.Descriptor(
  name='Point',
  full_name='protobuf_v_ros.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='protobuf_v_ros.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='protobuf_v_ros.Point.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='protobuf_v_ros.Point.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=34,
  serialized_end=74,
)


_QUATERNION = descriptor.Descriptor(
  name='Quaternion',
  full_name='protobuf_v_ros.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='protobuf_v_ros.Quaternion.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='protobuf_v_ros.Quaternion.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='z', full_name='protobuf_v_ros.Quaternion.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='w', full_name='protobuf_v_ros.Quaternion.w', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=76,
  serialized_end=132,
)


_POSE = descriptor.Descriptor(
  name='Pose',
  full_name='protobuf_v_ros.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='position', full_name='protobuf_v_ros.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='orientation', full_name='protobuf_v_ros.Pose.orientation', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=134,
  serialized_end=230,
)

_POSE.fields_by_name['position'].message_type = _POINT
_POSE.fields_by_name['orientation'].message_type = _QUATERNION
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['Pose'] = _POSE

class Point(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POINT
  
  # @@protoc_insertion_point(class_scope:protobuf_v_ros.Point)

class Quaternion(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUATERNION
  
  # @@protoc_insertion_point(class_scope:protobuf_v_ros.Quaternion)

class Pose(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POSE
  
  # @@protoc_insertion_point(class_scope:protobuf_v_ros.Pose)

# @@protoc_insertion_point(module_scope)
