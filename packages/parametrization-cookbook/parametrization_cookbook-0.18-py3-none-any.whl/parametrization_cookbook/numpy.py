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

from .functions import numpy as _np_funs
from . import _common

_np_class_decorator = _common.custom_class_decorator(
    backend=_np_funs,
)


@_np_class_decorator
class Param(_common.Param):
    pass


@_np_class_decorator
class Real(_common.Real):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value:

    >>> parametrization = Real()
    >>> parametrization.params_to_reals1d(0.5)
    array([0.5])
    >>> parametrization.reals1d_to_params(0.5)
    0.5

    An example for the parametrization of a 3×3 matrix:

    >>> parametrization = Real(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[0,1,2],[3,4,5],[6,7,8]]))
    >>> one_dim_vec
    array([0., 1., 2., 3., 4., 5., 6., 7., 8.])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[0., 1., 2.],
           [3., 4., 5.],
           [6., 7., 8.]])
    """


@_np_class_decorator
class RealLowerBounded(_common.RealLowerBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5)
    >>> parametrization.params_to_reals1d(7)
    array([1.85458654])
    >>> parametrization.reals1d_to_params(1.85458654)
    6.999999998157278

    An example for the parametrization of a 3×3 matrix of values in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[5.1,5.2,5.3],[5.5,5.6,5.7],[5.9,6,6.1]]))
    >>> one_dim_vec
    array([-2.25216846, -1.5077718 , -1.05022561, -0.43275213, -0.19587037,
            0.013659  ,  0.37816456,  0.54132485,  0.69522803])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[5.1, 5.2, 5.3],
           [5.5, 5.6, 5.7],
           [5.9, 6. , 6.1]])
    """


@_np_class_decorator
class RealPositive(_common.RealPositive):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar positive value:

    >>> parametrization = RealPositive()
    >>> parametrization.params_to_reals1d(0.5)
    array([-0.43275213])
    >>> parametrization.reals1d_to_params(-0.43275213)
    0.49999999982970195

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealPositive(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[0.1,0.2,0.3],[1.5,1.6,1.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    array([-2.25216846, -1.5077718 , -1.05022561,  1.24751754,  1.37448299,
            1.4982711 ,  2.84340508,  1.85458654,  1.96937133])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[0.1, 0.2, 0.3],
           [1.5, 1.6, 1.7],
           [2.9, 2. , 2.1]])
    """


@_np_class_decorator
class RealUpperBounded(_common.RealUpperBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5)
    >>> parametrization.params_to_reals1d(4)
    array([0.54132485])
    >>> parametrization.reals1d_to_params(0.54132485)
    4.00000000291592

    An example for the parametrization of a 3×3 matrix of values in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[4.9,4.7,4.5],[3.5,3.6,3.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    array(-2.25216846, -1.05022561, -0.43275213,  1.24751754,  1.11684505,
           0.98181502,  1.96937133,  2.94893082,  2.84340508])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[4.9, 4.7, 4.5],
           [3.5, 3.6, 3.7],
           [2.9, 2. , 2.1]])
    """


@_np_class_decorator
class RealNegative(_common.RealNegative):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar negative value:

    >>> parametrization = RealNegative()
    >>> parametrization.params_to_reals1d(-0.5)
    array([-0.43275213])
    >>> parametrization.reals1d_to_params(-0.43275213)
    -0.49999999982970195

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealNegative(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[-0.1,-0.2,-0.3],[-1.5,-1.6,-1.7],[-2.9,-2,-2.1]]))
    >>> one_dim_vec
    array([-2.25216846, -1.5077718 , -1.05022561,  1.24751754,  1.37448299,
            1.4982711 ,  2.84340508,  1.85458654,  1.96937133])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[-0.1, -0.2, -0.3],
           [-1.5, -1.6, -1.7],
           [-2.9, -2. , -2.1]])
    """


@_np_class_decorator
class RealBounded(_common.RealBounded):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1)
    >>> parametrization.params_to_reals1d(0.5)
    array([1.09861229])
    >>> parametrization.reals1d_to_params(1.09861229)
    0.5000000004994588

    An example for the parametrization of a 3×3 matrix of values in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[-0.1,-0.2,0.3],[-0.5,0.6,-0.7],[0.9,0,-0.1]]))
    >>> one_dim_vec
    array([-0.2006707 , -0.40546511,  0.61903921, -1.09861229,  1.38629436,
           -1.73460106,  2.94443898,  0.        , -0.2006707 ])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[-0.1, -0.2,  0.3],
           [-0.5,  0.6, -0.7],
           [ 0.9,  0. , -0.1]])
    """


