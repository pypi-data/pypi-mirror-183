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
    shape_param_scalar,
    doc_reals1d_to_params,
    doc_params_to_reals1d,
    ShapedParam,
)


class Real(ShapedParam):
    """Representation of the parametrization of reals.

    This representation is used to represent reals field, vectors of reals,
    matrices of reals, and nd-arrays of reals.

    Note
    ----
    This parametrization is only reshaping and optional scaling.

    {examples}
    """

    @method_add_doc(
        f"""Representation of parametrization of reals.

        Represent reals field, vectors of reals, matrices of reals, and nd-arrays of reals.

        Parameters
        ----------
        loc : {{array_like}} or float, optional
            location added after the transformation. Must be shape
            compatible or broadcatable with target shape.
        scale : {{array_like}} or float, optional
            scale applied after the transformation.  Must be shape
            compatible or broadcastable with target shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, loc=0.0, scale=1.0, shape=None):
        if shape is None:
            self._shape = None
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert is_broadcastable_without_change(
            self._shape, loc
        ), "loc must be a scalar or a shape broadcastable array."
        assert is_broadcastable_without_change(
            self._shape, scale
        ), "scale must be a scalar or a shape broadcastable array."
        self._loc = loc
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        assert one_or_all(self._scale > 0), "Scale must be positive"
        self._size = (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        if one_or_any(loc != 0.0):
            repr_args.append(f"loc={loc!r}")
        if one_or_any(scale != 1.0):
            repr_args.append(f"scale={scale!r}")
        if self._shape is not None:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        value = self._loc + self._scale * (
            x.reshape(self._shape)
            if self._shape is not None and hasattr(x, "shape")
            else x
        )
        if self._shape is None and hasattr(value, "shape") and value.shape:
            return value[0]
        return value

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape(x)
        return ((x - self._loc) / self._scale).ravel()


class _RealBoundedOne(ShapedParam):
    _disp_bound = True

    def __init__(self, *, bound=0.0, scale=1.0, shape=None, disp_scale=None):
        if shape is None:
            self._shape = None
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        self._bound = bound
        assert is_broadcastable_without_change(
            self._shape, scale
        ), "Scale must be a scalar or a shape broadcastable array."
        self._scale = (
            scale if hasattr(scale, "shape") else self._backend._to_array(scale)
        )
        self._size = (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        if self._disp_bound:
            repr_args.append(f"bound={bound!r}")
        if disp_scale is None:
            disp_scale = scale
        if one_or_any(disp_scale != 1.0):
            repr_args.append(f"scale={disp_scale!r}")
        if self._shape is not None:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals with one bound constraint (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        value = self._bound + self._backend.softplus(
            x.reshape(self._shape)
            if self._shape is not None and hasattr(x, "shape")
            else x,
            scale=self._scale,
        )
        if self._shape is None and hasattr(value, "shape") and value.shape:
            return value[0]
        return value

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals with one bound constraint (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def params_to_reals1d(self, x):
        self._check_params_shape(x)
        return self._backend.softplusinv(x - self._bound, scale=self._scale).ravel()


class RealLowerBounded(_RealBoundedOne):
    """Representation of the parametrization of reals with lower bound.

    This representation is used to represent the set of reals with lower
    bounds, vectors,  matrices and nd-arrays with lower bound.

    Note
    ----
    This parametrization use the softplus function and its reciprocical.

    {examples}
    """

    _disp_bound = True

    @method_add_doc(
        f"""Representation of the parametrization of reals with lower bound.

        This representation is used to represent the set of reals with lower
        bounds, vectors,  matrices and nd-arrays with lower bound.

        Parameters
        ----------
        bound : {{array_like}} or float
            the lower bound. Must be shape compatible or broadcastable wih
            the target shape.
        scale : {{array_like}} or float, optional
            scale applied after the transformation. **The scale should have
            the same order of magnitude than expected values (relatively to
            the bound) in constrained space.** Must be a scalar or
            shape-compatible or broadcastable with target shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, bound, scale=1.0, shape=None):
        assert one_or_all(self._backend._to_array(scale) > 0), "Scale must be positive"
        super().__init__(shape=shape, bound=bound, scale=scale)


