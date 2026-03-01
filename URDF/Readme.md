

## Create urdf for the robot with Liadr

![alt text](image.png)


Commands:

View urdf in Rviz :

```
ros2 launch urdf_tutorial display.launch.py model:=<file path_to_urdf>
```

View frames:
```
ros2 run tf2_tools view_frames
```

This will generate a pdf of frame(Tree structure)
