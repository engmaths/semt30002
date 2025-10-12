"""
This code solves a trivial linear system Au = b where
A is the identity matrix and b is a random vector using
dense and sparse matrices.  The memory is profiled
using the memory_profiler package
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve 
from memory_profiler import profile

@profile
def build_and_solve(matrix_type):
    """
    This function builds and solves the linear system.
    The argument is a string, either "dense" or "sparse"
    that determines whether dense or sparse matrices
    and linear algebra are used
    """

    # Set the size of the linear system
    N = 10000

    # Make the RHS vector random
    b = np.random.random(N)

    # solve using dense matrices
    if matrix_type == 'dense':
        A = np.eye(N)
        u = np.linalg.solve(A, b)

    # solve using sparse matrices
    elif matrix_type == 'sparse':
        A = sp.eye(N, format = 'csc')
        u = spsolve(A, b)

    else:
        print('unknown matrix type')


# Run the function with dense matrices
# build_and_solve(matrix_type='dense')

# Run the function with sparse matrices
build_and_solve(matrix_type='sparse')