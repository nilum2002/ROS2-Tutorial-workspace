#!/usr/bin/env python3

import rclpy
from  rclpy.node  import Node



class NodeOpTemplate(Node):
    def __init__(self):
        super().__init__('node_op_template') # name of the node
        


def main(args = None):
    rclpy.init(args=args) # initialize 
    
    # create the node 
    myNode = NodeOpTemplate()

    rclpy.spin(myNode) # keep the node alive and processing callbacks

    rclpy.shutdown() # shutdown 


if __name__ == '__main__':
    main()
