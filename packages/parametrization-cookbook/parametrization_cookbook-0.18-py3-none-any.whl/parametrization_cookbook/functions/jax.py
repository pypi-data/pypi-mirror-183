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

import jax
import jax.numpy as jnp

from . import _doc_tools

_doc = _doc_tools.get_doc(
    array_like="array_like",
    backend_desc="This function is JIT-compiled and implemented using only JAX functions.",
)


def _to_array(x):
    if isinstance(x, collections.abc.Iterable):
        return jnp.array(x)
    return jnp.array((x,))[0]


def _array_size(x):
    return x.size


_concatenate = jnp.concatenate


@_doc
@jax.jit
def log1pexp(x):
    return jnp.log1p(jnp.exp(-jnp.abs(x))) + jnp.maximum(x, 0)


@_doc
@jax.jit
def softplus(x, scale=1.0):
    return scale * log1pexp(x)


@_doc
@jax.jit
def logexpm1(x):
    return x + jnp.log(-jnp.expm1(-x))


@_doc
@jax.jit
def softplusinv(x, scale=1.0):
    return logexpm1(x / scale)


expit = jax.scipy.special.expit
logit = jax.scipy.special.logit

tanh = jnp.tanh
arctanh = jnp.arctanh


@_doc
@jax.jit
def reals_to_simplex(x):
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = -log1pexp(x) / jnp.arange(n, 0, -1)
    logvalues = jnp.concatenate(
        (jnp.log(-jnp.expm1(ksi)), jnp.zeros(other_shape_and_one)), axis=-1
    ) + jnp.concatenate(
        (jnp.zeros(other_shape_and_one), jnp.cumsum(ksi, axis=-1)), axis=-1
    )
    values = jnp.exp(logvalues - logvalues.max(axis=-1)[other_slices + (None,)])
    return values / values.sum(axis=-1)[other_slices + (None,)]


@_doc
@jax.jit
def simplex_to_reals(x):
    n = x.shape[-1] - 1
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = -jnp.arange(n, 0, -1) * jnp.log1p(
        x[other_slices + (slice(None, -1),)]
        / jnp.cumsum(x[other_slices + (slice(-1, 0, -1),)], axis=-1)[
            other_slices + (slice(None, None, -1),)
        ]
    )
    return jnp.log(-jnp.expm1(ksi)) - ksi


@_doc
@jax.jit
def reals_to_sphere(x):
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = jnp.tanh(x / 2 / jnp.sqrt(2 * jnp.arange(n, 0, -1) - 1)) * jnp.pi / 2
    ksi = ksi.at[other_slices + (-1,)].multiply(2)
    zeta = jnp.exp(
        jnp.cumsum(jnp.log(jnp.cos(ksi[other_slices + (slice(None, -1),)])), axis=-1)
    )
    return jnp.concatenate(
        (jnp.sin(ksi), jnp.ones(other_shape_and_one)), axis=-1
    ) * jnp.concatenate(
        (
            jnp.ones(other_shape_and_one),
            zeta,
            (
                (zeta[other_slices + (-1,)] if zeta.size > 0 else 1.0)
                * jnp.cos(ksi[other_slices + (-1,)])
            )[other_slices + (None,)],
        ),
        axis=-1,
    )


@_doc
@jax.jit
def sphere_to_reals(x):
    n = x.shape[-1] - 1
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = jnp.arctan2(
        x[other_slices + (slice(None, -1),)],
        jnp.concatenate(
            (
                jnp.sqrt(
                    jnp.cumsum(x[other_slices + (slice(None, 0, -1),)] ** 2, axis=-1)[
                        other_slices + (slice(None, 0, -1),)
                    ]
                ),
                x[other_slices + (-1,)][other_slices + (None,)],
            ),
            axis=-1,
        ),
    )
    ksi = ksi.at[other_slices + (-1,)].divide(2)
    return 2 * jnp.arctanh(ksi / (jnp.pi / 2)) * jnp.sqrt(2 * jnp.arange(n, 0, -1) - 1)


@_doc
@jax.jit
def reals_to_half_sphere(x):
    n = x.shape[-1]
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = jnp.pi / 2 * jnp.tanh(x / 2 / jnp.sqrt(2 * jnp.arange(n, 0, -1) - 1))
    return jnp.concatenate(
        (jnp.sin(ksi), jnp.ones(other_shape_and_one)), axis=-1
    ) * jnp.concatenate(
        (
            jnp.ones(other_shape_and_one),
            jnp.exp(jnp.cumsum(jnp.log(jnp.cos(ksi)), axis=-1)),
        ),
        axis=-1,
    )


