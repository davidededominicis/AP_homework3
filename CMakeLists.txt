cmake_minimum_required(VERSION 3.12)
project(advanced_programming_homework_3)

#find_package(pybind11 REQUIRED)
#include_directories(SYSTEM ${pybind11_INCLUDE_DIRS})


##################################################

# OLD PART

##################################################

add_compile_options(-std=c++17 -Wall -Wextra -Wpedantic) 

# --COMPILE CSVPARSER SHARED LIBRARY--

### find Boost
find_package(Boost 1.82.0 REQUIRED)
if(Boost_FOUND)
    message("Boost found")
    include_directories(${BOOST_ROOT}/boost/include)
else()
    message(FATAL_ERROR "Boost not found")
endif()

set(pybind11_DIR "${CMAKE_CURRENT_SOURCE_DIR}/ext/pybind_installation/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

### compile csvparser.so
pybind11_add_module(csvparser src/csvparser.hpp src/csvparser.cpp src/csv_bind.cpp)

### include header files for the library
target_include_directories(csvparser PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

### link against Boost and any other necessary libraries
target_link_libraries(csvparser PRIVATE ${Boost_LIBRARIES})
