import roslib; roslib.load_manifest('protobuf_v_ros')
import time, random
from StringIO import StringIO
import rospy
from protobuf_v_ros import messages_pb2
import geometry_msgs.msg as gm

N = 10000

ros_messages_before = []
ros_messages_serialized = []
ros_messages_after = []
proto_messages_before = []
proto_messages_serialized = []
proto_messages_after = []

# create un-serialized messages of each type
for msg_i in xrange(N):
    p_ros = gm.Pose()
    p_proto = messages_pb2.Pose()

    p_ros.position.x = p_proto.position.x = random.random()
    p_ros.position.y = p_proto.position.y = random.random()
    p_ros.position.z = p_proto.position.z = random.random()

    p_ros.orientation.x = p_proto.orientation.x = random.random()
    p_ros.orientation.y = p_proto.orientation.y = random.random()
    p_ros.orientation.z = p_proto.orientation.z = random.random()
    p_ros.orientation.w = p_proto.orientation.w = 1.0
    
    ros_messages_before.append(p_ros)
    proto_messages_before.append(p_proto)
        
# serialize N times using ROS
ros_messages_serialized = [StringIO() for msg in ros_messages_before]
t0 = time.time()
for msg_i, msg in enumerate(ros_messages_before):
    msg.serialize(ros_messages_serialized[msg_i])
t1 = time.time()
print 'Serializing %d times with ROS took %f seconds' % (N, t1 - t0)

# serialize N times using protobuf
t0 = time.time()
for proto_msg in proto_messages_before:
    proto_messages_serialized.append(proto_msg.SerializeToString())
t1 = time.time()
print 'Serializing %d times with protobuf took %f seconds' % (N, t1 - t0)

# deserialize N times using ROS
t0 = time.time()
for sio in ros_messages_serialized:
    msg = gm.Pose().deserialize(sio.getvalue())
    ros_messages_after.append(msg)
t1 = time.time()
print 'Deserializing %d times with ROS took %f seconds' % (N, t1 - t0)

# deserialize N times using protobuf
t0 = time.time()
for proto_msg_str in proto_messages_serialized:
    msg_proto = messages_pb2.Pose()
    ros_messages_after.append(msg_proto.FromString(proto_msg_str))
t1 = time.time()
print 'Deserializing %d times with protobuf took %f seconds' % (N, t1 - t0)