@_doc
@jax.jit
def half_sphere_to_reals(x):
    n = x.shape[-1] - 1
    other_shape_and_one = x.shape[:-1] + (1,)
    other_slices = (slice(None),) * (len(x.shape) - 1)
    ksi = jnp.arctan2(
        x[other_slices + (slice(None, -1),)],
        jnp.sqrt(
            jnp.cumsum(x[other_slices + (slice(None, 0, -1),)] ** 2, axis=-1)[
                other_slices + (slice(None, None, -1),)
            ]
        ),
    )
    return 2 * jnp.arctanh(2 * ksi / jnp.pi) * jnp.sqrt(2 * jnp.arange(n, 0, -1) - 1)


@_doc
@jax.jit
def reals_to_ball(x):
    n = x.shape[-1]
    assert n >= 2
    other_slices = (slice(None),) * (len(x.shape) - 1)
    g = jnp.sqrt(2) * jax.scipy.special.erfinv(jnp.tanh(x / 2))
    normsq_g = (g**2).sum(axis=-1)
    normsq_g_rep_01 = normsq_g + (normsq_g == 0) * 1.0
    if n == 2:
        log_m = jnp.log(-jnp.expm1(-normsq_g_rep_01 / 2))
    else:
        log_m = jax.scipy.special.log_ndtr(
            (
                1 / 4 * logexpm1(4 * normsq_g_rep_01 ** (1 / 3))
                - n ** (1 / 3) * (1 - 2 / (9 * n))
            )
            / jnp.sqrt(2 / (9 * n ** (1 / 3)))
        )
    return (
        jnp.exp(log_m / n - 0.5 * jnp.log(normsq_g_rep_01))[other_slices + (None,)] * g
    )


@_doc
@jax.jit
def ball_to_reals(x):
    n = x.shape[-1]
    assert n >= 2
    other_slices = (slice(None),) * (len(x.shape) - 1)
    normsq_x = (x**2).sum(axis=-1)
    normsq_x_rep_01 = normsq_x + (normsq_x == 0) * 1.0
    if n == 2:
        m_inv = -2 * jnp.log1p(-normsq_x_rep_01)
    else:
        phi_inv = jnp.sqrt(2) * jax.scipy.special.erfinv(
            2 * normsq_x_rep_01 ** (n / 2) - 1
        )
        m_inv = (
            0.25
            * log1pexp(
                4
                * (
                    n ** (1 / 3) * (1 - 2 / (9 * n))
                    + phi_inv * jnp.sqrt(2 / (9 * n ** (1 / 3)))
                )
            )
        ) ** 3
    h_inv = (m_inv**0.5 / normsq_x_rep_01**0.5)[other_slices + (None,)] * x
    return 2 * jnp.arctanh(jax.scipy.special.erf(h_inv / jnp.sqrt(2)))


@_doc
@jax.jit
def corr_matrix_to_reals(x):
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    assert n > 1
    other_slices = (slice(None),) * (len(x.shape) - 2)

    sqrt_diag_x = x[other_slices + (jnp.arange(n),) * 2] ** 0.5
    x = (
        x
        / sqrt_diag_x[other_slices + (slice(None), None)]
        / sqrt_diag_x[other_slices + (None, slice(None))]
    )

    y = jnp.linalg.cholesky(x)
    return jnp.concatenate(
        [
            half_sphere_to_reals(y[other_slices + (i, slice(None, i + 1))])
            for i in range(1, n)
        ],
        axis=-1,
    )


