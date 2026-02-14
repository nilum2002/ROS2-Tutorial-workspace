#!/usr/bin/env python3

import rclpy
from  rclpy.node  import Node
from rclpy.action.client import ActionClient




class CountUntilClient(Node):
    def __init__(self):
        super().__init__("count_until_client") # name of the node
        


def main(args = None):
    rclpy.init(args=args) # initialize 
    
    # create the node 
    myNode = CountUntilClient()

    rclpy.spin(myNode) # keep the node alive and processing callbacks

    rclpy.shutdown() # shutdown 


if __name__ == '__main__':
    main()
