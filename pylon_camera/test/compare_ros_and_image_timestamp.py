#!/usr/bin/env python
# simple script to test the feature to fetch camera's time stamp.
# compares ros time and camera time
import rospy
from sensor_msgs.msg import Image

prev_ros_time = prev_img_time = None

def callback(msg):
    global prev_ros_time, prev_img_time
    new_ros_time = rospy.Time.now()
    new_img_time = msg.header.stamp
    if prev_ros_time is not None and prev_img_time is not None:
        ros_dur = new_ros_time - prev_ros_time
        img_dur = new_img_time - prev_img_time
        rospy.loginfo('ros time: %d seconds and %d nanoseconds', new_ros_time.secs, new_ros_time.nsecs)
        rospy.loginfo('img time: %d seconds and %d nanoseconds', new_img_time.secs, new_img_time.nsecs)
        rospy.loginfo('ros duration: %d seconds and %d nanoseconds', ros_dur.secs, ros_dur.nsecs)
        rospy.loginfo('img duration: %d seconds and %d nanoseconds', img_dur.secs, img_dur.nsecs)
    prev_ros_time = new_ros_time
    prev_img_time = new_img_time

rospy.init_node('compare_ros_and_image_timestamp')
sub = rospy.Subscriber('/pylon_camera_node/image_raw', Image,  callback)
rospy.spin()