@_doc
@jax.jit
def reals_to_corr_matrix(x):
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2 + 1)
    assert n * (n - 1) // 2 == x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 1)
    row_zero = jnp.zeros(x.shape[:-1] + (n,))
    y = jnp.stack(
        [row_zero.at[other_slices + (0,)].set(1.0)]
        + [
            row_zero.at[other_slices + (slice(None, i + 1),)].set(
                reals_to_half_sphere(
                    x[other_slices + (slice((i * (i - 1) // 2), (i + 1) * (i) // 2),)]
                )
            )
            for i in range(1, n)
        ],
        axis=-2,
    )

    z = y @ y.transpose(
        tuple(range(len(y.shape) - 2)) + (len(y.shape) - 1, len(y.shape) - 2)
    )
    sqrt_diag_z = z[other_slices + (jnp.arange(n),) * 2] ** 0.5
    z = (
        z
        / sqrt_diag_z[other_slices + (slice(None), None)]
        / sqrt_diag_z[other_slices + (None, slice(None))]
    )
    return z


@_doc
@jax.jit
def spd_matrix_to_reals(x, scale=1.0):
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = jnp.sqrt(scale)
        x_rescaled = (
            x
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (slice(None), None)]
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (None, slice(None))]
        )
    else:
        x_rescaled = x / scale

    y = jnp.linalg.cholesky(x_rescaled)
    y *= jnp.sqrt(jnp.arange(1, n + 1))[
        (None,) * (len(x.shape) - 2) + (slice(None), None)
    ]
    diag_values = y[other_slices + (jnp.arange(n),) * 2]
    tril_values = y[other_slices + jnp.tril_indices(n, -1)]
    return jnp.concatenate((logexpm1(diag_values), tril_values), axis=-1)


@_doc
@jax.jit
def reals_to_spd_matrix(x, scale=1.0):
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2)
    assert (
        x.shape[-1] == n * (n + 1) // 2
    ), f"Incorect size. It does not exist n such as n*(n+1)/2=={x.shape[-1]}"
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    y = (
        jnp.zeros(x.shape[:-1] + (n, n))
        .at[other_slices + (jnp.arange(n),) * 2]
        .set(log1pexp(x[other_slices + (slice(None, n),)]))
        .at[other_slices + jnp.tril_indices(n, -1)]
        .set(x[other_slices + (slice(n, None),)])
    )
    y /= jnp.sqrt(jnp.arange(1, n + 1))[
        (None,) * (len(x.shape) - 2) + (slice(None), None)
    ]
    z_rescaled = y @ y.transpose(
        tuple(range(len(y.shape) - 2)) + (len(y.shape) - 1, len(y.shape) - 2)
    )

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = jnp.sqrt(scale)
        z = (
            z_rescaled
            * sqrt_scale[(None,) * (len(z_rescaled.shape) - 2) + (slice(None), None)]
            * sqrt_scale[(None,) * (len(z_rescaled.shape) - 2) + (None, slice(None))]
        )
    else:
        z = z_rescaled * scale
    return z


@_doc
@jax.jit
def sym_matrix_to_reals(x, scale=1.0):
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = jnp.sqrt(scale)
        x_rescaled = (
            x
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (slice(None), None)]
            / sqrt_scale[(None,) * (len(x.shape) - 2) + (None, slice(None))]
        )
    else:
        x_rescaled = x / scale

    return x_rescaled[other_slices + jnp.tril_indices(n)]


@_doc
@jax.jit
def reals_to_sym_matrix(x, scale=1.0):
    n = int((8 * x.shape[-1] + 1) ** 0.5 / 2)
    assert (
        x.shape[-1] == n * (n + 1) // 2
    ), f"Incorect size. It does not exist n such as n*(n+1)/2=={x.shape[-1]}"
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    indices = jnp.tril_indices(n)
    y = jnp.zeros(x.shape[:-1] + (n, n)).at[other_slices + indices].set(x)
    y_transposed = (
        y.transpose(
            tuple(range(len(y.shape) - 2)) + (len(y.shape) - 1, len(y.shape) - 2)
        )
        .at[other_slices + (jnp.arange(n),) * 2]
        .set(0)
    )
    y = y + y_transposed
    if hasattr(scale, "shape") and len(scale.shape) == 1:
        sqrt_scale = jnp.sqrt(scale)
        z = (
            y
            * sqrt_scale[(None,) * (len(y.shape) - 2) + (slice(None), None)]
            * sqrt_scale[(None,) * (len(y.shape) - 2) + (None, slice(None))]
        )
    else:
        z = y / scale
    return z


@_doc
@jax.jit
def diag_matrix_to_reals(x, scale=1.0):
    assert len(x.shape) >= 2 and x.shape[-2] == x.shape[-1]
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 2)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"

    y = x[other_slices + (jnp.arange(n),) * 2]
    return y / scale


@_doc
@jax.jit
def reals_to_diag_matrix(x, scale=1.0):
    n = x.shape[-1]
    other_slices = (slice(None),) * (len(x.shape) - 1)
    if hasattr(scale, "shape"):
        assert len(scale.shape) == 0 or (
            len(scale.shape) == 1 and scale.shape[0] == n
        ), f"Non broacastable shapes, got matrix shape {x.shape!r} and scale shape {scale.shape!r}"
    y = jnp.zeros(x.shape[:-1] + (n, n)).at[other_slices + (jnp.arange(n),) * 2].set(x)
    return y
