#!/user/bin/env python3

import rclpy # python lib for ROS2
from  rclpy.node  import Node


class MyNode(Node):
    def __init__(self):
        super().__init__('my_node') # name of the node
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Timer callback called"+ str(self.counter_))
        self.counter_ += 1
        
      





def main(args = None):
    rclpy.init(args=args) # initialize the ROS2 communication in python

    # create the node 
    myNode = MyNode()

    rclpy.spin(myNode) # keep the node alive and processing callbacks

    rclpy.shutdown() # shutdown the ROS2 communication


    pass 




if __name__ == '__main__':
    main()
