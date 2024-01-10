#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include "odesolver.hpp"
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(odesolver, m) {
	m.doc() = "Python bind of CSVParser class";

	py::class_<ODESolver>(m, "ODESolver")
	.def(py::init<const std::function<Eigen::VectorXd(double, Eigen::VectorXd)> &, double, double, Eigen::VectorXd &>())
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
