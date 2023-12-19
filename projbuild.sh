#!/bin/bash

# builds dynamic libraries???

set -x # print commands executed

BOOST_ROOT=$1 # example: ~/Desktop/uni/advanced_programming/homeworks/extlib
EIGEN_PATH=$2 # example: /usr/local/include/eigen3
PYBIND_PATH=$3 # example: ...

# execute cmake command

if [ -d "./build" ]; then # checks if folder exist
	rm -r build
fi
mkdir build
cd build
cmake -DBOOST_ROOT=${BOOST_ROOT} -DEIGEN_PATH=${EIGEN_PATH} ..
make
cd ..
