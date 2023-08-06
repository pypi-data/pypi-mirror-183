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

from ._doc_tools import decorate_with_doc


def _to_array(x):
    raise NotImplementedError


def _array_size(x):
    raise NotImplementedError


def _concatenate(*args, **kwargs):
    raise NotImplementedError


@decorate_with_doc(
    """
    Bijective function x ↦ log(1+exp(x))

    Implementation of function x ↦ log(1+exp(x)).
    """,
    reciprocal="logexpm1",
)
def log1pexp(x):
    raise NotImplementedError


@decorate_with_doc(
    """
    Bijective function x ↦ scale * log(1+exp(x))

    Implementation of function x ↦ scale * log(1+exp(x)).
    """,
    reciprocal="softplusinv",
    scale=True,
)
def softplus(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    """
    Bijective function x ↦ log(exp(x)-1)

    Implementation of function x ↦ log(exp(x)-1).
    """,
    reciprocal="log1pexp",
)
def logexpm1(x):
    raise NotImplementedError


@decorate_with_doc(
    """
    Bijective function x ↦ log(exp(x/scale)-1)

    Implementation of function x ↦ log(exp(x/scale)-1).
    """,
    reciprocal="softplus",
    scale=True,
)
def softplusinv(x, scale=1.0):
    raise NotImplementedError


def expit(x):
    raise NotImplementedError


def logit(x):
    raise NotImplementedError


def tanh(*args, **kwargs):
    raise NotImplementedError