class RealPositive(RealLowerBounded):
    """Representation of the parametrization of positive reals.

    This representation is used to represent the set of positive reals,
    vectors,  matrices and nd-arrays.

    Note
    ----
    This parametrization use the softplus function and its reciprocical.

    {examples}
    """

    _disp_bound = False

    @method_add_doc(
        f"""Representation of the parametrization of positive reals.

        This representation is used to represent the set of positive reals,
        vectors,  matrices and nd-arrays with lower bound.

        Parameters
        ----------
        scale : {{array_like}} or float, optional
            scale applied after the transformation. **The scale should have
            the same order of magnitude than expected values in constrained
            space.** Must be shape compatible or broadcastable with target
            shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, scale=1.0, shape=None):
        super().__init__(shape=shape, bound=0.0, scale=scale)


class RealUpperBounded(_RealBoundedOne):
    """Representation of the parametrization of reals with upper bound.

    This representation is used to represent the set of reals with upper
    bounds, vectors,  matrices and nd-arrays with upper bound.

    Note
    ----
    This parametrization use the softplus function and its reciprocical.

    {examples}
    """

    _disp_bound = True

    @method_add_doc(
        f"""Representation of the parametrization of reals with upper bound.

        This representation is used to represent the set of reals with upper
        bounds, vectors,  matrices and nd-arrays with upper bound.

        Parameters
        ----------
        bound : {{array_like}} or float
            the upper bound. Must be shape compatible or broadcastable wih
            the target shape.
        scale : {{array_like}} or float, optional
            scale applied after the transformation. **The scale should have
            the same order of magnitude than expected values (relatively to
            the bound) in constrained space.** Must be shape compatible
            or broadcastable with target shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, bound, scale=1.0, shape=None):
        assert one_or_all(self._backend._to_array(scale) > 0), "Scale must be positive"
        super().__init__(shape=shape, bound=bound, scale=-scale, disp_scale=scale)


