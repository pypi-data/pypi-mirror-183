#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "trimesh.h"

namespace py = pybind11;

namespace fast_trimesh {
namespace cpu {
namespace ops {

trimesh::Trimesh3D linear_extrude(const trimesh::Trimesh2D &mesh, float height);

void add_modules(py::module &m);

}  // namespace ops
}  // namespace cpu
}  // namespace fast_trimesh