@_np_class_decorator
class RealBounded01(_common.RealBounded01):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (0,1):

    >>> parametrization = RealBounded01()
    >>> parametrization.params_to_reals1d(0.2)
    array([-1.38629436])
    >>> parametrization.reals1d_to_params(-1.38629436)
    0.20000000017918249

    An example for the parametrization of a matrix of values in (0,1):

    >>> parametrization = RealBounded01(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     np.array([[0.1,0.2,0.3],[0.5,0.6,0.7],[0.9,0.4,0.1]]))
    >>> one_dim_vec
    array([-2.19722458, -1.38629436, -0.84729786,  0.        ,  0.40546511,
            0.84729786,  2.19722458, -0.40546511, -2.19722458])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    array([[0.1, 0.2, 0.3],
           [0.5, 0.6, 0.7],
           [0.9, 0.4, 0.1]])
    """


@_np_class_decorator
class VectorSimplex(_common.VectorSimplex):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional simplex (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSimplex(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> vsimplex = parametrization.reals1d_to_params(vreals)
    >>> vsimplex
    array([0.5078521 , 0.23692215, 0.0963581 , 0.15886765])
    >>> vsimplex.sum()
    1.0
    >>> parametrization.params_to_reals1d(vsimplex)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3-dimentional
    simplex (we obtain a (2,4) array where each row is in the 3-dimentional simplex):

    >>> parametrization = VectorSimplex(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> msimplex = parametrization.reals1d_to_params(vreals)
    >>> msimplex
    array([[0.5078521 , 0.23692215, 0.0963581 , 0.15886765],
           [0.09915364, 0.58982216, 0.30543005, 0.00559415]])
    >>> msimplex.sum(axis=-1)
    array([1., 1.])
    >>> parametrization.params_to_reals1d(msimplex)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class VectorSphere(_common.VectorSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-sphere (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSphere(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> vsphere = parametrization.reals1d_to_params(vreals)
    >>> vsphere
    array([ 0.61241777,  0.33762081, -0.49731586,  0.51345262])
    >>> (vsphere**2).sum()
    1.0
    >>> parametrization.params_to_reals1d(vsphere)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3-dimentional
    sphere (we obtain a (2,4) array where each row is in the 3-dimentional
    sphere):

    >>> parametrization = VectorSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> msphere = parametrization.reals1d_to_params(vreals)
    >>> msphere
    array([[ 0.61241777,  0.33762081, -0.49731586,  0.51345262],
           [-0.33866857,  0.68663584,  0.07254512, -0.6391964 ]])
    >>> (msphere**2).sum(axis=-1)
    array([1., 1.])
    >>> parametrization.params_to_reals1d(msphere)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class VectorHalfSphere(_common.VectorHalfSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-half-sphere
    (subspace of :math:`\mathbb R^4`:

    >>> parametrization = VectorHalfSphere(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> vhsphere = parametrization.reals1d_to_params(vreals)
    >>> vhsphere
    array([ 0.61241777,  0.33762081, -0.26826703,  0.6625628 ])
    >>> (vhsphere**2).sum()
    0.9999999999999999
    >>> vhsphere[-1] > 0
    True
    >>> parametrization.params_to_reals1d(vhsphere)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3-dimentional
    unit-half-sphere (we obtain a (2,4) array where each row is in the
    3-dimentional unif-half-sphere):

    >>> parametrization = VectorHalfSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> mhsphere = parametrization.reals1d_to_params(vreals)
    >>> mhsphere
    array([[ 0.61241777,  0.33762081, -0.26826703,  0.6625628 ],
           [-0.33866857,  0.68663584,  0.64227324,  0.03633055]])
    >>> (mhsphere**2).sum(axis=-1)
    array([1., 1.])
    >>> mhsphere[:,-1] > 0
    array([ True,  True])
    >>> parametrization.params_to_reals1d(mhsphere)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class VectorBall(_common.VectorBall):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-ball (subspace
    of :math:`\mathbb R^3`:

    >>> parametrization = VectorBall(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> vball = parametrization.reals1d_to_params(vreals)
    >>> vball
    array([ 0.6323941 ,  0.33042605, -0.16732504])
    >>> (vball**2).sum()
    0.5371013399369556
    >>> parametrization.params_to_reals1d(vball)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3-dimentional
    ball (we obtain a (2,4) array where each row is in the 3-dimentional
    ball):

    >>> parametrization = VectorBall(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> mball = parametrization.reals1d_to_params(vreals)
    >>> mball
    array([[ 0.6323941 ,  0.33042605, -0.16732504],
           [-0.23929328,  0.45797738,  0.81467661]])
    >>> (mball**2).sum(axis=-1)
    array([0.53710134, 0.93070253])
    >>> parametrization.params_to_reals1d(mball)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class MatrixDiag(_common.MatrixDiag):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal matrices:

    >>> parametrization = MatrixDiag(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    array([[ 2. ,  0. ,  0. ],
           [ 0. ,  1. ,  0. ],
           [ 0. ,  0. , -0.5]])
    >>> parametrization.params_to_reals1d(mat)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3×3 diagonal
    matrices (we obtain a (2,3,3) array where each row is a 3×3 diagonal
    matrix):

    >>> parametrization = MatrixDiag(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    array([[[ 2. ,  0. ,  0. ],
            [ 0. ,  1. ,  0. ],
            [ 0. ,  0. , -0.5]],
          ﻿
           [[-1. ,  0. ,  0. ],
            [ 0. ,  2. ,  0. ],
            [ 0. ,  0. ,  4. ]]])
    >>> parametrization.params_to_reals1d(nmat)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class MatrixDiagPosDef(_common.MatrixDiagPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal positive definite
    matrices:

    >>> parametrization = MatrixDiagPosDef(dim=3)
    >>> vreals = np.array([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    array([[2.12692801, 0.        , 0.        ],
           [0.        , 1.31326169, 0.        ],
           [0.        , 0.        , 0.47407698]])
    >>> parametrization.params_to_reals1d(mat)
    array([ 2. ,  1. , -0.5])

    An example for the parametrization of a (2,) array of 3×3 diagonal
    positive definite matrices (we obtain a (2,3,3) array where each row is
    a 3×3 diagonal positive definite matrix):

    >>> parametrization = MatrixDiagPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    array([[[2.12692801, 0.        , 0.        ],
            [0.        , 1.31326169, 0.        ],
            [0.        , 0.        , 0.47407698]],
          ﻿
           [[0.31326169, 0.        , 0.        ],
            [0.        , 2.12692801, 0.        ],
            [0.        , 0.        , 4.01814993]]])
    >>> parametrization.params_to_reals1d(nmat)
    array([ 2. ,  1. , -0.5, -1. ,  2. ,  4. ])
    """


