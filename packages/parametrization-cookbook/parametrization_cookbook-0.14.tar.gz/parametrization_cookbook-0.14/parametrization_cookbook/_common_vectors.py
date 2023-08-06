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


class VectorSimplex(ShapedParam):
    r"""Representation of the parametrization of the unit-simplex.

    This representation is used to represent vector of the open unit-simplex,
    matrices where rows are elements of the open unit-simplex, or nd-array of
    positive values where the sum over the last dim is one.

    The n-dimensional open unit-simplex is defined by: :math:`\mathcal S_n =
    \left\{{x\in\mathbb {{R_+^*}}^{{n+1}}: \sum_ix_i=1\right\}}\subset \mathbb R^{{n+1}}`.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of the unit-simplex.

        This representation is used to represent vector of the open unit-simplex,
        matrices where rows are elements of the open unit-simplex, or nd-array of
        positive values where the sum over the last dim is one.

        Parameters
        ----------
        dim : int
            dimension of simplex. Elements of the `dim`-dimentional simplex are
            vectors of size `dim+1`.
        {shape_param_vector("(dim+1,)")}
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
        self._dim = dim
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="open unit-simplex elements or nd-arrays of open unit-simplex elements",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._backend.reals_to_simplex(x.reshape(self._shape + (self._dim,)))

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="open unit-simplex elements or nd-arrays of open unit-simplex elements",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim + 1,))
        return self._backend.simplex_to_reals(x).ravel()


class VectorSphere(ShapedParam):
    r"""Representation of the parametrization of the sphere.

    This representation is used to represent vector sphere,
    matrices where rows are elements of the sphere, or nd-array of
    positive values where the sum of square over the last dim is squared
    radius.

    The n-dimensional sphere of radius r is defined by: :math:`\mathsf S_n =
    \left\{{x\in\mathbb R^{{n+1}}: \sum_ix_i^2=r^2\right\}}\subset \mathbb R^{{n+1}}`.

    Note
    ----
    There is no bijective mapping between the whole shpere and uncontrained
    vector space. Some boundaries of the sphere are excluded.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of the sphere.

        This representation is used to represent vector sphere,
        matrices where rows are elements of the sphere, or nd-array of
        positive values where the sum of square over the last dim is squared
        radius.

        Parameters
        ----------
        dim : int
            dimension of sphere. Elements of the `dim`-dimentional sphere are
            vectors of size `dim+1`.
        radius : {{array_like}} or float, optional
            radius of the sphere. Must be shape compatible or broadcastable
            with target shape.
        {shape_param_vector("(dim+1,)")}
        """
    )
    def __init__(self, *, dim, radius=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        assert one_or_all(radius > 0), "Radius must be positive."
        assert is_broadcastable_without_change(
            self._shape, radius
        ), "Radius must be a scalar or a shape broadcastable array."
        self._radius = (
            radius if hasattr(radius, "shape") else self._backend._to_array(radius)
        )
        self._broadcast_radius = (
            self._radius.reshape(self._radius.shape + (1,))
            if hasattr(self._radius, "shape")
            else self._radius
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(self._radius != 1.0):
            repr_args.append(f"radius={self._radius!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="sphere elements or nd-arrays of sphere elements",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._broadcast_radius * self._backend.reals_to_sphere(
            x.reshape(self._shape + (self._dim,))
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="sphere elements or nd-arrays of sphere elements",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim + 1,))
        return self._backend.sphere_to_reals(x / self._broadcast_radius).ravel()


class VectorHalfSphere(ShapedParam):
    r"""Representation of the parametrization of the half-sphere.

    This representation is used to represent vector of the halh-sphere (element
    with last coordinate is positive), matrices where rows are elements of the
    sphere, or nd-array of positive values where the sum of square over the last
    dim is squared radius and where last index of last dim contains positive
    values.

    The n-dimensional half-sphere of radius r is defined by: :math:`\mathsf{{HS}}_n =
    \left\{{x\in\mathbb R^{{n+1}}: x_n>0\wedge\sum_ix_i^2=r^2\right\}}\subset \mathbb R^{{n+1}}`.

    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of the half-sphere.

        This representation is used to represent vector of the halh-sphere (element
        with last coordinate is positive), matrices where rows are elements of the
        sphere, or nd-array of positive values where the sum of square over the last
        dim is squared radius and where last index of last dim contains positive
        values.

        Parameters
        ----------
        dim : int
            dimension of half-sphere. Elements of the `dim`-dimentional sphere are
            vectors of size `dim+1`.
        radius : {{array_like}} or float, optional
            radius of the half-sphere. Must be shape compatible or broadcastable
            with target shape.
        {shape_param_vector("(dim+1,)")}
        """
    )
    def __init__(self, *, dim, radius=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        assert one_or_all(radius > 0), "Radius must be positive."
        assert is_broadcastable_without_change(
            self._shape, radius
        ), "Radius must be a scalar or a shape broadcastable array."
        self._radius = (
            radius if hasattr(radius, "shape") else self._backend._to_array(radius)
        )
        self._broadcast_radius = (
            self._radius.reshape(self._radius.shape + (1,))
            if hasattr(self._radius, "shape")
            else self._radius
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(self._radius != 1.0):
            repr_args.append(f"radius={self._radius!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="half-sphere elements or nd-arrays of half-sphere elements",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._broadcast_radius * self._backend.reals_to_half_sphere(
            x.reshape(self._shape + (self._dim,))
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="half-sphere elements or nd-arrays of half-sphere elements",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim + 1,))
        return self._backend.half_sphere_to_reals(x / self._broadcast_radius).ravel()


class VectorBall(ShapedParam):
    r"""Representation of the parametrization of the ball.

    This representation is used to represent vector of the ball,
    matrices where rows are elements of the ball, or nd-array of
    positive values where the sum of square over the last dim is less than
    squared radius.

    The n-dimensional ball of radius r is defined by: :math:`\mathcal B_n =
    \left\{{x\in\mathbb R^n: \sum_ix_i^2<r^2\right\}}\subset \mathbb R^n`.


    {examples}
    """

    @method_add_doc(
        f"""Representation of the parametrization of the sphere.

        This representation is used to represent vector sphere,
        matrices where rows are elements of the sphere, or nd-array of
        positive values where the sum of square over the last dim is squared
        radius.

        Parameters
        ----------
        dim : int
            dimension of ball. Elements of the `dim`-dimentional ball are
            vectors of size `dim`.
        radius : {{array_like}} or float, optional
            radius of the ball. Must be shape compatible or broadcastable
            with target shape.
        {shape_param_vector("(dim,)")}
        """
    )
    def __init__(self, *, dim, radius=1.0, shape=None):
        if shape is None:
            self._shape = ()
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert dim >= 1, "Dimention must be positive."
        self._dim = dim
        self._size = dim * (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        assert one_or_all(radius > 0), "Radius must be positive."
        assert is_broadcastable_without_change(
            self._shape, radius
        ), "Radius must be a scalar or a shape broadcastable array."
        self._radius = (
            radius if hasattr(radius, "shape") else self._backend._to_array(radius)
        )
        self._broadcast_radius = (
            self._radius.reshape(self._radius.shape + (1,))
            if hasattr(self._radius, "shape")
            else self._radius
        )
        repr_args = []
        repr_args.append(f"dim={dim!r}")
        if one_or_any(self._radius != 1.0):
            repr_args.append(f"radius={self._radius!r}")
        if self._shape:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="ball elements or nd-arrays of ball elements",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._broadcast_radius * self._backend.reals_to_ball(
            x.reshape(self._shape + (self._dim,))
        )

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="ball elements or nd-arrays of ball elements",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape_with_suppshape(x, (self._dim,))
        return self._backend.ball_to_reals(x / self._broadcast_radius).ravel()
