#!/usr/bin/env python3

import rclpy 
from  rclpy.node  import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.action.server import ServerGoalHandle
# include the action 
from my_robot_interface.action import CountUntil
import time


class CountUntilServerNode(Node):
    def __init__(self):
        super().__init__('count_until_server') # name of the node
        self.count_until_server_ = ActionServer(
            self, 
            CountUntil, 
            "count_until", 
            execute_callback= self.execute_callback,
            )
        self.get_logger().info("Count Until Action Server has been started.")

    def execute_callback(self, goal_handle: ServerGoalHandle):
        # Get request from the goal
        target_number =  goal_handle.request.target_number
        period =  goal_handle.request.period

        # execute
        self.get_logger().info("Executing the Goal")
        counter =0
        for i in range(target_number):
            counter += 1
            self.get_logger().info(f"counter:{counter}")
            time.sleep(period) 

        # Return the result 
        
        # one done, the goal final state
        
        goal_handle.succeed() # set the goal state to succeeded

        # send result back to the client
        result = CountUntil.Result()
        result.reached_number = counter

        return result

def main(args = None):
    rclpy.init(args=args) # initialize the ROS2 communication in python
    
    # create the node 
    myNode = CountUntilServerNode()

    rclpy.spin(myNode) # keep the node alive and processing callbacks

    rclpy.shutdown() # shutdown the ROS2 communication in python

if __name__ == '__main__':
    main()
