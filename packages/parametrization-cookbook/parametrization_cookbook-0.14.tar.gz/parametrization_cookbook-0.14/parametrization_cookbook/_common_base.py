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

from .functions import _dummy as dummy_backend


def one_or_all(x):
    if hasattr(x, "shape"):
        return x.all()
    return x


def one_or_any(x):
    if hasattr(x, "shape"):
        return x.any()
    return x


def is_broadcastable_without_change(shape1, arr2):
    if shape1 is None:
        shape1 = ()
    shape2 = getattr(arr2, "shape", ())
    if len(shape2) > len(shape1):
        return False
    for a, b in zip(shape1[::-1], shape2[::-1]):
        if a != 1 and b != 1 and a != b:
            return False
    return True


def method_add_doc(doc):
    def mywrap(fun):
        fun.__doc__ = doc
        return fun

    return mywrap


shape_param_scalar = """shape : tuple of int or None, optional
            Shape of the custom space. If None (by default), the custom
            space is scalar field of reals."""

shape_param_vector = (
    lambda vect_dim: f"""shape : tuple of int, optional
            Shape of the custom space. If `shape==()` (by default), the
            custom space is the targeted vector space with shape
            `({vect_dim},)`. Else, the resulting shape will be
            `shape+{vect_dim}`."""
)

doc_reals1d_to_params = """Mapping from a 1-D unconstrained array of reals to {set_name}.

        Parameters
        ----------
        x : {{array_like}}
            unconstrained 1-D array

        {{method_notes}}Returns
        -------
        {{array_like}}
            mapped {set_name} value of `x`
        """

doc_params_to_reals1d = """Mapping from {set_name} to 1-D unconstrained array of reals.

        Parameters
        ----------
        x : {{array_like}}
            {set_name} value

        {{method_notes}}Returns
        -------
        {{array_like}}
            mapped value of `x` in the set of unconstrained 1-D array of reals
        """

doc_reals1d_to_params_tuple = """Mapping from a 1-D unconstrained array of reals to {tuple_name} of elementary parameters.

        Parameters
        ----------
        x : {{array_like}}
            unconstrained 1-D array

        {{method_notes}}Returns
        -------
        tuple
            mapped value of `x` in elementary parameters
        """

doc_params_to_reals1d_tuple = """Mapping from {tuple_name} of elementary parameters to 1-D unconstrained array of reals.

        Parameters
        ----------
        x : tuple
            value of elementary parameters

        {{method_notes}}Returns
        -------
        {{array_like}}
            mapped value of `x` in the set of unconstrained 1-D array of reals
        """


class Param:
    """Virtual class to represent parametrization

    This class must be derivated. The attribute `_size`, and the methods
    `reals1d_to_params` and `params_to_reals1d` must be definied.
    """

    _size: int
    _repr: str
    _backend = dummy_backend

    @property
    def size(self):
        """Size of the unconstraint 1-D reals space

        Returns
        -------
        int
        """
        return self._size

    def reals1d_to_params(self, x):
        raise NotImplementedError

    def params_to_reals1d(self, x):
        raise NotImplementedError

    def __repr__(self):
        if hasattr(self, "_repr"):
            return self._repr
        return object.__repr__(self)

    def _check_reals1d_size(self, x):
        if not hasattr(x, "shape"):
            if isinstance(x, collections.abc.Iterable):
                x = self._backend._to_array(x)
            else:
                x = self._backend._to_array((x,))
        else:
            if not x.shape:
                x = x.reshape((1,))
        assert len(x.shape) == 1, "Invalid shape. Input must be a 1-d array."
        assert (
            self._backend._array_size(x) == self._size
        ), f"Invalid size. Got {self._backend._array_size(x)!r}. Expected {self._size!r}."
        return x


class ShapedParam(Param):
    _shape: tuple

    @property
    def shape(self):
        """Shape of the constrained space.

        Returns
        -------
        tuple of ints or None
        """
        return self._shape

    def _check_params_shape(self, x):
        if self._shape is None:
            if hasattr(x, "shape"):
                assert x.shape == () or x.shape == (
                    1,
                ), f"Invalid shape. Got {x.shape!r}. Expected () or (1,)."
        else:
            assert hasattr(
                x, "shape"
            ), f"Invalid shape. Got no shape. Expected {self._shape!r}."
            assert (
                x.shape == self._shape
            ), f"Invalid shape. Got {x.shape!r}. Expected {self._shape!r}."

    def _check_params_shape_with_suppshape(self, x, suppshape):
        assert hasattr(
            x, "shape"
        ), f"Invalid shape. Got no shape. Expected {self._shape!r}."
        assert (
            x.shape == self._shape + suppshape
        ), f"Invalid shape. Got {x.shape!r}. Expected {self._shape+suppshape!r}."
