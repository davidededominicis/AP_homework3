# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build

# Include any dependencies generated for this target.
include CMakeFiles/odesolver.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/odesolver.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/odesolver.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/odesolver.dir/flags.make

CMakeFiles/odesolver.dir/src/odesolver.cpp.o: CMakeFiles/odesolver.dir/flags.make
CMakeFiles/odesolver.dir/src/odesolver.cpp.o: /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/odesolver.cpp
CMakeFiles/odesolver.dir/src/odesolver.cpp.o: CMakeFiles/odesolver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/odesolver.dir/src/odesolver.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/odesolver.dir/src/odesolver.cpp.o -MF CMakeFiles/odesolver.dir/src/odesolver.cpp.o.d -o CMakeFiles/odesolver.dir/src/odesolver.cpp.o -c /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/odesolver.cpp

CMakeFiles/odesolver.dir/src/odesolver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/odesolver.dir/src/odesolver.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/odesolver.cpp > CMakeFiles/odesolver.dir/src/odesolver.cpp.i

CMakeFiles/odesolver.dir/src/odesolver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/odesolver.dir/src/odesolver.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/odesolver.cpp -o CMakeFiles/odesolver.dir/src/odesolver.cpp.s

CMakeFiles/odesolver.dir/src/ode_bind.cpp.o: CMakeFiles/odesolver.dir/flags.make
CMakeFiles/odesolver.dir/src/ode_bind.cpp.o: /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/ode_bind.cpp
CMakeFiles/odesolver.dir/src/ode_bind.cpp.o: CMakeFiles/odesolver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/odesolver.dir/src/ode_bind.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/odesolver.dir/src/ode_bind.cpp.o -MF CMakeFiles/odesolver.dir/src/ode_bind.cpp.o.d -o CMakeFiles/odesolver.dir/src/ode_bind.cpp.o -c /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/ode_bind.cpp

CMakeFiles/odesolver.dir/src/ode_bind.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/odesolver.dir/src/ode_bind.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/ode_bind.cpp > CMakeFiles/odesolver.dir/src/ode_bind.cpp.i

CMakeFiles/odesolver.dir/src/ode_bind.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/odesolver.dir/src/ode_bind.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/src/ode_bind.cpp -o CMakeFiles/odesolver.dir/src/ode_bind.cpp.s

# Object files for target odesolver
odesolver_OBJECTS = \
"CMakeFiles/odesolver.dir/src/odesolver.cpp.o" \
"CMakeFiles/odesolver.dir/src/ode_bind.cpp.o"

# External object files for target odesolver
odesolver_EXTERNAL_OBJECTS =

odesolver.cpython-311-x86_64-linux-gnu.so: CMakeFiles/odesolver.dir/src/odesolver.cpp.o
odesolver.cpython-311-x86_64-linux-gnu.so: CMakeFiles/odesolver.dir/src/ode_bind.cpp.o
odesolver.cpython-311-x86_64-linux-gnu.so: CMakeFiles/odesolver.dir/build.make
odesolver.cpython-311-x86_64-linux-gnu.so: CMakeFiles/odesolver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared module odesolver.cpython-311-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/odesolver.dir/link.txt --verbose=$(VERBOSE)
	/usr/bin/strip /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build/odesolver.cpython-311-x86_64-linux-gnu.so

# Rule to build all files generated by this target.
CMakeFiles/odesolver.dir/build: odesolver.cpython-311-x86_64-linux-gnu.so
.PHONY : CMakeFiles/odesolver.dir/build

CMakeFiles/odesolver.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/odesolver.dir/cmake_clean.cmake
.PHONY : CMakeFiles/odesolver.dir/clean

CMakeFiles/odesolver.dir/depend:
	cd /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3 /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3 /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build /home/andreg/Desktop/uni/ap/homeworks/hm3/AP_homework3/build/CMakeFiles/odesolver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/odesolver.dir/depend
