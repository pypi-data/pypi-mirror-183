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

import functools
import operator
import math

import torch

from . import _doc_tools

_doc = _doc_tools.get_doc(
    array_like="tensor",
    backend_desc="This function is implemented using only function from torch.",
)


def _to_array(x):
    if isinstance(x, float):
        return x
    raise TypeError("all arguments must be Tensor of float")


def _array_size(x):
    return functools.reduce(operator.mul, x.shape, 1)


_concatenate = torch.concatenate


@_doc
def log1pexp(x):
    return torch.log1p(torch.exp(-torch.abs(x))) + torch.relu(x)


@_doc
def softplus(x, scale=1.0):
    return scale * log1pexp(x)


@_doc
def logexpm1(x):
    return x + torch.log(-torch.expm1(-x))


@_doc
def softplusinv(x, scale=1.0):
    return logexpm1(x / scale)


expit = torch.special.expit
logit = torch.special.logit

tanh = torch.tanh
arctanh = torch.arctanh


@_doc
def reals_to_simplex(x):
    device = x.device
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = -log1pexp(x) / torch.arange(n, 0, -1, device=device)
    logvalues = torch.concatenate(
        (torch.log(-torch.expm1(ksi)), torch.zeros(other_shape_and_one, device=device)),
        axis=-1,
    ) + torch.concatenate(
        (torch.zeros(other_shape_and_one, device=device), torch.cumsum(ksi, axis=-1)),
        axis=-1,
    )
    return torch.softmax(logvalues, dim=-1)


def _revcumsum(x):
    return x + torch.sum(x, axis=-1, keepdims=True) - torch.cumsum(x, axis=-1)


@_doc
def simplex_to_reals(x):
    device = x.device
    n = x.shape[-1] - 1
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = -torch.arange(n, 0, -1, device=device) * torch.log1p(
        x[other_slices + (slice(None, -1),)]
        / _revcumsum(x[other_slices + (slice(1, None),)])
    )
    return torch.log(-torch.expm1(ksi)) - ksi


@_doc
def reals_to_sphere(x):
    device = x.device
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = (
        torch.tanh(x / 2 / torch.sqrt(2 * torch.arange(n, 0, -1, device=device) - 1))
        * torch.pi
        / 2
    )
    ksi[other_slices + (-1,)] *= 2
    zeta = torch.exp(
        torch.cumsum(
            torch.log(torch.cos(ksi[other_slices + (slice(None, -1),)])), axis=-1
        )
    )
    return torch.concatenate(
        (torch.sin(ksi), torch.ones(other_shape_and_one, device=device)), axis=-1
    ) * torch.concatenate(
        (
            torch.ones(other_shape_and_one, device=device),
            zeta,
            (
                (zeta[other_slices + (-1,)] if n > 1 else 1.0)
                * torch.cos(ksi[other_slices + (-1,)])
            )[other_slices + (None,)],
        ),
        axis=-1,
    )


@_doc
def sphere_to_reals(x):
    device = x.device
    n = x.shape[-1] - 1
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = torch.arctan2(
        x[other_slices + (slice(None, -1),)],
        torch.concatenate(
            (
                torch.sqrt(
                    _revcumsum(x[other_slices + (slice(1, None),)] ** 2)[
                        other_slices + (slice(None, -1),)
                    ]
                ),
                x[other_slices + (-1,)][other_slices + (None,)],
            ),
            axis=-1,
        ),
    )
    ksi[other_slices + (-1,)] /= 2
    return (
        2
        * torch.arctanh(ksi / (torch.pi / 2))
        * torch.sqrt(2 * torch.arange(n, 0, -1, device=device) - 1)
    )


@_doc
def reals_to_half_sphere(x):
    device = x.device
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = (
        torch.pi
        / 2
        * torch.tanh(x / 2 / torch.sqrt(2 * torch.arange(n, 0, -1, device=device) - 1))
    )
    return torch.concatenate(
        (torch.sin(ksi), torch.ones(other_shape_and_one, device=device)), axis=-1
    ) * torch.concatenate(
        (
            torch.ones(other_shape_and_one, device=device),
            torch.exp(torch.cumsum(torch.log(torch.cos(ksi)), axis=-1)),
        ),
        axis=-1,
    )


