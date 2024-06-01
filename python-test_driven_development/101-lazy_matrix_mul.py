#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Convert lists to NumPy arrays
    m_a_num = np.array(m_a)
    m_b_num = np.array(m_b)

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("invalid data type for einsum")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("invalid data type for einsum")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("setting an array element with a sequence.")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("setting an array element with a sequence.")

    m_a_num_0, m_a_num_1 = m_a_num.shape()
    m_b_num_0, m_b_num_1 = m_b_num.shape()

    if m_a_num_1 != m_b_num_0:
        raise ValueError("shapes {} and {} not aligned: {} (dim 1) != {} \
                         (dim 0)".format(m_a_num.shape(), m_b_num.shape(),
                                         m_a_num_1, m_b_num_0))

    return (np.matmul(m_a, m_b))