class RealNegative(RealUpperBounded):
    """Representation of the parametrization of negative reals.

    This representation is used to represent the set of negative reals,
    vectors,  matrices and nd-arrays.

    Note
    ----
    This parametrization use the softplus function and its reciprocical.

    {examples}
    """

    _disp_bound = False

    @method_add_doc(
        f"""Representation of the parametrization of negative reals.

        This representation is used to represent the set of negative reals,
        vectors,  matrices and nd-arrays with lower bound.

        Parameters
        ----------
        scale : {{array_like}} or float, optional
            scale applied after the transformation. **The scale should have
            the same order of magnitude than expected values in constrained
            space.** Must be shape compatible or broadcastable with target
            shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, shape=None, scale=1.0):
        super().__init__(shape=shape, bound=0.0, scale=scale)


class RealBounded(ShapedParam):
    """Representation of the parametrization of reals with lower
    and upper bounds.

    This representation is used to represent the set of reals with lower
    and upper bounds, vectors,  matrices and nd-arrays with lower and upper
    bounds.

    Note
    ----
    This parametrization use expit/logit functions or tanh/arctanh depending
    on bounds to acheive best numerical precision.

    {examples}
    """

    _disp_bounds = True
    _supplementary_methods = (
        "_reals1d_to_params_0X",
        "_params_to_reals1d_0X",
        "_reals1d_to_params_X0",
        "_params_to_reals1d_X0",
        "_reals1d_to_params_XY",
        "_params_to_reals1d_XY",
    )

    @method_add_doc(
        f"""Representation of the parametrization of lower and upper bounded reals.

        This representation is used to represent the set of lower and upper
        bounded reals, vectors,  matrices and nd-arrays with lower and upper
        bound.

        Parameters
        ----------
        bound_lower : {{array_like}} or float
            the lower bound. Must be shape compatible or broadcastable wih
            the target shape.
        bound_upper : {{array_like}} or float
            the lower bound. Must be shape compatible or broadcastable wih
            the target shape.
        {shape_param_scalar}
        """
    )
    def __init__(self, *, bound_lower, bound_upper, shape=None):
        if shape is None:
            self._shape = None
        elif isinstance(shape, collections.abc.Iterable):
            self._shape = tuple(shape)
        else:
            self._shape = (shape,)
        assert one_or_all(
            bound_lower < bound_upper
        ), "Lower bound must be lower than upper bound"
        self._bound_lower = bound_lower
        self._bound_upper = bound_upper
        self._bound_upper_minus_lower = bound_upper - bound_lower
        self._bound_med = (bound_lower + bound_upper) / 2
        self._bound_radius = self._bound_upper_minus_lower / 2
        self._size = (
            1 if self._shape is None else functools.reduce(operator.mul, self._shape, 1)
        )
        repr_args = []
        if self._disp_bounds:
            repr_args.append(f"bound_lower={bound_lower!r}")
            repr_args.append(f"bound_upper={bound_upper!r}")
        if self._shape is not None:
            repr_args.append(f"shape={self._shape!r}")
        self._repr = self.__class__.__name__ + f"({', '.join(repr_args)})"

        if one_or_all(self._bound_lower == 0):
            self.reals1d_to_params = self._reals1d_to_params_0X
            self.params_to_reals1d = self._params_to_reals1d_0X
        elif one_or_all(self._bound_upper == 0):
            self.reals1d_to_params = self._reals1d_to_params_X0
            self.params_to_reals1d = self._params_to_reals1d_X0
        else:
            self.reals1d_to_params = self._reals1d_to_params_XY
            self.params_to_reals1d = self._params_to_reals1d_XY

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def params_to_reals1d(self, x):
        raise NotImplementedError  # only for doc, this method is overrided in __init__

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def reals1d_to_params(self, x):
        raise NotImplementedError  # only for doc, this method is overrided in __init__

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _reals1d_to_params_0X(self, x):
        x = self._check_reals1d_size(x)
        value = self._bound_upper_minus_lower * self._backend.expit(
            x.reshape(self._shape)
            if self._shape is not None and hasattr(x, "shape")
            else x
        )
        if self._shape is None and hasattr(value, "shape") and value.shape:
            return value[0]
        return value

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _params_to_reals1d_0X(self, x):
        self._check_params_shape(x)
        return self._backend.logit(x / self._bound_upper_minus_lower).ravel()

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _reals1d_to_params_X0(self, x):
        x = self._check_reals1d_size(x)
        value = -self._bound_upper_minus_lower * self._backend.expit(
            -(
                x.reshape(self._shape)
                if self._shape is not None and hasattr(x, "shape")
                else x
            )
        )
        if self._shape is None and hasattr(value, "shape") and value.shape:
            return value[0]
        return value

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _params_to_reals1d_X0(self, x):
        self._check_params_shape(x)
        return -self._backend.logit(-x / self._bound_upper_minus_lower).ravel()

    @method_add_doc(
        doc_reals1d_to_params.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _reals1d_to_params_XY(self, x):
        x = self._check_reals1d_size(x)
        value = self._bound_med + self._bound_radius * self._backend.tanh(
            (
                x.reshape(self._shape)
                if self._shape is not None and hasattr(x, "shape")
                else x
            )
            / 2
        )
        if self._shape is None and hasattr(value, "shape") and value.shape:
            return value[0]
        return value

    @method_add_doc(
        doc_params_to_reals1d.format(
            set_name="reals with lower and upper bound constraints (or vectors of reals, matrices, nd-arrays)",
        )
    )
    def _params_to_reals1d_XY(self, x):
        self._check_params_shape(x)
        return (
            2
            * self._backend.arctanh((x - self._bound_med) / self._bound_radius).ravel()
        )


class RealBounded01(RealBounded):
    """Representation of the parametrization of reals in (0,1).

    This representation is used to represent the set of reals with lower
    and upper bounds, vectors,  matrices and nd-arrays with lower and upper
    bounds.

    Note
    ----
    This parametrization use expit/logit functions.

    {examples}
    """

    _disp_bounds = False

    @method_add_doc(
        f"""Representation of the parametrization of reals in (0,1).

        This representation is used to represent the set of reals in (0,1),
        vectors,  matrices and nd-arrays with elements in (0,1).

        Parameters
        ----------
        {shape_param_scalar}
        """
    )
    def __init__(self, *, shape=None):
        super().__init__(bound_lower=0, bound_upper=1, shape=shape)
