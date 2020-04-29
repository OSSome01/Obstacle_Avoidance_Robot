#!/usr/bin/env python 
import rospy
import time
from sensor_msgs.msg import geometry_msgs, LaserScan
from geometry_msgs.msg import Twist

def callback_laser(msg): # callback function for subscriber
    # divide total laser scan of 180 degrees into 5 parts
    regions = {
            'right':  min(min(msg.ranges[0:143]), 10),
            'fright': min(min(msg.ranges[144:287]), 10),
            'front':  min(min(msg.ranges[288:431]), 10),
            'fleft':  min(min(msg.ranges[432:575]), 10),
            'left':   min(min(msg.ranges[576:713]), 10),
    }
    avoid_obst(regions)

def avoid_obst(regions):
    msg = Twist()
    linear_x = 0
    angular_z = 0
    
    state_description = ''
    # check obstacle position and move accordingly
    if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 1 - no obstacle in range'
        linear_x = 0.6
        angular_z = 0
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
        state_description = 'case 2 - obstacle position front'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 3 - obstacle position fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 4 - obstacle position fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
        state_description = 'case 5 - obstacle position front and fright'
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
        state_description = 'case 6 - obstacle position front and fleft'
        linear_x = 0
        angular_z = -0.3
    elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 7 - obstacle position front and fleft and fright'
        time.sleep(0.1)
        linear_x = 0
        angular_z = 0.3
    elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
        state_description = 'case 8 - obstacle position fleft and fright'
        linear_x = 0.3
        angular_z = 0
    else:
        state_description = 'unknown case'
        rospy.loginfo(regions)
 
    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    msg.angular.z = -angular_z
    pub.publish(msg)

def main():
    global pub
    rospy.init_node('reading_laser')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('obst_avoidance_robot/laser/scan', LaserScan, callback_laser)
    rospy.spin()

if __name__ == '__main__':
    main()

