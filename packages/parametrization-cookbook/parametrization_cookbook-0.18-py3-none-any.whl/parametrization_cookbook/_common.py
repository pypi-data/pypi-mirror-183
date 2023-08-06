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
import itertools

from ._common_base import Param

from ._common_scalars import (
    Real,
    RealLowerBounded,
    RealPositive,
    RealUpperBounded,
    RealNegative,
    RealBounded,
    RealBounded01,
)

from ._common_vectors import (
    VectorSimplex,
    VectorSphere,
    VectorHalfSphere,
    VectorBall,
)

from ._common_matrices import (
    MatrixDiag,
    MatrixDiagPosDef,
    MatrixSym,
    MatrixSymPosDef,
    MatrixCorrelation,
)

from ._common_tuples import (
    Tuple,
    NamedTuple,
)


def decorate_method(*, fun, method_decorator, method_notes, array_like):
    @functools.wraps(fun)
    def fun_copy(*args, **kwargs):
        return fun(*args, **kwargs)

    if fun.__doc__ is not None:
        fun_copy.__doc__ = fun.__doc__.format(
            method_notes=method_notes, array_like=array_like
        )
    if method_decorator is not None:
        fun_copy = method_decorator(fun_copy)
    return fun_copy


def custom_class_decorator(
    *,
    backend,
    method_decorator=None,
    method_notes="",
    array_like="array_like",
    class_notes=""
):
    def the_decorator(cls):
        cls._backend = backend
        class_doc = cls.__bases__[0].__doc__
        if class_doc is not None:
            cls.__doc__ = class_doc.format(
                class_notes=class_notes,
                examples=getattr(cls, "_doc_examples", ""),
            )
        for method in ("__init__", "reals1d_to_params", "params_to_reals1d") + getattr(
            cls, "_supplementary_methods", ()
        ):
            setattr(
                cls,
                method,
                decorate_method(
                    fun=getattr(cls, method),
                    method_decorator=method_decorator if method != "__init__" else None,
                    method_notes=method_notes,
                    array_like=array_like,
                ),
            )
        return cls

    return the_decorator
