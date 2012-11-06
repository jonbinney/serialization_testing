To use the ros_v_protobuf package, first do:

```bash
sudo apt-get install python-protobuf
```

Next add this serialization_testing to your ROS_PACKAGE_PATH. roscd to protobuf_v_ros, and type:

```bash
make
```

If you'll look in the Makefile for that package, you'll see the hack to generate the protobuf message wrappers.
Finally, run the test script:

```bash
python scripts/encode_decode.py
```

This will serialize and deserialize Pose messages many times, and output how much time it took. In the test, I 
pre-construct the StringIO instances that ROS serializes into, since I think it would normally create one 
and re-use it.