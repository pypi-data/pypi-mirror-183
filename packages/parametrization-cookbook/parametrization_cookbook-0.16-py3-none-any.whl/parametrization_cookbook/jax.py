# Copyright 2022, Jean-Benoist Leger <jbleger@hds.utc.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from .functions import jax as _jax_funs
from . import _common

import functools as _functools
import jax as _jax

_jax_class_decorator = _common.custom_class_decorator(
    backend=_jax_funs,
    method_decorator=_functools.partial(_jax.jit, static_argnums=0),
    method_notes="""Note
        ----
        This function use JAX defined functions using only LAX primitives
        and the control flow depends only on the shape of the object.
        Therefore, this method can be used in with `jax.jit` and gradient
        can be computed (e.g. `jax.grad`, `jax.jacfwd`, `jax.jacrev`) if
        forward mode and reverse mode.

        """,
)


@_jax_class_decorator
class Param(_common.Param):
    pass


@_jax_class_decorator
class Real(_common.Real):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value:

    >>> parametrization = Real()
    >>> parametrization.params_to_reals1d(0.5)
    DeviceArray([0.5], dtype=float32)
    >>> parametrization.reals1d_to_params(0.5)
    DeviceArray(0.5, dtype=float32)

    An example for the parametrization of a 3×3 matrix:

    >>> parametrization = Real(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[0,1,2],[3,4,5],[6,7,8]]))
    >>> one_dim_vec
    DeviceArray([0., 1., 2., 3., 4., 5., 6., 7., 8.], dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[0., 1., 2.],
                 [3., 4., 5.],
                 [6., 7., 8.]], dtype=float32)
    """


@_jax_class_decorator
class RealLowerBounded(_common.RealLowerBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5)
    >>> parametrization.params_to_reals1d(7)
    DeviceArray([1.8545866], dtype=float32)
    >>> parametrization.reals1d_to_params(1.8545866)
    DeviceArray(7., dtype=float32)

    An example for the parametrization of a 3×3 matrix of values in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[5.1,5.2,5.3],[5.5,5.6,5.7],[5.9,6,6.1]]))
    >>> one_dim_vec
    DeviceArray([-2.2521696 , -1.5077729 , -1.050225  , -0.43275213,
                 -0.19587052,  0.0136587 ,  0.37816477,  0.54132485,
                  0.6952279 ], dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[5.1, 5.2, 5.3],
                 [5.5, 5.6, 5.7],
                 [5.9, 6. , 6.1]], dtype=float32)
"""


@_jax_class_decorator
class RealPositive(_common.RealPositive):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar positive value:

    >>> parametrization = RealPositive()
    >>> parametrization.params_to_reals1d(0.5)
    DeviceArray([-0.43275213], dtype=float32)
    >>> parametrization.reals1d_to_params(-0.43275213)
    DeviceArray(0.49999997, dtype=float32)

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealPositive(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[0.1,0.2,0.3],[1.5,1.6,1.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    DeviceArray([-2.2521687, -1.5077717, -1.0502257,  1.2475176,  1.374483 ,
                  1.4982711,  2.8434052,  1.8545866,  1.9693712],            dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[0.09999998, 0.20000002, 0.29999995],
                 [1.5       , 1.6       , 1.7       ],
                 [2.9       , 2.        , 2.1       ]], dtype=float32)
    """


@_jax_class_decorator
class RealUpperBounded(_common.RealUpperBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5)
    >>> parametrization.params_to_reals1d(4)
    DeviceArray([0.54132485], dtype=float32)
    >>> parametrization.reals1d_to_params(0.54132485)
    DeviceArray(4., dtype=float32)

    An example for the parametrization of a 3×3 matrix of values in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[4.9,4.7,4.5],[3.5,3.6,3.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    DeviceArray([-2.2521696 , -1.050225  , -0.43275213,  1.2475176 ,
                  1.1168451 ,  0.981815  ,  1.9693712 ,  2.9489307 ,
                  2.8434052 ], dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[4.9, 4.7, 4.5],
                 [3.5, 3.6, 3.7],
                 [2.9, 2. , 2.1]], dtype=float32)
    """


@_jax_class_decorator
class RealNegative(_common.RealNegative):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar negative value:

    >>> parametrization = RealNegative()
    >>> parametrization.params_to_reals1d(-0.5)
    DeviceArray([-0.43275213], dtype=float32)
    >>> parametrization.reals1d_to_params(-0.43275213)
    DeviceArray(-0.49999997, dtype=float32)

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealNegative(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[-0.1,-0.2,-0.3],[-1.5,-1.6,-1.7],[-2.9,-2,-2.1]]))
    >>> one_dim_vec
    DeviceArray([-2.2521687, -1.5077717, -1.0502257,  1.2475176,  1.374483 ,
                  1.4982711,  2.8434052,  1.8545866,  1.9693712],            dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[-0.09999998, -0.20000002, -0.29999995],
                 [-1.5       , -1.6       , -1.7       ],
                 [-2.9       , -2.        , -2.1       ]], dtype=float32)
    """


@_jax_class_decorator
class RealBounded(_common.RealBounded):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1)
    >>> parametrization.params_to_reals1d(0.5)
    DeviceArray([1.0986123], dtype=float32, weak_type=True)
    >>> parametrization.reals1d_to_params(1.0986123)
    DeviceArray(0.5, dtype=float32, weak_type=True)

    An example for the parametrization of a 3×3 matrix of values in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[-0.1,-0.2,0.3],[-0.5,0.6,-0.7],[0.9,0,-0.1]]))
    >>> one_dim_vec
    DeviceArray([-0.20067069, -0.40546513,  0.61903924, -1.0986123 ,
                  1.3862944 , -1.734601  ,  2.9444387 ,  0.        ,
                 -0.20067069], dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[-0.09999999, -0.19999999,  0.29999998],
                 [-0.5       ,  0.6       , -0.7       ],
                 [ 0.8999999 ,  0.        , -0.09999999]], dtype=float32)
    """


