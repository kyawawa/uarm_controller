cmake_minimum_required(VERSION 2.8.3)
project(uarm_controller)

find_package(catkin REQUIRED COMPONENTS
  ps3joy
  rospy
  std_msgs
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES uarm_controller
#  CATKIN_DEPENDS ps3joy rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