@_doc
def half_sphere_to_reals(x):
    device = x.device
    n = x.shape[-1] - 1
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = torch.arctan2(
        x[other_slices + (slice(None, -1),)],
        torch.sqrt(_revcumsum(x[other_slices + (slice(1, None),)] ** 2)),
    )
    return (
        2
        * torch.arctanh(2 * ksi / torch.pi)
        * torch.sqrt(2 * torch.arange(n, 0, -1, device=device) - 1)
    )


@_doc
def reals_to_ball(x):
    n = x.shape[-1]
    assert n >= 2
    other_slices = (slice(None),) * (len(x.shape) - 1)
    g = math.sqrt(2) * torch.special.erfinv(torch.tanh(x / 2))
    normsq_g = (g**2).sum(axis=-1)
    normsq_g_rep_01 = normsq_g + (normsq_g == 0) * 1.0
    if n == 2:
        log_m = torch.log(-torch.expm1(-normsq_g_rep_01 / 2))
    else:
        log_m = torch.special.log_ndtr(
            (
                1 / 4 * logexpm1(4 * normsq_g_rep_01 ** (1 / 3))
                - n ** (1 / 3) * (1 - 2 / (9 * n))
            )
            / math.sqrt(2 / (9 * n ** (1 / 3)))
        )
    return (
        torch.exp(log_m / n - 0.5 * torch.log(normsq_g_rep_01))[other_slices + (None,)]
        * g
    )


@_doc
def ball_to_reals(x):
    n = x.shape[-1]
    assert n >= 2
    other_slices = (slice(None),) * (len(x.shape) - 1)
    normsq_x = (x**2).sum(axis=-1)
    normsq_x_rep_01 = normsq_x + (normsq_x == 0) * 1.0
    if n == 2:
        m_inv = -2 * torch.log1p(-normsq_x_rep_01)
    else:
        phi_inv = math.sqrt(2) * torch.special.erfinv(
            2 * normsq_x_rep_01 ** (n / 2) - 1
        )
        m_inv = (
            0.25
            * log1pexp(
                4
                * (
                    n ** (1 / 3) * (1 - 2 / (9 * n))
                    + phi_inv * math.sqrt(2 / (9 * n ** (1 / 3)))
                )
            )
        ) ** 3
    h_inv = (m_inv**0.5 / normsq_x_rep_01**0.5)[other_slices + (None,)] * x
    return 2 * torch.arctanh(torch.special.erf(h_inv / math.sqrt(2)))


@_doc
def corr_matrix_to_reals(x):
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    assert n > 1
    other_slices = (slice(None),) * (len(x.shape) - 2)

    sqrt_diag_x = x[other_slices + (torch.arange(n),) * 2] ** 0.5
    x = (
        x
        / sqrt_diag_x[other_slices + (slice(None), None)]
        / sqrt_diag_x[other_slices + (None, slice(None))]
    )

    y = torch.linalg.cholesky(x)
    return torch.concatenate(
        [
            half_sphere_to_reals(y[other_slices + (i, slice(None, i + 1))])
            for i in range(1, n)
        ],
        axis=-1,
    )


