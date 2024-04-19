import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Define parameter directory (assuming same location for all parameters)
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
            get_package_share_directory('my_camera'),
            'param',
            'size.yaml'
        )
    )

    return LaunchDescription([
        # Declare parameter argument (shared by all nodes)
        DeclareLaunchArgument(
            'param_dir',
            default_value=param_dir
        ),

        # Launch img_publisher node
        Node(
            package='my_camera',
            executable='img_publisher',
            name='img_publisher',
            parameters=[LaunchConfiguration('param_dir')],
            output='screen'
        ),

        # Launch canny_edge_filter node with remapping
        Node(
            package='my_camera',
            executable='canny_edge_filter',
            name='canny_edge_filter',
            parameters=[LaunchConfiguration('param_dir')],
            remappings=[
                ('camera', '/camera')  # Remap input topic to match img_publisher
            ],
            output='screen'
        ),
        Node(
            package='my_camera',  # Assuming your package name
            executable='red_filter',
            name='red_filter',
            remappings=[
                ('camera_image', '/camera'),  # Remap input topic from img_publisher
                ('red_filtered_image', '/red_filtered_image'),  # Custom output topic
            ],
            output='screen'
        ),
        Node(
            package='my_camera',  # Assuming your package name
            executable='green_filter',
            name='green_filter',
            remappings=[
                ('camera_image', '/camera'),  # Subscribe to red filter output
                ('green_filtered_image', '/green_filtered_image'),  # Custom output topic
            ],
            output='screen'
        ),
        Node(
            package='my_camera',  # Assuming your package name
            executable='blue_filter',
            name='blue_filter',
            remappings=[
                ('camera_image', '/camera'),  # Remap input topic from img_publisher
                ('blue_filtered_image', '/blue_filtered_image'),  # Custom output topic
            ],
            output='screen'
        )

    ]
)
