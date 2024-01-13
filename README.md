# Advanced Programming - Homework 3

## GROUP MEMBERS
Sara Carpenè – saracarpene01@gmail.com Davide De Dominicis – dedominicis2001@gmail.com Andrea Gottardi – andreagottardi24@gmail.com

## CODE ORGANIZATION
We created the bindings for c++ and python integration using pybind11. Firstly, we used the bindings to implements in python the classes for the csv parser and the ODE solver of the previous homework. Secondly, we wrote python scripts to showcases the code functionalities and to compare the time efficience of the python and c++ implementations. To achieve this goal we exploited advanced python features, such as scientific computing libraries and decorators.

## STRUCTURE
```bash
├── src: contains the csvparser and odesolver source codes and the code for the binding
├── apps: contains the python code and the tests
├── csv_examples: contains the csv file used in testing csv parser
└── ext: contains the pybind11 installation
```

## INSTALL AND TEST
The script *./projbuild.sh* compiles csvparser and odesolver using pybind11. The packages are saved in a build folder and they can be directly imported in a python file. To build the packages use the command: *./projbuild.sh /path/to/boost path/to/eigen3*. It is requested the version 1.82.0 of Boost. The boost installation folder must contain a boost folder, which contains an include folder.
The result will be saved in a build directory inside the main project directory.

To test the executables on a predetermined example execute *./testbuild.sh*. In order to change the dataset on which maincsv is executed is necessary to modify the given dataset in the testbuild.sh file or execute the command *./maincsv datasetname.csv outputfile_name.
## INDIVIDUAL CONTRIBUTION
- pybind11 bindings: Gottardi
- python and c++ integration: Carpenè, De Dominicis
- functionalities and performance testing: Carpené, De Dominicis
- project organization, scripts, CMake: Gottardi
