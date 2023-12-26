cmake_minimum_required(VERSION 3.4...3.18)
project(MyProject)

# Specify the paths to Boost and pybind11 if they are not in standard locations
set(Boost_INCLUDE_DIR "/path/to/boost")
set(pybind11_DIR "/ath/to/pybind11/share/cmake/pybind11")

find_package(pybind11 REQUIRED) # Find pybind11
find_package(Boost REQUIRED COMPONENTS accumulator) # Find Boost

pybind11_add_module(my_module my_module.cpp) # Add your module
target_include_directories(my_module PRIVATE ${Boost_INCLUDE_DIR})
target_link_libraries(my_module PRIVATE Boost::boost Boost::accumulator) # Link Boost libraries

