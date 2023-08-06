use pyo3::prelude::*;

/// Fill a line of text at a given width.
///
/// ```python
/// wraptext.fill("Memory safety without garbage collection.", 15)
/// # "Memory safety\nwithout garbage\ncollection."
/// ```
#[pyfunction]
fn fill(
    text: &str,
    width: usize,
    initial_indent: Option<&str>,
    subsequent_indent: Option<&str>,
    break_words: Option<bool>,
) -> PyResult<String> {
    Ok(textwrap::fill(
        text,
        textwrap::Options::new(width)
            .initial_indent(&initial_indent.unwrap_or(""))
            .subsequent_indent(&subsequent_indent.unwrap_or(""))
            .break_words(break_words.unwrap_or(true))
        )
    )
}

#[pymodule]
fn wraptext(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fill, m)?)?;
    Ok(())
}
