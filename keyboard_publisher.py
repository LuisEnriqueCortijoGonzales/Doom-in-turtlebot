#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from pynput import keyboard

def on_press(key):
    try:
        key_map = {
            keyboard.Key.up: "UP",
            keyboard.Key.down: "DOWN",
            keyboard.Key.left: "LEFT",
            keyboard.Key.right: "RIGHT"
        }
        
        if key in key_map:
            print(f"Tecla presionada: {key_map[key]}")
            pub.publish(key_map[key])

    except AttributeError:
        pass
def on_release(key):
    if key == keyboard.Key.esc:
        return False
rospy.init_node('keyboard_publisher')
pub = rospy.Publisher('/doom_cmd', String, queue_size=10)

print("Presiona las flechas para mover el TurtleBot en DOOM (ESC para salir)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
