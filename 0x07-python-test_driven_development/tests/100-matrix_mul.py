#!/usr/bin/python3
"""Module that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(x, (int, float)) for j in m_a for x in j):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for j in m_b for x in j):
        raise TypeError("m_a should contain only integers or floats")
