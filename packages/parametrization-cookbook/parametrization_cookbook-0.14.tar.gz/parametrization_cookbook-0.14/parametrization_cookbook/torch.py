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

from .functions import torch as _torch_funs
from . import _common

import functools as _functools

_torch_class_decorator = _common.custom_class_decorator(
    backend=_torch_funs,
    method_notes="""Note
        ----
        This function is implemented using `torch` primitive. Gradients can
        be computed as usual with the torch `backward` method.

        """,
    array_like="tensor",
)


@_torch_class_decorator
class Param(_common.Param):
    pass


@_torch_class_decorator
class Real(_common.Real):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value:

    >>> parametrization = Real()
    >>> parametrization.params_to_reals1d(torch.tensor(0.5))
    tensor([0.5000])
    >>> parametrization.reals1d_to_params(torch.tensor(0.5))
    tensor(0.5000)

    An example for the parametrization of a 3×3 matrix:

    >>> parametrization = Real(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[0,1,2],[3,4,5],[6,7,8]]))
    >>> one_dim_vec
    tensor([0., 1., 2., 3., 4., 5., 6., 7., 8.])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[0., 1., 2.],
            [3., 4., 5.],
            [6., 7., 8.]])
    """


@_torch_class_decorator
class RealLowerBounded(_common.RealLowerBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5)
    >>> parametrization.params_to_reals1d(torch.tensor(7))
    tensor([1.8546])
    >>> parametrization.reals1d_to_params(torch.tensor(1.8546))
    tensor(7.0000)

    An example for the parametrization of a 3×3 matrix of values in (5, +∞):

    >>> parametrization = RealLowerBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[5.1,5.2,5.3],[5.5,5.6,5.7],[5.9,6,6.1]]))
    >>> one_dim_vec
    tensor([-2.2522, -1.5078, -1.0502, -0.4328, -0.1959,  0.0137,  0.3782,  0.5413,
             0.6952])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[5.1000, 5.2000, 5.3000],
            [5.5000, 5.6000, 5.7000],
            [5.9000, 6.0000, 6.1000]])
    """


@_torch_class_decorator
class RealPositive(_common.RealPositive):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar positive value:

    >>> parametrization = RealPositive()
    >>> parametrization.params_to_reals1d(torch.tensor(0.5))
    tensor([-0.4328])
    >>> parametrization.reals1d_to_params(torch.tensor(-0.4328))
    tensor(0.5000)

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealPositive(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[0.1,0.2,0.3],[1.5,1.6,1.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    tensor([-2.2522, -1.5078, -1.0502,  1.2475,  1.3745,  1.4983,  2.8434,  1.8546,
             1.9694])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[0.1000, 0.2000, 0.3000],
            [1.5000, 1.6000, 1.7000],
            [2.9000, 2.0000, 2.1000]])
    """


@_torch_class_decorator
class RealUpperBounded(_common.RealUpperBounded):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar value in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5)
    >>> parametrization.params_to_reals1d(torch.tensor(4))
    tensor([0.5413])
    >>> parametrization.reals1d_to_params(torch.tensor(0.5413))
    tensor(4.0000)

    An example for the parametrization of a 3×3 matrix of values in (-∞, 5):

    >>> parametrization = RealUpperBounded(bound=5, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[4.9,4.7,4.5],[3.5,3.6,3.7],[2.9,2,2.1]]))
    >>> one_dim_vec
    tensor([-2.2522, -1.0502, -0.4328,  1.2475,  1.1168,  0.9818,  1.9694,  2.9489,
             2.8434])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[4.9000, 4.7000, 4.5000],
            [3.5000, 3.6000, 3.7000],
            [2.9000, 2.0000, 2.1000]])
    """


