
## URDF - Unified Robot Description Format 
<br>
This is structured XML file contain the robot details. 
```
Tree of links connected by Joints
```

URDF format is following like this.
<br>

```
<?xml version="1.0"?>
<robot name="my_bot">
    <link name="arm_link">
        <visual>
            <geometry></geometry>
            <origin></origin>
            <material></material>
        </visual>
        <collision>
            <geometry></geometry>
            <origin></origin>
        </collision>
        <inertial>
            <mass></mass>
            <origin></origin>
            <inertia></inertia>
        </inertial>
    </link>

    <joint name="base_to_arm_link>
        <parent>  # parent link
        <child>   # child link
        <origin>  # fixed transformation from parent link
        <axis>    # the rotation axis
        <limit>   # limits - upper and lower boundary.
    </joint>

</robot>
```
## Xacro - XML Macro

Ros processing tool uesed to simplify URDF files. It acts as a preprocessor. It acts as a pre-processor, converting clean, modular code into single comprehensive URDF for robot_state_publisher.

| To enable this use this code in the <robot>

```
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
```

1. Modular Design (xacro:include)

    Xacro allows you to split massive URDFs into smaller, manageable files (e.g., separating sensors, materials, and the robot core).

* How it works: Use the <xacro:include filename="file.xacro" /> tag to "copy-paste" contents of one file into your main file.
* Benefits: Easier debugging, cleaner version control (Git), and reusable components across different robot projects.

2. Efficiency Tools (The "DRY" Principle)

    Xacro prevents manual errors and redundancy by using programming-like features:

* Properties (Variables)

    Define a value once and reference it everywhere. Changing the value in one place updates the entire robot.

    Syntax: <xacro:property name="width" value="0.2" />
    Usage: <box size="${width} 0.1 0.1" />
    Math Expressions

    Perform calculations directly within tags using ${}. It supports basic operators and constants like pi.

    Example: length="${2 * arm_radius}"
    Macros (Templates)

    Create reusable templates for complex code blocks (like inertial matrices). You define the logic once and call it with different parameters.

    ![alt text](image.png)


    