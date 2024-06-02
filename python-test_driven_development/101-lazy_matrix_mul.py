#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    try:
        # Perform matrix multiplication
        result_matrix = np.dot(m_a, m_b)
        return result_matrix

    except Exception as e:
        # Handle exceptions gracefully
        return f"{str(e)}"
