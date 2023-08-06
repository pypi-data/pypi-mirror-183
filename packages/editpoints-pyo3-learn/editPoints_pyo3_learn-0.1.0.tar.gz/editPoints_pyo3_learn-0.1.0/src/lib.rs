use pyo3::prelude::*;

#[pyfunction]
//write a funciton to scale a point
fn scale_value(value: f32, scale: f32) -> f32 {
    value * scale
}

#[pymodule]
fn editPoints_pyo3_learn(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(scale_value, m)?)?;
    Ok(())
}