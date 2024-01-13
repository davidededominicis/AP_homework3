#include <pybind11/pybind11.h>
#include "csvparser.hpp"

namespace py = pybind11;

PYBIND11_MODULE(csvparser, m) {
	m.doc() = "Python bind of CSVParser class";

	py::class_<CSVParser>(m, "CSVParser")
		.def(py::init([](const string& input_file) {
			return new CSVParser(input_file);
		}))
		.def("read", &CSVParser::read)
		.def("mean_col", &CSVParser::mean_col)
		.def("var_col", &CSVParser::var_col)
		.def("median_col", &CSVParser::median_col)
		.def("std_dev", &CSVParser::std_dev)
		.def("covar", &CSVParser::covar)
		.def("correlation_analysis", &CSVParser::correlation_analysis)
		.def("countFrequency", &CSVParser::countFrequency)
		.def("summary", &CSVParser::summary)
		.def("classification", &CSVParser::classification);
}
