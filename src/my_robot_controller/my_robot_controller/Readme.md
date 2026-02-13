## After you run this the terminal looks like this. 

![alt text](image.png)
Note that this happen without spin


## Install the Node

Go to the setup.py and edit this : 
``` 
entry_points={
        'console_scripts': [
            'test_node = my_robot_controller.my_first_node:main'
        ]
```


After this build the pakage and source it.

```
cd ../..
colcon build 
source ~/.bashrc
ros2 run my_robot_controller  test_node
```


Set a timer inside the node 

The method is make a another function inside the Node and call it within create_timer function like in the code. 

```
    class MyNode(Node):
        def __init__(self):
            super().__init__('my_node') # name of the node
            self.counter_ = 0
            self.create_timer(1.0, self.timer_callback)

        def timer_callback(self):
            self.get_logger().info("Timer callback called"+ str(self.counter_))
            self.counter_ += 1
        
```


Get the node info 

```
# find the node list 
ros2 node list 
# get the node info 
ros2 node info /<your_node>
```

The output should be like this: 
![alt text](image-1.png)


Get rqt graph 

```
rqt_graph 
```

![alt text](image-2.png)