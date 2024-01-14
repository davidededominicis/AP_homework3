# Advanced Programming - Homework 3

## GROUP MEMBERS
Sara Carpenè – saracarpene01@gmail.com Davide De Dominicis – dedominicis2001@gmail.com Andrea Gottardi – andreagottardi24@gmail.com

## CODE ORGANIZATION
We created the bindings for c++ and python integration using pybind11. 
Initially, we leveraged bindings to implement in Python the classes for the CSV parser and the ODE solver from the previous assignment. We enhanced these classes with functions to replicate the results achieved with the C++ version, but using Python libraries and custom functions developed by us.
Next, we composed Python scripts to demonstrate the functionality of the code and to contrast the efficiency of the Python and C++ implementations in terms of execution time. To accomplish this, we harnessed Python's advanced features, such as scientific computing libraries and decorators.

### Brief description of CSVParser
This module accepts a CSV file as a command line argument. The decision was made to implement the CSVParser as a class. The dataset, the header (containing the names of the columns), and the size of the dataset (corresponding to the number of columns) are stored as private members. The Boost library was chosen to carry out the statistical operations.
The main function creates an instance of the CSVParser class. When the function read() is invoked, the data in the CSV file is stored in "dataset". The "dataset" is a private member of the "CSVParser" and is a two-dimensional vector that stores information in columns. Each column is homogeneous and can consist of doubles or strings. It can handle missing values using std::optional. For the columns, certain operations can be performed.
-Double columns: mean, variance, median, standard deviation, covariance between two double columns, correlation analysis between two columns, frequency count.
-String columns: frequency count.
There are two more methods:
Summary: for all the columns it computes all possible operations (according to column type), and saves the results in the specified file.
Classification: allows to find the rows where a wanted word appears and save the results in a specified txt file. You need to indicate the index of the column in which you want to search for the wanted word.

### Brief description of the ODESolver class
The ODEsolver class within the module embodies a Cauchy problem. The instantiation of this class necessitates the specification of the differential equation to be resolved, the initial point, and the interval within which the solution must be computed. The Eigen library was employed to conduct operations involving vectors.

The Cauchy problem resolution methods implemented are Runge Kutta 4, Euler's method, and the midpoint method. Each of these methods is encapsulated within two functions, the first bearing the name of the method and the second carrying 'csv'. The first function returns an object where various t_n and y1, y2, y3, etc., are stored for future use in other computations. The second function prints the results into a .csv file. Other functions facilitate the assessment of the adequacy of numerical methods.
### Note:
With respect to the previous implementation of this modules (see Homework 2) we modified some methos to ensure correct bindings. 
For example we defined a customized data type for the solutions ode the method for solving ODEs, and we changed the type of the FrequencyCount function.


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
- python, c++ integration, data type corections: Carpenè, De Dominicis
- functionalities and performance testing: Carpené, De Dominicis
- project organization, scripts, CMake: Gottardi
