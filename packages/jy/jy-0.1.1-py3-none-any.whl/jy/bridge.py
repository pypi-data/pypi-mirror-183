"""Python portals to JS"""

from typing import Any
from functools import partial

from dol.signatures import Sig

from jy.js_parse import dflt_py_to_js_value_trans, func_name_and_params_pairs

# TODO: Add value transformer (routing). For example, booleans, True->true
def _js_func_call(
    *args,
    __sig,
    __func_call_template,
    __value_trans=dflt_py_to_js_value_trans,
    __apply_defaults=True,
    **kwargs,
):
    _kwargs = __sig.kwargs_from_args_and_kwargs(
        args, kwargs, apply_defaults=__apply_defaults
    )
    inputs = map(__value_trans, _kwargs.values())
    inputs = ', '.join(map(str, inputs))
    return __func_call_template.format(inputs=inputs)


def mk_py_binder_func(
    name,
    params,
    *,
    prefix='',
    suffix='',
    doc='',
    value_trans=dflt_py_to_js_value_trans,
    apply_defaults=True,
):
    *_, func_name = name.split('.')  # e.g. object.containing.func --> func
    func_call_template = prefix + name + '({inputs})' + suffix

    sig = Sig.from_params(params)
    js_func_call = partial(
        _js_func_call,
        __sig=sig,
        __func_call_template=func_call_template,
        __value_trans=value_trans,
        __apply_defaults=apply_defaults,
    )
    js_func_call = sig(js_func_call)
    js_func_call.__name__ = func_name
    js_func_call.__doc__ = doc

    return js_func_call


class JsBridge:
    """
    The default class to make instances that will contain methods that mirror JS
    function calls
    """


def add_js_funcs(
    js_code: str,
    *,
    obj: Any = None,
    name: str | None = None,
    encoding: str | None = None,
    forbidden_method_names=(),
    apply_defaults=True
):
    """
    Add js call functions as attributes to an object.

    If object is not given, ``add_js_funcs`` will use a new ``JsBridge`` instance.

    """
    if obj is None:
        obj = JsBridge()

    forbidden_method_names = set(forbidden_method_names)

    for full_func_ref, params in func_name_and_params_pairs(js_code, encoding=encoding):
        *_, func_name = full_func_ref.split('.')  # e.g. object.containing.func --> func
        # TODO: Could specify a recovery function that finds another name instead of
        #  raising an error
        if func_name in forbidden_method_names:
            raise ValueError(
                f"This func name was already used, or mentioned in "
                f"the forbidden_method_names argument: {func_name}"
            )
        setattr(
            obj,
            func_name,
            mk_py_binder_func(full_func_ref, params, apply_defaults=apply_defaults)
        )

    if name:
        obj.__name__ = name

    return obj