def arctanh(*args, **kwargs):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to simplex element.

    The n-dimensional open unit-simplex is defined by: :math:`\mathcal S_n =
    \left\{{x\in\mathbb {{R_+^*}}^{{n+1}}: \sum_ix_i=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a vector of shape (n,), the output is a n-simplex element, i.e.
       a vector of shape (n+1,).
     - input is a nd-array of shape (..., n), the output is a nd-array of
       n-simplex elements with a total shape (..., n+1).
    """,
    reciprocal="simplex_to_reals",
    scale=False,
    input_shape="(..., n)",
    output_shape="(..., n+1)",
)
def reals_to_simplex(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform to simplex element vector of reals.

    The n-dimensional open unit-simplex is defined by: :math:`\mathcal S_n =
    \left\{{x\in\mathbb {{R_+^*}}^{{n+1}}: \sum_ix_i=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a n-simplex element (i.e. a vector of shape (n+1,)), the output
       is a vector of shape (n,).
     - input is a nd-array of n-simplex elements with a total shape (..., n+1),
       the output is a nd-array of shape (..., n).
    """,
    reciprocal="reals_to_simplex",
    scale=False,
    input_shape="(..., n+1)",
    output_shape="(..., n)",
)
def simplex_to_reals(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to sphere element.

    The n-dimensional unit sphere is defined by: :math:`\mathsf S_n =
    \left\{{x\in\mathbb R^{{n+1}}: \sum_ix_i^2=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a vector of shape (n,), the output is a n-sphere element, i.e.
       a vector of shape (n+1,).
     - input is a nd-array of shape (..., n), the output is a nd-array of
       n-sphere elements with a total shape (..., n+1).
    """,
    note="There is no bijective mapping between the whole shpere and uncontrained vector space. "
    "Some boundaries of the sphere are excluded.",
    reciprocal="sphere_to_reals",
    scale=False,
    input_shape="(..., n)",
    output_shape="(..., n+1)",
)
def reals_to_sphere(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform to sphere element vector of reals.

    The n-dimensional unit sphere is defined by: :math:`\mathsf S_n =
    \left\{{x\in\mathbb R^{{n+1}}: \sum_ix_i^2=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a n-sphere element (i.e. a vector of shape (n+1,)), the output
       is a vector of shape (n,).
     - input is a nd-array of n-sphere elements with a total shape (..., n+1),
       the output is a nd-array of shape (..., n).
    """,
    note="There is no bijective mapping between the whole shpere and uncontrained vector space. "
    "Some boundaries of the sphere are excluded.",
    reciprocal="reals_to_sphere",
    scale=False,
    input_shape="(..., n+1)",
    output_shape="(..., n)",
)
def sphere_to_reals(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to half-sphere element.

    The n-dimensional unit-half-sphere is defined by: :math:`\mathsf{{HS}}_n =
    \left\{{x\in\mathbb R^{{n+1}}: x_n>0\wedge\sum_ix_i^2=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a vector of shape (n,), the output is a n-half-sphere element, i.e.
       a vector of shape (n+1,).
     - input is a nd-array of shape (..., n), the output is a nd-array of
       n-half-sphere elements with a total shape (..., n+1).
    """,
    reciprocal="half_sphere_to_reals",
    scale=False,
    input_shape="(..., n)",
    output_shape="(..., n+1)",
)
def reals_to_half_sphere(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform to half-sphere element vector of reals.

    The n-dimensional unit-half-sphere is defined by: :math:`\mathsf{{HS}}_n =
    \left\{{x\in\mathbb R^{{n+1}}: x_n>0\wedge\sum_ix_i^2=1\right\}}\subset \mathbb R^{{n+1}}`.

    If:
     - input is a n-half-sphere element (i.e. a vector of shape (n+1,)), the output
       is a vector of shape (n,).
     - input is a nd-array of n-half-sphere elements with a total shape (..., n+1),
       the output is a nd-array of shape (..., n).
    """,
    reciprocal="reals_to_half_sphere",
    scale=False,
    input_shape="(..., n+1)",
    output_shape="(..., n)",
)
def half_sphere_to_reals(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to ball element.

    The n-dimensional unit-ball is defined by: :math:`\mathcal B_n =
    \left\{{x\in\mathbb R^n: \sum_ix_i^2<1\right\}}\subset \mathbb R^n`.

    If:
     - input is a vector of shape (n,), the output is a n-ball element, i.e.
       a vector of shape (n+1,).
     - input is a nd-array of shape (..., n), the output is a nd-array of
       n-ball elements with a total shape (..., n).
    """,
    reciprocal="ball_to_reals",
    scale=False,
    input_shape="(..., n)",
    output_shape="(..., n)",
)
def reals_to_ball(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform to ball element vector of reals.

    The n-dimensional unit-ball is defined by: :math:`\mathcal B_n =
    \left\{{x\in\mathbb R^n: \sum_ix_i^2<1\right\}}\subset \mathbb R^n`.

    If:
     - input is a n-ball element (i.e. a vector of shape (n+1,)), the output
       is a vector of shape (n,).
     - input is a nd-array of n-ball elements with a total shape (..., n),
       the output is a nd-array of shape (..., n).
    """,
    reciprocal="reals_to_ball",
    scale=False,
    input_shape="(..., n)",
    output_shape="(..., n)",
)
def ball_to_reals(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform correlation matrix to vector.

    A correlation matrix is a symmetric definite positive matrix with unit
    diagonal.

    If:
     - input is a correlation matrix of shape (n,n), the output is a vector of
       shape (N,) with N=n*(n-1)/2.
     - input is a nd-array of correlation matrix with total shape (..., n, n),
       the output is a nd-array of shape (..., N) with N=n*(n-1)/2.
    """,
    reciprocal="reals_to_corr_matrix",
    scale=False,
    input_shape="(..., n, n)",
    output_shape="(..., N)",
)
def corr_matrix_to_reals(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to correlation matrix.

    A correlation matrix is a symmetric definite positive matrix with unit
    diagonal.

    If:
     - input is a vector of shape (N,), with N=n*(n-1)/2, the output is a (n,n)
       correlation matrix.
     - input is a nd-array of shape (..., N), with N=n*(n-1)/2, the output is a
       nd-array of correlation matrices with total shape (..., n, n).
    """,
    reciprocal="corr_matrix_to_reals",
    scale=False,
    input_shape="(..., N)",
    output_shape="(..., n, n)",
)
def reals_to_corr_matrix(x):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform symmetric positive definite matrix to vector.

    If:
     - input is a symmetric positive definite matrix of shape (n,n), the output
       is a vector of shape (N,) with N=n*(n+1)/2.
     - input is a nd-array of symmetric positive definite matrix with total
       shape (..., n, n), the output is a nd-array of shape (..., N) with
       N=n*(n+1)/2.
    """,
    reciprocal="reals_to_spd_matrix",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., n, n)",
    output_shape="(..., N)",
)
def spd_matrix_to_reals(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to symmetric positive definite matrix.

    If:
     - input is a vector of shape (N,), with N=n*(n+1)/2, the output is a (n,n)
       symmetric positive definite matrix.
     - input is a nd-array of shape (..., N), with N=n*(n+1)/2, the output is a
       nd-array of symmetric positive definite matrices with total shape (..., n, n).
    """,
    reciprocal="spd_matrix_to_reals",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., N)",
    output_shape="(..., n, n)",
)
def reals_to_spd_matrix(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform symmetric matrix to vector.

    If:
     - input is a symmetric matrix of shape (n,n), the output is a vector of
       shape (N,) with N=n*(n+1)/2.
     - input is a nd-array of symmetric matrix with total shape (..., n, n), the
       output is a nd-array of shape (..., N) with N=n*(n+1)/2.
    """,
    reciprocal="reals_to_sym_matrix",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., n, n)",
    output_shape="(..., N)",
)
def sym_matrix_to_reals(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to symmetric matrix.

    If:
     - input is a vector of shape (N,), with N=n*(n+1)/2, the output is a (n,n)
       symmetric matrix.
     - input is a nd-array of shape (..., n), with N=n*(n+1)/2, the output is a
       nd-array of symmetric matrices with total shape (..., n, n).
    """,
    reciprocal="sym_matrix_to_reals",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., N)",
    output_shape="(..., n, n)",
)
def reals_to_sym_matrix(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform diagonal matrix to vector.

    If:
     - input is a diagonal matrix of shape (n,n), the output is a vector of
       shape (N,) with N=n*(n+1)/2.
     - input is a nd-array of diagonal matrix with total shape (..., n, n), the
       output is a nd-array of shape (..., n).
    """,
    reciprocal="reals_to_diag_matrix",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., n, n)",
    output_shape="(..., n)",
)
def diag_matrix_to_reals(x, scale=1.0):
    raise NotImplementedError


@decorate_with_doc(
    r"""
    Bijective function which transform vector of reals to diagonal matrix.

    If:
     - input is a vector of shape (n,), the output is a (n,n)
       diagonal matrix.
     - input is a nd-array of shape (..., n), the output is a
       nd-array of diagonal matrices with total shape (..., n, n).
    """,
    reciprocal="diag_matrix_to_reals",
    scale=True,
    scale_with="the diagonal of the matrix",
    input_shape="(..., n)",
    output_shape="(..., n, n)",
)
def reals_to_diag_matrix(x, scale=1.0):
    raise NotImplementedError
