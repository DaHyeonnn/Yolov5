## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

from email.mime import image
import pyrealsense2 as rs
import numpy as np
import cv2

"""
RealSense 카메라를 사용하여 실시간 이미지 처리 및 표시
"""
# Configure depth and color streams
pipeline = rs.pipeline() #realsense pipeline 생성
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline) 
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device() #디바이스 호출
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False #RGB 카메라 여부
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

# config.enable_stream(rs.stream.depth, 640, 480, rs.format.bgr8, 30)

if device_product_line != 'L500':
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    print('ok')

# Start streaming
pipeline.start(config)

try:
    while True: #무한루프를 통해 컬러 프레임을 계속해서 받아옴

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()

        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        color_colormap_dim = color_image.shape
        
        images = np.stack(color_image)
        images = cv2.flip(images, 1) #좌우반전
        
        # Show image
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()
