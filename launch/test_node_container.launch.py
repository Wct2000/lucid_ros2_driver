# Copyright 2020 Tier IV, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.actions import LoadComposableNodes
from launch_ros.descriptions import ComposableNode
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch.actions import TimerAction

from launch import LaunchContext

import yaml


def generate_launch_description():
    launch_arguments = []

    context = LaunchContext()

    camera_param_path_camera_1 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_1.yaml"
    )

    camera_param_path_camera_2 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_2.yaml"
    )

    camera_param_path_camera_3 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_3.yaml"
    )

    '''camera_param_path_camera_4 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_4.yaml"
    )

    camera_param_path_camera_5 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_5.yaml"
    )'''

    '''camera_param_path_camera_6 = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.camera_6.yaml"
    )'''

    camera_1 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_1",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_1],
        remappings=[],
    )

    camera_2 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_2",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_2],
        remappings=[],
    )

    camera_3 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_3",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_3],
        remappings=[],
    )

    '''camera_4 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_4",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_4],
        remappings=[],
    )

    camera_5 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_5",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_5],
        remappings=[],
    )'''

    '''camera_6 = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_camera_6",
        namespace="camera_lucid",
        parameters=[camera_param_path_camera_6],
        remappings=[],
    )'''

    return LaunchDescription(
        [
        *launch_arguments,
        camera_1,
        camera_2,
        camera_3,
        #camera_4,
        #camera_5,
        #TimerAction(period=3.0, actions=[camera_2]),
        #TimerAction(period=6.0, actions=[camera_3]),
        #TimerAction(period=9.0, actions=[camera_4]),
        #TimerAction(period=12.0, actions=[camera_5]),
        #camera_6,
        ]
    )