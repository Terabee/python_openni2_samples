#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openni import openni2
import platform

# Initialize OpenNI
if platform.system() == "Windows":
    openni2.initialize("C:/Program Files/OpenNI2/Redist")  # Specify path for Redist
else:
    openni2.initialize()  # can also accept the path of the OpenNI redistribution

# Connect and open device
dev = openni2.Device.open_any()

# Create depth stream
depth_stream = dev.create_depth_stream()
depth_stream.start()

while True:
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    print("Center pixel distance is {} mm".format(frame_data[2440]))
depth_stream.stop()
openni2.unload()