@_jax_class_decorator
class RealBounded01(_common.RealBounded01):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (0,1):

    >>> parametrization = RealBounded01()
    >>> parametrization.params_to_reals1d(0.2)
    DeviceArray([-1.3862944], dtype=float32, weak_type=True)
    >>> parametrization.reals1d_to_params(-1.3862944)
    DeviceArray(0.2, dtype=float32, weak_type=True)

    An example for the parametrization of a matrix of values in (0,1):

    >>> parametrization = RealBounded01(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     jnp.array([[0.1,0.2,0.3],[0.5,0.6,0.7],[0.9,0.4,0.1]]))
    >>> one_dim_vec
    DeviceArray([-2.1972246 , -1.3862944 , -0.84729785,  0.        ,
                  0.4054652 ,  0.84729785,  2.1972244 , -0.40546507,
                 -2.1972246 ], dtype=float32)
    >>> parametrization.reals1d_to_params(one_dim_vec)
    DeviceArray([[0.09999999, 0.2       , 0.29999998],
                 [0.5       , 0.6       , 0.7       ],
                 [0.9       , 0.4       , 0.09999999]], dtype=float32)
    """


@_jax_class_decorator
class VectorSimplex(_common.VectorSimplex):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional simplex (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSimplex(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> vsimplex = parametrization.reals1d_to_params(vreals)
    >>> vsimplex
    DeviceArray([0.5078521 , 0.23692214, 0.09635811, 0.15886763], dtype=float32)
    >>> vsimplex.sum()
    DeviceArray(1., dtype=float32)
    >>> parametrization.params_to_reals1d(vsimplex)
    DeviceArray([ 1.9999998,  1.       , -0.4999996], dtype=float32)

    An example for the parametrization of a (2,) array of 3-dimentional
    simplex (we obtain a (2,4) array where each row is in the 3-dimentional simplex):

    >>> parametrization = VectorSimplex(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> msimplex = parametrization.reals1d_to_params(vreals)
    >>> msimplex
    DeviceArray([[0.5078521 , 0.23692214, 0.09635811, 0.15886763],
                 [0.09915365, 0.5898222 , 0.30543002, 0.00559415]],            dtype=float32)
    >>> msimplex.sum(axis=-1)
    DeviceArray([1., 1.], dtype=float32)
    >>> parametrization.params_to_reals1d(msimplex)
    DeviceArray([ 1.9999998,  1.       , -0.4999996, -1.       ,  2.0000005,
                  4.       ], dtype=float32)
    """