@_np_class_decorator
class MatrixSym(_common.MatrixSym):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric
    matrix:

    >>> parametrization = MatrixSym(dim=3)
    >>> parametrization.size
    6
    >>> vreals = np.array([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    array([[ 2. , -1. ,  0.5],
           [-1. , -2. , -0.5],
           [ 0.5, -0.5,  1.5]])
    >>> parametrization.params_to_reals1d(mat)
    array([ 2. , -1. , -2. ,  0.5, -0.5,  1.5])

    An example for the parametrization of a (2,) array of 3×3 symetric (we
    obtain a (2,3,3) array where each row is a 3×3 symmetric matrix):

    >>> parametrization = MatrixSym(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = np.array(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    array([[[ 2. , -1. ,  0.5],
            [-1. , -2. , -0.5],
            [ 0.5, -0.5,  1.5]],
          ﻿
           [[-3. , -0.5,  2.5],
            [-0.5,  3. , -1.5],
            [ 2.5, -1.5,  0.5]]])
    >>> parametrization.params_to_reals1d(nmat)
    array([ 2. , -1. , -2. ,  0.5, -0.5,  1.5, -3. , -0.5,  3. ,  2.5, -1.5,
            0.5]))
    """


@_np_class_decorator
class MatrixSymPosDef(_common.MatrixSymPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric positive definite
    matrix:

    >>> parametrization = MatrixSymPosDef(dim=3)
    >>> parametrization.size
    6
    >>> vreals = np.array([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    array([[ 4.52382276,  0.75198261, -0.61399123],
           [ 0.75198261,  0.17406644,  0.08977075],
           [-0.61399123,  0.08977075,  0.83870357]])
    >>> (np.linalg.eigh(mat)[0] > 0).all()
    True
    >>> parametrization.params_to_reals1d(mat)
    array([ 2. , -1. , -2. ,  0.5, -0.5,  1.5])

    An example for the parametrization of a (2,) array of 3×3 symetric
    positive definite (we obtain a (2,3,3) array where each row is a 3×3
    symmetric positive definite matrix):

    >>> parametrization = MatrixSymPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = np.array(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    array([[[ 4.52382276e+00,  7.51982610e-01, -6.13991230e-01],
            [ 7.51982610e-01,  1.74066442e-01,  8.97707500e-02],
            [-6.13991230e-01,  8.97707500e-02,  8.38703573e-01]],
          ﻿
           [[ 2.36073073e-03,  8.58911144e-02, -4.20778808e-02],
            [ 8.58911144e-02,  3.23737449e+00, -1.43416053e+00],
            [-4.20778808e-02, -1.43416053e+00,  3.93129495e+00]]])
    >>> (np.linalg.eigh(nmat[0])[0] > 0).all()
    True
    >>> (np.linalg.eigh(nmat[1])[0] > 0).all()
    True
    >>> parametrization.params_to_reals1d(nmat)
    array([ 2. , -1. , -2. ,  0.5, -0.5,  1.5, -3. , -0.5,  3. ,  2.5, -1.5,
            0.5]))
    """


@_np_class_decorator
class MatrixCorrelation(_common.MatrixCorrelation):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 correlation matrix:

    >>> parametrization = MatrixCorrelation(dim=3)
    >>> parametrization.size
    3
    >>> vreals = np.array([2, -1, -1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    array([[ 1.        ,  0.93069539, -0.42707927],
           [ 0.93069539,  1.        , -0.67538964],
           [-0.42707927, -0.67538964,  1.        ]])
    >>> (np.linalg.eigh(mat)[0] > 0).all()
    True
    >>> parametrization.params_to_reals1d(mat)
    array([ 2. , -1. , -1.5])

    An example for the parametrization of a (2,) array of 3×3 correlation matrix
    (we obtain a (2,3,3) array where each row is a 3×3 correlation matrix):

    >>> parametrization = MatrixCorrelation(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = np.array([2, -1, -1.5, 0.5, -0.5, 1.5])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    array([[[ 1.        ,  0.93069539, -0.42707927],
            [ 0.93069539,  1.        , -0.67538964],
            [-0.42707927, -0.67538964,  1.        ]],
            ﻿
           [[ 1.        ,  0.37529715, -0.22326569],
            [ 0.37529715,  1.        ,  0.67535432],
            [-0.22326569,  0.67535432,  1.        ]]])
    >>> (np.linalg.eigh(nmat[0])[0] > 0).all()
    True
    >>> (np.linalg.eigh(nmat[1])[0] > 0).all()
    True
    >>> parametrization.params_to_reals1d(nmat)
    array([ 2. , -1. , -1.5,  0.5, -0.5,  1.5])
    """


@_np_class_decorator
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
    >>> vreals = np.linspace(-3, 3, 13)
    >>> vreals
    array([-3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,
            2.5,  3. ])
    >>> s, X, M = parametrization.reals1d_to_params(vreals)
    >>> s
    0.04858735157374206
    >>> X
    array([[-2.5, -2. , -1.5],
           [-1. , -0.5,  0. ]])
    >>> M
    array([[0.94882597, 1.37755288, 1.40595902],
           [1.37755288, 2.86232813, 3.64965197],
           [1.40595902, 3.64965197, 6.04826905]])
    >>> parametrization.params_to_reals1d(s, X, M)
    array([-3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,
            2.5,  3. ])

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
    True
    """


@_np_class_decorator
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
    >>> vreals = np.linspace(-3, 3, 13)
    >>> vreals
    array([-3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,
            2.5,  3. ])
    >>> my_params = parametrization.reals1d_to_params(vreals)
    >>> my_params.s
    0.04858735157374206
    >>> my_params.X
    array([[-2.5, -2. , -1.5],
           [-1. , -0.5,  0. ]])
    >>> my_params.M
    array([[0.94882597, 1.37755288, 1.40595902],
           [1.37755288, 2.86232813, 3.64965197],
           [1.40595902, 3.64965197, 6.04826905]])
    >>> parametrization.params_to_reals1d(my_params)
    array([-3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,
            2.5,  3. ])
    >>> parametrization.params_to_reals1d(s=my_params.s, X=my_params.X, M=my_params.M)
    array([-3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ,
            2.5,  3. ])

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
    True
    """
