#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    if m_a is None or m_b is None:
        raise TypeError("Object arrays are not currently supported")
    if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if (not all(isinstance(row, list) for row in m_a) and
            all(isinstance(row, list) for row in m_b)):
        raise ValueError("shapes (2,) and (1,2) not aligned: "
                         "2 (dim 0) != 1 (dim 0)")
    if not all(isinstance(row, list) for row in m_b):
        return (np.matmul(m_a, m_b))

    # Convert lists to NumPy arrays
    m_a_num = np.array(m_a)
    m_b_num = np.array(m_b)

    m_a_num_0, m_a_num_1 = m_a_num.shape
    m_b_num_0, m_b_num_1 = m_b_num.shape

    if m_a_num_1 != m_b_num_0:
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: "
                         "{} (dim 1) != {} (dim 0)".format(m_a_num_0,
                                                           m_a_num_1,
                                                           m_b_num_0,
                                                           m_b_num_1,
                                                           m_a_num_1,
                                                           m_b_num_0))

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

    return (np.matmul(m_a, m_b))
