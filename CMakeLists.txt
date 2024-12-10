cmake_minimum_required(VERSION 3.5)
project(mecademic_description)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

# Install URDF and mesh files
install(DIRECTORY urdf meshes
  DESTINATION share/${PROJECT_NAME}
)

# Install RViz configuration files
# install(DIRECTORY rviz
#   DESTINATION share/${PROJECT_NAME}
# )

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Specify package dependencies
ament_package()