@_torch_class_decorator
class RealNegative(_common.RealNegative):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a scalar negative value:

    >>> parametrization = RealNegative()
    >>> parametrization.params_to_reals1d(torch.tensor(-0.5))
    tensor([-0.4328])
    >>> parametrization.reals1d_to_params(torch.tensor(-0.4328))
    tensor(-0.5000)

    An example for the parametrization of a 3×3 matrix of negative values:

    >>> parametrization = RealNegative(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[-0.1,-0.2,-0.3],[-1.5,-1.6,-1.7],[-2.9,-2,-2.1]]))
    >>> one_dim_vec
    tensor([-2.2522, -1.5078, -1.0502,  1.2475,  1.3745,  1.4983,  2.8434,  1.8546,
             1.9694])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[-0.1000, -0.2000, -0.3000],
            [-1.5000, -1.6000, -1.7000],
            [-2.9000, -2.0000, -2.1000]])
    """


@_torch_class_decorator
class RealBounded(_common.RealBounded):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1)
    >>> parametrization.params_to_reals1d(torch.tensor(0.5))
    tensor([1.0986])
    >>> parametrization.reals1d_to_params(torch.tensor(1.0986))
    tensor(0.5000)

    An example for the parametrization of a 3×3 matrix of values in (-1,1):

    >>> parametrization = RealBounded(bound_lower=-1, bound_upper=1, shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[-0.1,-0.2,0.3],[-0.5,0.6,-0.7],[0.9,0,-0.1]]))
    >>> one_dim_vec
    tensor([-0.2007, -0.4055,  0.6190, -1.0986,  1.3863, -1.7346,  2.9444,  0.0000,
            -0.2007])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[-0.1000, -0.2000,  0.3000],
            [-0.5000,  0.6000, -0.7000],
            [ 0.9000,  0.0000, -0.1000]])
    """


@_torch_class_decorator
class RealBounded01(_common.RealBounded01):
    _doc_examples = """
    Examples
    --------
    An example for the parametrization of a scalar in (0,1):

    >>> parametrization = RealBounded01()
    >>> parametrization.params_to_reals1d(torch.tensor(0.2))
    tensor([-1.3863])
    >>> parametrization.reals1d_to_params(torch.tensor(-1.38629436))
    tensor(0.2000)

    An example for the parametrization of a matrix of values in (0,1):

    >>> parametrization = RealBounded01(shape=(3,3))
    >>> one_dim_vec = parametrization.params_to_reals1d(
    ...     torch.tensor([[0.1,0.2,0.3],[0.5,0.6,0.7],[0.9,0.4,0.1]]))
    >>> one_dim_vec
    tensor([-2.1972, -1.3863, -0.8473,  0.0000,  0.4055,  0.8473,  2.1972, -0.4055,
            -2.1972])
    >>> parametrization.reals1d_to_params(one_dim_vec)
    tensor([[0.1000, 0.2000, 0.3000],
            [0.5000, 0.6000, 0.7000],
            [0.9000, 0.4000, 0.1000]])
    """


