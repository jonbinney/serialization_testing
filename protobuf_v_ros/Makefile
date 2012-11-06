include $(shell rospack find mk)/cmake.mk

# make the protobuf messages
PROTOBUF_SRC_DIR=msg_protobuf
PROTOBUF_PYTHON_OUT_DIR=src/protobuf_v_ros/
protobuf:
	protoc -I${PROTOBUF_SRC_DIR} --python_out=${PROTOBUF_PYTHON_OUT_DIR} ${PROTOBUF_SRC_DIR}/messages.proto
