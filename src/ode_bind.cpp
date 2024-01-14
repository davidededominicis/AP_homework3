#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
#include "odesolver.hpp"

namespace py = pybind11;

PYBIND11_MODULE(odesolver, m) {
    m.doc() = "Python bind of CSVParser class";

    // Dichiarazione della classe ODESolution
    py::class_<ODESolution>(m, "ODESolution")
        .def_readwrite("t", &ODESolution::t)
        .def_readwrite("Y", &ODESolution::Y);

    py::class_<ODESolver>(m, "ODESolver")
        .def(py::init([](function<VectorXd(double, VectorXd)> fun, double t_start, double t_end, VectorXd y0) {
            return new ODESolver(fun, t_start, t_end, y0);
        }))
        .def("RK4", &ODESolver::RK4)
        .def("RK4_csv", &ODESolver::RK4_csv)
        .def("midpoint", &ODESolver::midpoint)
        .def("midpoint_csv", &ODESolver::midpoint_csv)
        .def("euler", &ODESolver::euler)
        .def("euler_csv", &ODESolver::euler_csv)
        .def("accuracy", &ODESolver::accuracy)
        .def("efficiency", &ODESolver::efficiency)
        .def("stability", &ODESolver::stability)
        .def("convergence", &ODESolver::convergence);
}
