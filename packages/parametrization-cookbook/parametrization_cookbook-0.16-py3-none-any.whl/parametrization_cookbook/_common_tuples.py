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
import itertools

from ._common_base import (
    one_or_all,
    one_or_any,
    is_broadcastable_without_change,
    method_add_doc,
    shape_param_scalar,
    doc_reals1d_to_params_tuple,
    doc_params_to_reals1d_tuple,
    Param,
)


class Tuple(Param):
    r"""Representation of the parametrization by Cartesian product of parametrization.

    When the constrained parameter space is expressed as cartesian product
    of constrained parameters spaces, this class is able to represent the
    whole parameter space using tuples.

    See Also
    --------
    NamedTuple: same behavior as Tuple, but use names to index elementary
        parameters as collections.namedtuple

    {examples}
    """

    def __init__(self, *args):
        """Representation of the parametrization by Cartesian product of parametrization.

        When the constrained parameter space is expressed as cartesian product
        of constrained parameters spaces, this class is able to represent the
        whole parameter space using tuples.

        Parameters
        ----------
        *args :
            representation of elementary parametrizations. At least 2
            element must be provided.
        """

        assert all(
            isinstance(p, Param) for p in args
        ), "All arguments must be parameters instances"
        assert (
            len(args) >= 2
        ), "At least two parameters instances must be provided as argument."

        self._params = tuple(args)
        self._size = sum(p._size for p in self._params)
        self._repr = (
            self.__class__.__name__ + f"({', '.join(p._repr for p in self._params)})"
        )

        idx = tuple(
            itertools.chain((0,), itertools.accumulate(p._size for p in self._params))
        )
        self._idx = tuple(slice(a, b) for a, b in zip(idx[:-1], idx[1:]))

    @property
    def idx_params(self):
        return self._idx

    def __getitem__(self, idx):
        return self._params[idx]

    @method_add_doc(
        doc_params_to_reals1d_tuple.format(
            tuple_name="tuple",
        )
    )
    def params_to_reals1d(self, *values):
        assert values, "Values must be provided"
        if len(values) == 1:
            assert isinstance(values[0], collections.abc.Sequence) and len(
                values[0]
            ) == len(
                self._params
            ), "If only one arg is provided, it must be a sequence of parameters values"
            values = values[0]
        else:
            assert len(values) == len(
                self._params
            ), "Provided {len(values}} arguments, expecting {len(self._params} parameters values."
        return self._backend._concatenate(
            [p.params_to_reals1d(val) for p, val in zip(self._params, values)]
        )

    @method_add_doc(
        doc_reals1d_to_params_tuple.format(
            tuple_name="tuple",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return tuple(
            p.reals1d_to_params(x[sli]) for (p, sli) in zip(self._params, self._idx)
        )


class NamedTuple(Param):
    r"""Representation of the parametrization by Cartesian product of parametrization.

    When the constrained parameter space is expressed as cartesian product
    of constrained parameters spaces, this class is able to represent the
    whole parameter space using namedtuple.

    See Also
    --------
    Tuple: same behavior as NamedTuple, but use names to index elementary
        parameters tuple

    {examples}
    """

    def __init__(self, **kwargs):
        """Representation of the parametrization by Cartesian product of parametrization.

        When the constrained parameter space is expressed as cartesian product
        of constrained parameters spaces, this class is able to represent the
        whole parameter space using namedtuple.

        Parameters
        ----------
        **kwargs : elementary representations provided with key-values
        pairs.
        """

        assert all(
            isinstance(p, Param) for p in kwargs.values()
        ), "All arguments must be parameters instances"
        assert (
            len(kwargs) >= 1
        ), "At least one parameter instance must be provided as argument."

        self._params = kwargs
        self._size = sum(p._size for p in self._params.values())

        self._repr = (
            self.__class__.__name__
            + f"({', '.join(k+'='+p._repr for k,p in self._params.items())})"
        )
        self._typeret = collections.namedtuple("Parameters", self._params.keys())

        idx = tuple(
            itertools.chain(
                (0,), itertools.accumulate(p._size for p in self._params.values())
            )
        )
        self._idx = {
            k: slice(a, b) for (k, a, b) in zip(self._params.keys(), idx[:-1], idx[1:])
        }

    @property
    def idx_params(self):
        return self._typeret(**self._idx)

    def __getitem__(self, idx):
        return self._params[idx]

    @method_add_doc(
        doc_params_to_reals1d_tuple.format(
            tuple_name="namedtuple",
        )
    )
    def params_to_reals1d(self, *args, **kwargs):
        if args:
            assert (
                len(args) == 1
            ), "Only one positionnal parameters namedtuple can be provided."
            assert isinstance(
                args[0], (self._typeret, collections.abc.Mapping)
            ), "Only parameters namedtuple or dict can be provided as postionnal arg"
            if isinstance(args[0], self._typeret):
                input_arg = args[0]
            else:
                input_arg = self._typeret(**args[0])
        else:
            assert (
                kwargs
            ), "Parameter values must be provided with one positionnal argument, or individuals keywords and values arguments"
            input_arg = self._typeret(**kwargs)

        return self._backend._concatenate(
            [
                p.params_to_reals1d(getattr(input_arg, k))
                for k, p in self._params.items()
            ]
        )

    @method_add_doc(
        doc_reals1d_to_params_tuple.format(
            tuple_name="namedtuple",
        )
    )
    def reals1d_to_params(self, x):
        x = self._check_reals1d_size(x)
        return self._typeret(
            **{k: p.reals1d_to_params(x[self._idx[k]]) for k, p in self._params.items()}
        )