@_torch_class_decorator
class VectorSimplex(_common.VectorSimplex):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional simplex (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSimplex(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> vsimplex = parametrization.reals1d_to_params(vreals)
    >>> vsimplex
    tensor([0.5079, 0.2369, 0.0964, 0.1589])
    >>> vsimplex.sum()
    tensor(1.)
    >>> parametrization.params_to_reals1d(vsimplex)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3-dimentional
    simplex (we obtain a (2,4) array where each row is in the 3-dimentional simplex):

    >>> parametrization = VectorSimplex(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> msimplex = parametrization.reals1d_to_params(vreals)
    >>> msimplex
    tensor([[0.5079, 0.2369, 0.0964, 0.1589],
            [0.0992, 0.5898, 0.3054, 0.0056]])
    >>> msimplex.sum(axis=-1)
    tensor([1., 1.])
    >>> parametrization.params_to_reals1d(msimplex)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class VectorSphere(_common.VectorSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-sphere (subspace
    of :math:`\mathbb R^4`:

    >>> parametrization = VectorSphere(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> vsphere = parametrization.reals1d_to_params(vreals)
    >>> vsphere
    tensor([ 0.6124,  0.3376, -0.4973,  0.5135])
    >>> (vsphere**2).sum()
    tensor(1.)
    >>> parametrization.params_to_reals1d(vsphere)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3-dimentional
    sphere (we obtain a (2,4) array where each row is in the 3-dimentional
    sphere):

    >>> parametrization = VectorSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> msphere = parametrization.reals1d_to_params(vreals)
    >>> msphere
    tensor([[ 0.6124,  0.3376, -0.4973,  0.5135],
            [-0.3387,  0.6866,  0.0725, -0.6392]])
    >>> (msphere**2).sum(axis=-1)
    tensor([1., 1.])
    >>> parametrization.params_to_reals1d(msphere)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class VectorHalfSphere(_common.VectorHalfSphere):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-half-sphere
    (subspace of :math:`\mathbb R^4`:

    >>> parametrization = VectorHalfSphere(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> vhsphere = parametrization.reals1d_to_params(vreals)
    >>> vhsphere
    tensor([ 0.6124,  0.3376, -0.2683,  0.6626])
    >>> (vhsphere**2).sum()
    tensor(1.)
    >>> vhsphere[-1] > 0
    tensor(True)
    >>> parametrization.params_to_reals1d(vhsphere)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3-dimentional
    unit-half-sphere (we obtain a (2,4) array where each row is in the
    3-dimentional unif-half-sphere):

    >>> parametrization = VectorHalfSphere(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> mhsphere = parametrization.reals1d_to_params(vreals)
    >>> mhsphere
    tensor([[ 0.6124,  0.3376, -0.2683,  0.6626],
            [-0.3387,  0.6866,  0.6423,  0.0363]])
    >>> (mhsphere**2).sum(axis=-1)
    tensor([1.0000, 1.0000])
    >>> mhsphere[:,-1] > 0
    tensor([True, True])
    >>> parametrization.params_to_reals1d(mhsphere)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class VectorBall(_common.VectorBall):
    _doc_examples = r"""
    Examples
    --------
    An example for a parametrization of a 3-dimensional unit-ball (subspace
    of :math:`\mathbb R^3`:

    >>> parametrization = VectorBall(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> vball = parametrization.reals1d_to_params(vreals)
    >>> vball
    tensor([ 0.6324,  0.3304, -0.1673])
    >>> (vball**2).sum()
    tensor(0.5371)
    >>> parametrization.params_to_reals1d(vball)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3-dimentional
    ball (we obtain a (2,4) array where each row is in the 3-dimentional
    ball):

    >>> parametrization = VectorBall(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> mball = parametrization.reals1d_to_params(vreals)
    >>> mball
    tensor([[ 0.6324,  0.3304, -0.1673],
            [-0.2393,  0.4580,  0.8147]])
    >>> (mball**2).sum(axis=-1)
    tensor([0.5371, 0.9307])
    >>> parametrization.params_to_reals1d(mball)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class MatrixDiag(_common.MatrixDiag):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal matrices:

    >>> parametrization = MatrixDiag(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    tensor([[ 2.0000,  0.0000,  0.0000],
            [ 0.0000,  1.0000,  0.0000],
            [ 0.0000,  0.0000, -0.5000]])
    >>> parametrization.params_to_reals1d(mat)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3×3 diagonal
    matrices (we obtain a (2,3,3) array where each row is a 3×3 diagonal
    matrix):

    >>> parametrization = MatrixDiag(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    tensor([[[ 2.0000,  0.0000,  0.0000],
             [ 0.0000,  1.0000,  0.0000],
             [ 0.0000,  0.0000, -0.5000]],
            ﻿
            [[-1.0000,  0.0000,  0.0000],
             [ 0.0000,  2.0000,  0.0000],
             [ 0.0000,  0.0000,  4.0000]]])
    >>> parametrization.params_to_reals1d(nmat)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class MatrixDiagPosDef(_common.MatrixDiagPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 diagonal positive definite
    matrices:

    >>> parametrization = MatrixDiagPosDef(dim=3)
    >>> vreals = torch.tensor([2, 1, -0.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    tensor([[2.1269, 0.0000, 0.0000],
            [0.0000, 1.3133, 0.0000],
            [0.0000, 0.0000, 0.4741]])
    >>> parametrization.params_to_reals1d(mat)
    tensor([ 2.0000,  1.0000, -0.5000])

    An example for the parametrization of a (2,) array of 3×3 diagonal
    positive definite matrices (we obtain a (2,3,3) array where each row is
    a 3×3 diagonal positive definite matrix):

    >>> parametrization = MatrixDiagPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, 1, -.5, -1, 2, 4])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    tensor([[[2.1269, 0.0000, 0.0000],
             [0.0000, 1.3133, 0.0000],
             [0.0000, 0.0000, 0.4741]],
            ﻿
            [[0.3133, 0.0000, 0.0000],
             [0.0000, 2.1269, 0.0000],
             [0.0000, 0.0000, 4.0181]]])
    >>> parametrization.params_to_reals1d(nmat)
    tensor([ 2.0000,  1.0000, -0.5000, -1.0000,  2.0000,  4.0000])
    """


@_torch_class_decorator
class MatrixSym(_common.MatrixSym):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric
    matrix:

    >>> parametrization = MatrixSym(dim=3)
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    tensor([[ 2.0000, -1.0000,  0.5000],
            [-1.0000, -2.0000, -0.5000],
            [ 0.5000, -0.5000,  1.5000]])
    >>> parametrization.params_to_reals1d(mat)
    tensor([ 2.0000, -1.0000, -2.0000,  0.5000, -0.5000,  1.5000])

    An example for the parametrization of a (2,) array of 3×3 symetric (we
    obtain a (2,3,3) array where each row is a 3×3 symmetric matrix):

    >>> parametrization = MatrixSym(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = torch.tensor(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    tensor([[[ 2.0000, -1.0000,  0.5000],
             [-1.0000, -2.0000, -0.5000],
             [ 0.5000, -0.5000,  1.5000]],
            ﻿
            [[-3.0000, -0.5000,  2.5000],
             [-0.5000,  3.0000, -1.5000],
             [ 2.5000, -1.5000,  0.5000]]])
    >>> parametrization.params_to_reals1d(nmat)
    tensor([ 2.0000, -1.0000, -2.0000,  0.5000, -0.5000,  1.5000, -3.0000, -0.5000,
             3.0000,  2.5000, -1.5000,  0.5000])
    """


@_torch_class_decorator
class MatrixSymPosDef(_common.MatrixSymPosDef):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 symmetric positive definite
    matrix:

    >>> parametrization = MatrixSymPosDef(dim=3)
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, -1, -2, 0.5, -0.5, 1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    tensor([[ 4.5238,  0.7520, -0.6140],
            [ 0.7520,  0.1741,  0.0898],
            [-0.6140,  0.0898,  0.8387]])
    >>> (torch.linalg.eigh(mat)[0] > 0).all()
    tensor(True)
    >>> parametrization.params_to_reals1d(mat)
    tensor([ 2.0000, -1.0000, -2.0000,  0.5000, -0.5000,  1.5000])

    An example for the parametrization of a (2,) array of 3×3 symetric
    positive definite (we obtain a (2,3,3) array where each row is a 3×3
    symmetric positive definite matrix):

    >>> parametrization = MatrixSymPosDef(dim=3, shape=(2,))
    >>> parametrization.size
    12
    >>> vreals = torch.tensor(
    ...     [2, -1, -2, 0.5, -0.5, 1.5, -3, -0.5, 3, 2.5, -1.5, 0.5]
    ... )
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    tensor([[[ 4.5238e+00,  7.5198e-01, -6.1399e-01],
             [ 7.5198e-01,  1.7407e-01,  8.9771e-02],
             [-6.1399e-01,  8.9771e-02,  8.3870e-01]],
            ﻿
            [[ 2.3607e-03,  8.5891e-02, -4.2078e-02],
             [ 8.5891e-02,  3.2374e+00, -1.4342e+00],
             [-4.2078e-02, -1.4342e+00,  3.9313e+00]]])
    >>> (torch.linalg.eigh(nmat[0])[0] > 0).all()
    tensor(True)
    >>> (torch.linalg.eigh(nmat[1])[0] > 0).all()
    tensor(True)
    >>> parametrization.params_to_reals1d(nmat)
    tensor([ 2.0000, -1.0000, -2.0000,  0.5000, -0.5000,  1.5000, -3.0000, -0.5000,
             3.0000,  2.5000, -1.5000,  0.5000])
    """


@_torch_class_decorator
class MatrixCorrelation(_common.MatrixCorrelation):
    _doc_examples = """
    Examples
    --------
    An example for a parametrization of a 3×3 correlation matrix:

    >>> parametrization = MatrixCorrelation(dim=3)
    >>> parametrization.size
    3
    >>> vreals = torch.tensor([2, -1, -1.5])
    >>> mat = parametrization.reals1d_to_params(vreals)
    >>> mat
    tensor([[ 1.0000,  0.9307, -0.4271],
            [ 0.9307,  1.0000, -0.6754],
            [-0.4271, -0.6754,  1.0000]])
    >>> (torch.linalg.eigh(mat)[0] > 0).all()
    tensor(True)
    >>> parametrization.params_to_reals1d(mat)
    tensor([ 2.0000, -1.0000, -1.5000])

    An example for the parametrization of a (2,) array of 3×3 correlation matrix
    (we obtain a (2,3,3) array where each row is a 3×3 correlation matrix):

    >>> parametrization = MatrixCorrelation(dim=3, shape=(2,))
    >>> parametrization.size
    6
    >>> vreals = torch.tensor([2, -1, -1.5, 0.5, -0.5, 1.5])
    >>> nmat = parametrization.reals1d_to_params(vreals)
    >>> nmat
    tensor([[[ 1.0000,  0.9307, -0.4271],
             [ 0.9307,  1.0000, -0.6754],
             [-0.4271, -0.6754,  1.0000]],
            ﻿
            [[ 1.0000,  0.3753, -0.2233],
             [ 0.3753,  1.0000,  0.6754],
             [-0.2233,  0.6754,  1.0000]]])
    >>> (torch.linalg.eigh(nmat[0])[0] > 0).all()
    tensor(True)
    >>> (torch.linalg.eigh(nmat[1])[0] > 0).all()
    tensor(True)
    >>> parametrization.params_to_reals1d(nmat)
    tensor([ 2.0000, -1.0000, -1.5000,  0.5000, -0.5000,  1.5000])
    """


@_torch_class_decorator
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
    >>> vreals = torch.linspace(-3, 3, 13)
    >>> vreals
    tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
             1.0000,  1.5000,  2.0000,  2.5000,  3.0000])
    >>> s, X, M = parametrization.reals1d_to_params(vreals)
    >>> s
    tensor(0.0486)
    >>> X
    tensor([[-2.5000, -2.0000, -1.5000],
            [-1.0000, -0.5000,  0.0000]])
    >>> M
    tensor([[0.9488, 1.3776, 1.4060],
            [1.3776, 2.8623, 3.6497],
            [1.4060, 3.6497, 6.0483]])
    >>> parametrization.params_to_reals1d(s, X, M)
    tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
             1.0000,  1.5000,  2.0000,  2.5000,  3.0000])

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
    tensor(True)
    """


@_torch_class_decorator
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
    >>> vreals = torch.linspace(-3, 3, 13)
    >>> vreals
    tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
             1.0000,  1.5000,  2.0000,  2.5000,  3.0000])
    >>> my_params = parametrization.reals1d_to_params(vreals)
    >>> my_params.s
    tensor(0.0486)
    >>> my_params.X
    tensor([[-2.5000, -2.0000, -1.5000],
            [-1.0000, -0.5000,  0.0000]])
    >>> my_params.M
    tensor([[0.9488, 1.3776, 1.4060],
            [1.3776, 2.8623, 3.6497],
            [1.4060, 3.6497, 6.0483]])
    >>> parametrization.params_to_reals1d(my_params)
    tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
             1.0000,  1.5000,  2.0000,  2.5000,  3.0000])
    >>> parametrization.params_to_reals1d(s=my_params.s, X=my_params.X, M=my_params.M)
    tensor([-3.0000, -2.5000, -2.0000, -1.5000, -1.0000, -0.5000,  0.0000,  0.5000,
             1.0000,  1.5000,  2.0000,  2.5000,  3.0000])

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
    tensor(True)
    """
