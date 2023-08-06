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

import textwrap


def decorate_with_doc(
    main_doc,
    *,
    note="",
    input_shape="",
    output_shape="",
    scale=False,
    scale_with="input",
    reciprocal="",
):
    def decorator(fun):
        fun.__doc__ = main_doc + textwrap.indent(
            textwrap.dedent(
                f"""
                {{backend_desc}}

                Parameters
                ----------
                x : {input_shape+' ' if input_shape else ''}{{array_like}}
                    input{' with shape '+input_shape if input_shape else ''}.
                """
            )
            + (
                "scale : {array_like}\n    "
                f"scale of the mapping. Must be a scalar or shape compatible with the {scale_with}.\n"
                if scale
                else ""
            )
            + (
                (
                    textwrap.dedent(
                        f"""
                        Note
                        ----
                        """
                    )
                    + "\n".join(textwrap.wrap(note, 80))
                    + "\n"
                )
                if note
                else ""
            )
            + textwrap.dedent(
                f"""
                Returns
                -------
                {output_shape+' ' if output_shape else ''}{{array_like}}
                    the mapping of the input bu the function{', with shape '+output_shape if output_shape else ''}.
                """
            )
            + (
                textwrap.dedent(
                    f"""
                    See Also
                    --------
                    {reciprocal}: the reciprocal function.
                    """
                )
                if reciprocal
                else ""
            ),
            "    ",
        )
        return fun

    return decorator


def get_doc(
    *,
    array_like,
    backend_desc,
):
    from . import _dummy

    def decorator(fun):
        dummy_fun = getattr(_dummy, fun.__name__)
        fun.__doc__ = dummy_fun.__doc__.format(
            backend_desc=backend_desc, array_like=array_like
        )
        return fun

    return decorator