@_doc
def reals_to_corr_matrix(x):
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2 + 1)
    assert n * (n - 1) // 2 == x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 1)
    y = torch.zeros(x.shape[:-1] + (n, n))
    y[other_slices + (0, 0)] = 1.0
    for i in range(1, n):
        y[other_slices + (i, slice(None, i + 1))] = reals_to_half_sphere(
            x[other_slices + (slice((i * (i - 1) // 2), (i + 1) * (i) // 2),)]
        )

    z = y @ y.transpose(-2, -1)
    sqrt_diag_z = z[other_slices + (torch.arange(n),) * 2] ** 0.5
    z = (
        z
        / sqrt_diag_z[other_slices + (slice(None), None)]
        / sqrt_diag_z[other_slices + (None, slice(None))]
    )
    return z


@_doc
def spd_matrix_to_reals(x, scale=1.0):
    device = x.device
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = torch.sqrt(scale)
        x_rescaled = (
            x
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (slice(None), None)]
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (None, slice(None))]
        )
    else:
        x_rescaled = x / scale

    y = torch.linalg.cholesky(x_rescaled)
    y *= torch.sqrt(torch.arange(1, n + 1, device=device))[
        (None,) * (len(x.shape) - 2) + (slice(None), None)
    ]
    diag_values = y[other_slices + (torch.arange(n, device=device),) * 2]
    tril_values = y[other_slices + tuple(torch.tril_indices(n, n, -1, device=device))]
    return torch.concatenate((logexpm1(diag_values), tril_values), axis=-1)


@_doc
def reals_to_spd_matrix(x, scale=1.0):
    device = x.device
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2)
    assert (
        x.shape[-1] == n * (n + 1) // 2
    ), f"Incorect size. It does not exist n such as n*(n+1)/2=={x.shape[-1]}"
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    y = torch.zeros(x.shape[:-1] + (n, n), device=device, dtype=x.dtype)
    y[other_slices + (torch.arange(n, device=device),) * 2] = log1pexp(
        x[other_slices + (slice(None, n),)]
    )
    y[other_slices + tuple(torch.tril_indices(n, n, -1, device=device))] = x[
        other_slices + (slice(n, None),)
    ]

    y /= torch.sqrt(torch.arange(1, n + 1, device=device))[
        (None,) * (len(x.shape) - 2) + (slice(None), None)
    ]
    z_rescaled = y @ y.transpose(-1, -2)

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = torch.sqrt(scale)
        z = (
            z_rescaled
            * sqrt_scale[(None,) * (len(z_rescaled.shape) - 2) + (slice(None), None)]
            * sqrt_scale[(None,) * (len(z_rescaled.shape) - 2) + (None, slice(None))]
        )
    else:
        z = z_rescaled * scale
    return z


@_doc
def sym_matrix_to_reals(x, scale=1.0):
    device = x.device
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = torch.sqrt(scale)
        x_rescaled = (
            x
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (slice(None), None)]
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (None, slice(None))]
        )
    else:
        x_rescaled = x / scale

    return x_rescaled[other_slices + tuple(torch.tril_indices(n, n, device=device))]


@_doc
def reals_to_sym_matrix(x, scale=1.0):
    device = x.device
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2)
    assert (
        x.shape[-1] == n * (n + 1) // 2
    ), f"Incorect size. It does not exist n such as n*(n+1)/2=={x.shape[-1]}"
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    y = torch.zeros(x.shape[:-1] + (n, n), device=device, dtype=x.dtype)
    indices = tuple(torch.tril_indices(n, n, device=device))
    y[other_slices + indices] = x
    y_transposed = y.transpose(-1, -2).clone()
    y_transposed[other_slices + (torch.arange(n, device=device),) * 2] = 0
    y += y_transposed
    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = torch.sqrt(scale)
        z = (
            y
            * sqrt_scale[(None,) * (len(y.shape) - 2) + (slice(None), None)]
            * sqrt_scale[(None,) * (len(y.shape) - 2) + (None, slice(None))]
        )
    else:
        z = y / scale
    return z


@_doc
def diag_matrix_to_reals(x, scale=1.0):
    device = x.device
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    y = x[other_slices + (torch.arange(n, device=device),) * 2]
    return y / scale


@_doc
def reals_to_diag_matrix(x, scale=1.0):
    device = x.device
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    y = torch.zeros(x.shape[:-1] + (n, n), dtype=x.dtype, device=device)
    y[other_slices + (torch.arange(n, device=device),) * 2] = x
    return y
