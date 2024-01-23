import rospy
from pynput import keyboard
from component_apis.base.base import FORWARD, TURN, STOP, BaseNode

""" 
    @Zix
    This node will listen for key presses which are matched with desired commands of the base.
    Uses the ASDF keys for the desired movements by publishing the correct message to the 
    base action server in real time. 
"""

def on_key_press(key, base_node):
    try:
        if key.char == 'a':
            FORWARD(base_node.base_pub)
        elif key.char == 's':
            STOP(base_node.base_pub)
        elif key.char == 'd':
            TURN(base_node.base_pub)
        elif key.char == 'f':
            FORWARD(base_node.base_pub)
    except AttributeError:
        pass

def print_welcome():
    rospy.loginfo("BASE NODE TURNED ON")
    rospy.loginfo("########################################################################################")
    rospy.loginfo("########################################################################################")
    rospy.loginfo("########################################################################################")
    rospy.loginfo("Welcome to the base node! This node will give you control of the robot bases")
    rospy.loginfo("You can use the keyboard input to give common commands to the bases")
    rospy.loginfo("a. Open Left Base")
    rospy.loginfo("s. Close Left Base")
    rospy.loginfo("d. Open Right Base")
    rospy.loginfo("f. Close Right Base")
    rospy.loginfo("########################################################################################")

def init_node():
    rospy.init_node('BaseNode')
    base_node = BaseNode()
    print_welcome()
    with keyboard.Listener(
        on_press=lambda key: on_key_press(key, base_node)
    ) as listener:
        listener.join()

if __name__ == "__main__" :
    try:
        init_node()
    except rospy.ROSInterruptException:
        pass