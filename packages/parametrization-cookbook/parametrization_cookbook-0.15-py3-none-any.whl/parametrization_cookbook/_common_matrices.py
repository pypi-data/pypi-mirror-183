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

import collections
import operator
import functools

from ._common_base import (
    one_or_all,
    one_or_any,
    is_broadcastable_without_change,
    method_add_doc,
    shape_param_vector,
    doc_reals1d_to_params,
    doc_params_to_reals1d,
    ShapedParam,
)


class MatrixDiag(ShapedParam):
    r"""Representation of the parametrization of diagonal matrices.

    This representation is used to represent diagonal matrices, or nd-array
    of diagonal matrix (nd-array where each element M[i0,i1,...,ik,:,:] is a
    diagonal matrix).

    Note
    ----
    Transformation are built on reshaping operations.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of diagonal matrices.

        This representation is used to represent diagonal matrices, or nd-array
        of diagonal matrix (nd-array where each element M[i0,i1,...,ik,:,:] is a
        diagonal matrix).

        Parameters
        ----------
        dim : int
            matrix size.
        loc : {{array_like}} or float, optional
            location added after the transformation. Must be shape
            compatible or broadcatable with the diagonal.
        scale : {{array_like}} or float, optional
            scale applied after the transformation.  Must be shape
            compatible or broadcastable with the diagonal.
        {shape_param_vector("(dim, dim)")}
        """
    )
    def __init__(self, *, dim, loc=0.0, scale=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        assert is_broadcastable_without_change(
            self._shape, loc
        ), "loc must be a scalar or a shape broadcastable array."
        assert is_broadcastable_without_change(
            self._shape + (dim,), scale
        ), "scale must be a scalar or a shape broadcastable array."
        self._loc = loc
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        assert one_or_all(self._scale > 0), "Scale must be positive"
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(loc != 0.0):
            repr_args.append(f"loc={loc!r}")
        if one_or_any(scale != 1.0):
            repr_args.append(f"scale={scale!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="diagonal matrix or nd-array of diagonal matrices",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_diag_matrix(
            self._loc + self._scale * x.reshape(self._shape + (self._dim,))
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="diagonal matrix or nd-array of diagonal matrices",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,) * 2)
        return (
            (self._backend.diag_matrix_to_reals(x) - self._loc) / self._scale
        ).ravel()


class MatrixDiagPosDef(ShapedParam):
    r"""Representation of the parametrization of diagonal positive definite matrices.

    This representation is used to represent diagonal positive definite
    matrices, or nd-array of diagonal positive definite matrix (nd-array
    where each element M[i0,i1,...,ik,:,:] is a diagonal positive definite
    matrix).

    Note
    ----
    Transformation are built on softplus and reshaping operations.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of diagonal positive definite matrices.

        This representation is used to represent diagonal positive definite
        matrices, or nd-array of diagonal positive definite matrix (nd-array
        where each element M[i0,i1,...,ik,:,:] is a diagonal positive definite
        matrix).

        Parameters
        ----------
        dim : int
            matrix size.
        scale : {{array_like}} or float, optional
            scale applied after the transformation.
            **The scale  should have the same order of magnitude than
            expected diagonal.**  Must be shape compatible or broadcastable
            with the diagonal.
        {shape_param_vector("(dim, dim)")}
        """
    )
    def __init__(self, *, dim, scale=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        assert is_broadcastable_without_change(
            self._shape + (dim,), scale
        ), "scale must be a scalar or a shape broadcastable array."
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        assert one_or_all(self._scale > 0), "Scale must be positive"
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(scale != 1.0):
            repr_args.append(f"scale={scale!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="diagonal positive definite matrix or nd-array of diagonal positive definite matrices",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_diag_matrix(
            self._backend.softplus(
                x.reshape(self._shape + (self._dim,)), scale=self._scale
            )
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="diagonal positive definite matrix or nd-array of diagonal positive definite matrices",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,) * 2)
        return self._backend.softplusinv(
            self._backend.diag_matrix_to_reals(x), scale=self._scale
        ).ravel()