@_jax_class_decorator
class VectorSphere(_common.VectorSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-sphere (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSphere(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> vsphere = parametrization.reals1d_to_params(vreals)
    >>> vsphere
    DeviceArray([ 0.61241776,  0.33762082, -0.49731594,  0.51345265], dtype=float32)
    >>> (vsphere**2).sum()
    DeviceArray(1., dtype=float32)
    >>> parametrization.params_to_reals1d(vsphere)
    DeviceArray([ 1.9999998,  0.9999999, -0.5      ], dtype=float32)

    An example for the parametrization of a (2,) array of 3-dimentional
    sphere (we obtain a (2,4) array where each row is in the 3-dimentional
    sphere):

    >>> parametrization = VectorSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> msphere = parametrization.reals1d_to_params(vreals)
    >>> msphere
    DeviceArray([[ 0.61241776,  0.33762082, -0.49731594,  0.51345265],
                 [-0.33866856,  0.68663585,  0.07254504, -0.63919646]],            dtype=float32)
    >>> (msphere**2).sum(axis=-1)
    DeviceArray([1., 1.], dtype=float32)
    >>> parametrization.params_to_reals1d(msphere)
    DeviceArray([ 1.9999998,  0.9999999, -0.5      , -0.9999999,  1.9999999,
                  4.       ], dtype=float32)
    """


@_jax_class_decorator
class VectorHalfSphere(_common.VectorHalfSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-half-sphere
    (subspace of :math:`\mathbb R^4`:

    >>> parametrization = VectorHalfSphere(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> vhsphere = parametrization.reals1d_to_params(vreals)
    >>> vhsphere
    DeviceArray([ 0.61241776,  0.33762082, -0.26826707,  0.66256285], dtype=float32)
    >>> (vhsphere**2).sum()
    DeviceArray(1., dtype=float32)
    >>> vhsphere[-1] > 0
    DeviceArray(True, dtype=bool)
    >>> parametrization.params_to_reals1d(vhsphere)
    DeviceArray([ 1.9999998,  0.9999999, -0.5      ], dtype=float32)

    An example for the parametrization of a (2,) array of 3-dimentional
    unit-half-sphere (we obtain a (2,4) array where each row is in the
    3-dimentional unif-half-sphere):

    >>> parametrization = VectorHalfSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> mhsphere = parametrization.reals1d_to_params(vreals)
    >>> mhsphere
    DeviceArray([[ 0.61241776,  0.33762082, -0.26826707,  0.66256285],
                 [-0.33866856,  0.68663585,  0.6422733 ,  0.0363305 ]],            dtype=float32)
    >>> (mhsphere**2).sum(axis=-1)
    DeviceArray([1.       , 1.0000001], dtype=float32)
    >>> mhsphere[:,-1] > 0
    DeviceArray([ True,  True], dtype=bool)
    >>> parametrization.params_to_reals1d(mhsphere)
    DeviceArray([ 1.9999998,  0.9999999, -0.5      , -0.9999999,  1.9999998,
                  4.       ], dtype=float32)
    """


@_jax_class_decorator
class VectorBall(_common.VectorBall):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-ball (subspace
    of :math:`\mathbb R^3`:

    >>> parametrization = VectorBall(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> vball = parametrization.reals1d_to_params(vreals)
    >>> vball
    DeviceArray([ 0.6323942 ,  0.33042613, -0.16732505], dtype=float32)
    >>> (vball**2).sum()
    DeviceArray(0.5371015, dtype=float32)
    >>> parametrization.params_to_reals1d(vball)
    DeviceArray([ 2.        ,  1.0000004 , -0.50000006], dtype=float32)

    An example for the parametrization of a (2,) array of 3-dimentional
    ball (we obtain a (2,4) array where each row is in the 3-dimentional
    ball):

    >>> parametrization = VectorBall(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> mball = parametrization.reals1d_to_params(vreals)
    >>> mball
    DeviceArray([[ 0.6323942 ,  0.33042613, -0.16732505],
                 [-0.2392933 ,  0.4579774 ,  0.81467664]], dtype=float32)
    >>> (mball**2).sum(axis=-1)
    DeviceArray([0.5371015, 0.9307026], dtype=float32)
    >>> parametrization.params_to_reals1d(mball)
    DeviceArray([ 2.        ,  1.0000004 , -0.50000006, -1.0000004 ,
                  2.0000005 ,  4.        ], dtype=float32)
    """


@_jax_class_decorator
class MatrixDiag(_common.MatrixDiag):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal matrices:

    >>> parametrization = MatrixDiag(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    DeviceArray([[ 2. ,  0. ,  0. ],
                 [ 0. ,  1. ,  0. ],
                 [ 0. ,  0. , -0.5]], dtype=float32)
    >>> parametrization.params_to_reals1d(mat)
    DeviceArray([ 2. ,  1. , -0.5], dtype=float32)

    An example for the parametrization of a (2,) array of 3×3 diagonal
    matrices (we obtain a (2,3,3) array where each row is a 3×3 diagonal
    matrix):

    >>> parametrization = MatrixDiag(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    DeviceArray([[[ 2. ,  0. ,  0. ],
                  [ 0. ,  1. ,  0. ],
                  [ 0. ,  0. , -0.5]],
                ﻿
                 [[-1. ,  0. ,  0. ],
                  [ 0. ,  2. ,  0. ],
                  [ 0. ,  0. ,  4. ]]], dtype=float32)

    >>> parametrization.params_to_reals1d(nmat)
    DeviceArray([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ], dtype=float32)
    """


@_jax_class_decorator
class MatrixDiagPosDef(_common.MatrixDiagPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal positive definite
    matrices:

    >>> parametrization = MatrixDiagPosDef(dim=3)
    >>> vreals = jnp.array([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    DeviceArray([[2.126928 , 0.       , 0.       ],
                 [0.       , 1.3132617, 0.       ],
                 [0.       , 0.       , 0.474077 ]], dtype=float32)
    >>> parametrization.params_to_reals1d(mat)
    DeviceArray([ 2.        ,  1.0000001 , -0.49999988], dtype=float32)

    An example for the parametrization of a (2,) array of 3×3 diagonal
    positive definite matrices (we obtain a (2,3,3) array where each row is
    a 3×3 diagonal positive definite matrix):

    >>> parametrization = MatrixDiagPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    DeviceArray([[[2.126928 , 0.       , 0.       ],
                  [0.       , 1.3132617, 0.       ],
                  [0.       , 0.       , 0.474077 ]],
                ﻿
                 [[0.3132617, 0.       , 0.       ],
                  [0.       , 2.126928 , 0.       ],
                  [0.       , 0.       , 4.01815  ]]], dtype=float32)
    >>> parametrization.params_to_reals1d(nmat)
    DeviceArray([ 2.        ,  1.0000001 , -0.49999988, -1.        ,
                  2.        ,  4.        ], dtype=float32)
    """


@_jax_class_decorator
class MatrixSym(_common.MatrixSym):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric
    matrix:

    >>> parametrization = MatrixSym(dim=3)
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    DeviceArray([[ 2. , -1. ,  0.5],
                 [-1. , -2. , -0.5],
                 [ 0.5, -0.5,  1.5]], dtype=float32)
    >>> parametrization.params_to_reals1d(mat)
    DeviceArray([ 2. , -1. , -2. ,  0.5, -0.5,  1.5], dtype=float32)

    An example for the parametrization of a (2,) array of 3×3 symetric (we
    obtain a (2,3,3) array where each row is a 3×3 symmetric matrix):

    >>> parametrization = MatrixSym(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = jnp.array(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    DeviceArray([[[ 2. , -1. ,  0.5],
                  [-1. , -2. , -0.5],
                  [ 0.5, -0.5,  1.5]],
                ﻿
                 [[-3. , -0.5,  2.5],
                  [-0.5,  3. , -1.5],
                  [ 2.5, -1.5,  0.5]]], dtype=float32)
    >>> parametrization.params_to_reals1d(nmat)
    DeviceArray([ 2. , -1. , -2. ,  0.5, -0.5,  1.5, -3. , -0.5,  3. ,  2.5,
                 -1.5,  0.5], dtype=float32)
    """


@_jax_class_decorator
class MatrixSymPosDef(_common.MatrixSymPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric positive definite
    matrix:

    >>> parametrization = MatrixSymPosDef(dim=3)
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    DeviceArray([[ 4.5238233 ,  0.7519826 , -0.61399126],
                 [ 0.7519826 ,  0.17406644,  0.08977074],
                 [-0.61399126,  0.08977074,  0.8387036 ]], dtype=float32)
    >>> (jnp.linalg.eigh(mat)[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> parametrization.params_to_reals1d(mat)
    DeviceArray([ 2.        , -1.        , -1.9999863 ,  0.49999997,
                 -0.49999997,  1.4999999 ], dtype=float32)

    An example for the parametrization of a (2,) array of 3×3 symetric
    positive definite (we obtain a (2,3,3) array where each row is a 3×3
    symmetric positive definite matrix):

    >>> parametrization = MatrixSymPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = jnp.array(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    DeviceArray([[[ 4.5238233e+00,  7.5198263e-01, -6.1399126e-01],
                  [ 7.5198263e-01,  1.7406644e-01,  8.9770742e-02],
                  [-6.1399126e-01,  8.9770742e-02,  8.3870357e-01]],
                ﻿
                 [[ 2.3607307e-03,  8.5891113e-02, -4.2077880e-02],
                  [ 8.5891113e-02,  3.2373745e+00, -1.4341606e+00],
                  [-4.2077880e-02, -1.4341606e+00,  3.9312947e+00]]],            dtype=float32)
    >>> (jnp.linalg.eigh(nmat[0])[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> (jnp.linalg.eigh(nmat[1])[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> parametrization.params_to_reals1d(nmat)
    DeviceArray([ 2.        , -1.        , -1.9999863 ,  0.49999997,
                 -0.49999997,  1.4999999 , -3.        , -0.49999714,
                  3.0000002 ,  2.4999998 , -1.5       ,  0.49999806],            dtype=float32)
    """


@_jax_class_decorator
class MatrixCorrelation(_common.MatrixCorrelation):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 correlation matrix:

    >>> parametrization = MatrixCorrelation(dim=3)
    >>> parametrization.size
    3
    >>> vreals = jnp.array([2, -1, -1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    DeviceArray([[ 1.        ,  0.9306954 , -0.42707926],
                 [ 0.9306954 ,  1.        , -0.67538965],
                 [-0.42707926, -0.67538965,  1.0000001 ]], dtype=float32)
    >>> (jnp.linalg.eigh(mat)[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> parametrization.params_to_reals1d(mat)
    DeviceArray([ 1.9999998 , -0.99999976, -1.5000004 ], dtype=float32)

    An example for the parametrization of a (2,) array of 3×3 correlation matrix
    (we obtain a (2,3,3) array where each row is a 3×3 correlation matrix):

    >>> parametrization = MatrixCorrelation(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = jnp.array([2, -1, -1.5, 0.5, -0.5, 1.5])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    DeviceArray([[[ 1.        ,  0.9306954 , -0.42707926],
                  [ 0.9306954 ,  1.        , -0.67538965],
                  [-0.42707926, -0.67538965,  1.0000001 ]],
                ﻿
                 [[ 1.        ,  0.37529716, -0.22326566],
                  [ 0.37529716,  1.        ,  0.67535436],
                  [-0.22326566,  0.67535436,  1.        ]]], dtype=float32)
    >>> (jnp.linalg.eigh(nmat[0])[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> (jnp.linalg.eigh(nmat[1])[0] > 0).all()
    DeviceArray(True, dtype=bool)
    >>> parametrization.params_to_reals1d(nmat)
    DeviceArray([ 1.9999998 , -0.99999976, -1.5000004 ,  0.5       ,
                 -0.49999988,  1.4999998 ], dtype=float32)
    """


@_jax_class_decorator
class Tuple(_common.Tuple):
    _doc_examples = """
    Examples
    --------
    Let the parameter theta = (s, X, M) where s a real positive, X an
    unconstrained 2×3 matrix and M a 3×3 symmetric positive
    definite matrix. We can define the parametrization as:

    >>> parametrization = Tuple(
    ...     RealPositive(),
    ...     Real(shape=(2,3)),
    ...     MatrixSymPosDef(dim=3),
    ... )
    >>> parametrization.size
    13
    >>> vreals = jnp.linspace(-3, 3, 13)
    >>> vreals
    DeviceArray([-3.        , -2.5       , -2.        , -1.5       ,
                 -0.9999999 , -0.49999994,  0.        ,  0.5000001 ,
                  1.        ,  1.5       ,  2.        ,  2.5       ,
                  3.        ], dtype=float32)
    >>> s, X, M = parametrization.reals1d_to_params(vreals)
    >>> s
    DeviceArray(0.04858735, dtype=float32)
    >>> X
    DeviceArray([[-2.5       , -2.        , -1.5       ],
                 [-0.9999999 , -0.49999994,  0.        ]], dtype=float32)
    >>> M
    DeviceArray([[0.9488262, 1.377553 , 1.4059591],
                 [1.377553 , 2.862328 , 3.649652 ],
                 [1.4059591, 3.649652 , 6.048269 ]], dtype=float32)
    >>> parametrization.params_to_reals1d(s, X, M)
    DeviceArray([-3.        , -2.5       , -2.        , -1.5       ,
                 -0.9999999 , -0.49999994,  0.        ,  0.50000024,
                  1.0000002 ,  1.5       ,  1.9999998 ,  2.4999998 ,
                  3.        ], dtype=float32)

    The 1-D unconstrained vector is splitted for elementary parametrizations. We
    can recover the split used by the parametrization:

    >>> parametrization.size
    13
    >>> parametrization.idx_params
    (slice(0, 1, None), slice(1, 7, None), slice(7, 13, None))

    We can access to elementary parametrization using `[]` (getitem):

    >>> parametrization[2]
    MatrixSymPosDef(dim=3)

    We can obtain exacly the same result by applying the elementary
    reparametrization:

    >>> M1 = parametrization.reals1d_to_params(vreals)[2]
    >>> M2 = parametrization[2].reals1d_to_params(
    ...         vreals[parametrization.idx_params[2]])
    >>> (M1 == M2).all()
    DeviceArray(True, dtype=bool)
    """


@_jax_class_decorator
class NamedTuple(_common.NamedTuple):
    _doc_examples = """
    Examples
    --------
    Let the parameter theta = (s, X, M) where s a real positive, X an
    unconstrained 2×3 matrix and M a 3×3 symmetric positive
    definite matrix. We can define the parametrization as:

    >>> parametrization = NamedTuple(
    ...     s=RealPositive(),
    ...     X=Real(shape=(2,3)),
    ...     M=MatrixSymPosDef(dim=3),
    ... )
    >>> parametrization.size
    13
    >>> vreals = jnp.linspace(-3, 3, 13)
    >>> vreals
    DeviceArray([-3.        , -2.5       , -2.        , -1.5       ,
                 -0.9999999 , -0.49999994,  0.        ,  0.5000001 ,
                  1.        ,  1.5       ,  2.        ,  2.5       ,
                  3.        ], dtype=float32)
    >>> my_params = parametrization.reals1d_to_params(vreals)
    >>> my_params.s
    0.04858735157374206
    DeviceArray(0.04858735, dtype=float32)
    >>> my_params.X
    DeviceArray([[-2.5       , -2.        , -1.5       ],
                 [-0.9999999 , -0.49999994,  0.        ]], dtype=float32)
    >>> my_params.M
    DeviceArray([[0.9488262, 1.377553 , 1.4059591],
                 [1.377553 , 2.862328 , 3.649652 ],
                 [1.4059591, 3.649652 , 6.048269 ]], dtype=float32)
    >>> parametrization.params_to_reals1d(my_params)
    DeviceArray([-3.        , -2.5       , -2.        , -1.5       ,
                 -0.9999999 , -0.49999994,  0.        ,  0.50000024,
                  1.0000002 ,  1.5       ,  1.9999998 ,  2.4999998 ,
                  3.        ], dtype=float32)
    >>> parametrization.params_to_reals1d(s=my_params.s, X=my_params.X, M=my_params.M)
    DeviceArray([-3.        , -2.5       , -2.        , -1.5       ,
                 -0.9999999 , -0.49999994,  0.        ,  0.50000024,
                  1.0000002 ,  1.5       ,  1.9999998 ,  2.4999998 ,
                  3.        ], dtype=float32)

    The 1-D unconstrained vector is splitted for elementary parametrizations. We
    can recover the split used by the parametrization:

    >>> parametrization.size
    13
    >>> parametrization.idx_params
    Parameters(s=slice(0, 1, None), X=slice(1, 7, None), M=slice(7, 13, None))
    >>> parametrization.idx_params.M
    slice(7, 13, None)

    We can access to elementary parametrization using `[]` (getitem):

    >>> parametrization['M']
    MatrixSymPosDef(dim=3)

    We can obtain exacly the same result by applying the elementary
    reparametrization:

    >>> M1 = parametrization.reals1d_to_params(vreals).M
    >>> M2 = parametrization['M'].reals1d_to_params(
    ...         vreals[parametrization.idx_params.M])
    >>> (M1 == M2).all()
    DeviceArray(True, dtype=bool)
    """
