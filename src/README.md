## Examine of the publisher Lambda function 

```
#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;


```


"rclcpp/rclcpp.hpp" includes which allows to use the most common pieces of the ROS  system.
<br>
"std_msgs/msg/string.hpp" includes the builtin massage type you will use to publish data.
<br>

These following lines represents the node's dependancies have to be added to "package.xml" and "CMakeLists.txt"
<br>

```
public:
  MinimalPublisher()
  : Node("minimal_publisher"), count_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
    auto timer_callback =
      [this]() -> void {
        auto message = std_msgs::msg::String();
        message.data = "Hello, world! " + std::to_string(this->count_++);
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        this->publisher_->publish(message);
      };
    timer_ = this->create_wall_timer(500ms, timer_callback);
  }

```

<br>
The public constructor names the node minimal_publisher and initializes count_ to 0. Inside the constructor, the publisher is initialized with the String message type, the topic name topic, and the required queue size to limit messages in the event of a backup. Next, a lambda function called timer_callback is declared. It performs a by-reference capture of the current object this, takes no input arguments and returns void. The timer_callback function creates a new message of type String, sets its data with the desired string and publishes it. The RCLCPP_INFO macro ensures every published message is printed to the console. At last, timer_ is initialized, which causes the timer_callback function to be executed twice a second.

<br>
In the bottom of the class is the declaration of the timer, publisher, and counter fields.
<br>
```
    private:
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
```
<br>

Following the MinimalPublisher class is main, where the node actually executes. rclcpp::init initializes ROS 2, and rclcpp::spin starts processing data from the node, including callbacks from the timer.
<br>
```
    int main(int argc, char * argv[])
    {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalPublisher>());
    rclcpp::shutdown();
    return 0;
    }

```

## Add dependancies 

open package.xml.<br>

Add a new line after the ament_cmake buildtool dependency and paste the following dependencies corresponding to your node’s include statements:
<br>

```
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```
<br>
This declares the package needs "rclcpp" and "std_msgs" 


open CMakelists.txt <br>

Now open the CMakeLists.txt file. Below the existing dependency find_package(ament_cmake REQUIRED), add the lines: 
<br>

```
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

```
<br>