class MatrixSym(ShapedParam):
    r"""Representation of the parametrization of symmetric matrices.

    This representation is used to represent symmetric matrices, or nd-array
    of symmetric matrix (nd-array where each element M[i0,i1,...,ik,:,:] is
    a symmetric matrix).

    Note
    ----
    Transformation are built on reshaping operations.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of symmetric matrices.

        This representation is used to represent symmetric matrices, or nd-array
        of symmetric matrix (nd-array where each element M[i0,i1,...,ik,:,:] is
        a symmetric matrix).

        Parameters
        ----------
        dim : int
            matrix size.
        scale : {{array_like}} or float, optional
            scale applied after the transformation.
            **The scale  should have the same order of magnitude than
            expected diagonal.**  Must be shape compatible or broadcastable
            with the diagonal.
        {shape_param_vector("(dim, dim)")}
        """
    )
    def __init__(self, *, dim, scale=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        assert is_broadcastable_without_change(
            self._shape + (dim,), scale
        ), "scale must be a scalar or a shape broadcastable array."
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        assert one_or_all(self._scale > 0), "Scale must be positive"
        self._size = (
            dim
            * (dim + 1)
            // 2
            * (
                1
                if self._shape is None
                else functools.reduce(operator.mul, self._shape, 1)
            )
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(scale != 1.0):
            repr_args.append(f"scale={scale!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="symmetric matrix or nd-array of symmetric matrices",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_sym_matrix(
            x.reshape(self._shape + (self._dim * (self._dim + 1) // 2,)),
            scale=self._scale,
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="symmetric matrix or nd-array of symmetric matrices",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,) * 2)
        return self._backend.sym_matrix_to_reals(x, scale=self._scale).ravel()


class MatrixSymPosDef(ShapedParam):
    r"""Representation of the parametrization of symmetric positive definite matrices.

    This representation is used to represent symmetric positive definite
    matrices, or nd-array of symmetric positive definite matrix (nd-array
    where each element M[i0,i1,...,ik,:,:] is a symmetric positive definite
    matrix).

    Note
    ----
    Transformation are built on Cholesky factorization, softplus, and
    reshaping operations.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of symmetric matrices.

        This representation is used to represent symmetric positive definite
        matrices, or nd-array of symmetric positive definite matrix (nd-array
        where each element M[i0,i1,...,ik,:,:] is a symmetric positive definite
        matrix).

        Parameters
        ----------
        dim : int
            matrix size.
        scale : {{array_like}} or float, optional
            scale applied after the transformation.
            **The scale  should have the same order of magnitude than
            expected diagonal.**  Must be shape compatible or broadcastable
            with the diagonal.
        {shape_param_vector("(dim, dim)")}
        """
    )
    def __init__(self, *, dim, scale=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        assert is_broadcastable_without_change(
            self._shape + (dim,), scale
        ), "scale must be a scalar or a shape broadcastable array."
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        assert one_or_all(self._scale > 0), "Scale must be positive"
        self._size = (
            dim
            * (dim + 1)
            // 2
            * (
                1
                if self._shape is None
                else functools.reduce(operator.mul, self._shape, 1)
            )
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(scale != 1.0):
            repr_args.append(f"scale={scale!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="symmetric positive definite matrix or nd-array of symmetric positive definite matrices",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_spd_matrix(
            x.reshape(self._shape + (self._dim * (self._dim + 1) // 2,)),
            scale=self._scale,
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="symmetric positive definite matrix or nd-array of symmetric positive definite matrices",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,) * 2)
        return self._backend.spd_matrix_to_reals(x, scale=self._scale).ravel()


class MatrixCorrelation(ShapedParam):
    r"""Representation of the parametrization of correlation matrices.

    This representation is used to represent correlation matrixes (a.k.a.
    symmetric positive definite matrices with unit diagonal), or nd-array of
    correlation matrixes (nd-array where each element M[i0,i1,...,ik,:,:] is a
    correlation matrix).

    Note
    ----
    Transformation are built on Cholesky factorization, reals to half-sphere
    transform, and reshaping operations.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of symmetric matrices.


        This representation is used to represent correlation matrixes (a.k.a.
        symmetric positive definite matrices with unit diagonal), or nd-array of
        correlation matrixes (nd-array where each element M[i0,i1,...,ik,:,:] is a
        correlation matrix).

        Parameters
        ----------
        dim : int
            matrix size.
        {shape_param_vector("(dim, dim)")}
        """
    )
    def __init__(self, *, dim, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._size = (
            dim
            * (dim - 1)
            // 2
            * (
                1
                if self._shape is None
                else functools.reduce(operator.mul, self._shape, 1)
            )
        )
        self._dim = dim
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="correlation matrix or nd-array of correlation matrices",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_corr_matrix(
            x.reshape(self._shape + (self._dim * (self._dim - 1) // 2,)),
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="correlation matrix or nd-array of correlation matrices",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,) * 2)
        return self._backend.corr_matrix_to_reals(x).ravel()
