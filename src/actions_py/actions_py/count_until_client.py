#!/usr/bin/env python3

import rclpy
from  rclpy.node  import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle
from my_robot_interface.action import CountUntil



class CountUntilClient(Node):
    def __init__(self):
        super().__init__("count_until_client") # name of the node
        self.count_until_client_ = ActionClient(self, CountUntil, "count_until")

    def send_goal(self, target_number, period):
        # wait for the server 
        self.count_until_client_.wait_for_server()

        # create goal 
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = period

        # send the goal 
        self.get_logger().info("Sending goal")
        self.count_until_client_.send_goal_async(goal).add_done_callback(self.goal_response_callback) # block 
    
    def goal_response_callback(self, future):
        self.goal_handle : ClientGoalHandle = future.result()
        if self.goal_handle.accepted:
            self.get_logger().info("Goal accepted")
            self.goal_handle.get_result_async().add_done_callback(self.goal_result_callback)
        else :
            self.get_logger().info("Goal rejected")
            
    def goal_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result.reached_number}")


def main(args = None):
    rclpy.init(args=args) # initialize 
    
    # create the node 
    myNode = CountUntilClient()
    myNode.send_goal(10, 1.0)
    rclpy.spin(myNode) # keep the node alive and processing callbacks

    rclpy.shutdown() # shutdown 


if __name__ == '__main__':
    main()
