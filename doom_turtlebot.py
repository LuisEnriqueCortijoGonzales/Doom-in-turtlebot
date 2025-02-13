#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import os  
class DoomTurtleBot:
    def __init__(self):
        rospy.init_node("doom_turtlebot", anonymous=True)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.sub = rospy.Subscriber("/doom_cmd", String, self.move)
        self.twist = Twist()
        print("🕹️ Ejecutando DOOM en el TurtleBot3...")
        os.system("doom &")

    def move(self, msg):
        key = msg.data
        print(f"🔄 Comando recibido: {key}")
        if key == "UP":
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0
        elif key == "DOWN":
            self.twist.linear.x = -0.2
            self.twist.angular.z = 0.0
        elif key == "LEFT":
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.5
        elif key == "RIGHT":
            self.twist.linear.x = 0.0
            self.twist.angular.z = -0.5
        else:
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0

        self.cmd_vel_pub.publish(self.twist)

if __name__ == "__main__":
    DoomTurtleBot()
    rospy.spin()
