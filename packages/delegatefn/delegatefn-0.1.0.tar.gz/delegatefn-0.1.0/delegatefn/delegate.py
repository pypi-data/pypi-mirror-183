import inspect
import sys


def delegate(
    f,
    kwonly=False,
    doc=True
):
    "Delegate kwargs to another function."

    def decorator(
        g
    ):
        "Transfer keyword arguments, including annotations and docstrings, from f to g"
        fsig = inspect.signature(f)
        gsig = inspect.signature(g)
        # Transfer annotations from f to g for keyword arguments without annotations in g
        for name, param in fsig.parameters.items():
            if (
                    param.kind == param.KEYWORD_ONLY
                    or param.kind == param.POSITIONAL_OR_KEYWORD
            ):
                if name in gsig.parameters and gsig.parameters[name].annotation is inspect._empty:
                    gsig.parameters[name].annotation = param.annotation
        # Gather parameters from f
        # Exclude:
        # - arguments that are already defined in g
        # - positional-only arguments
        # - if kwonly, positional-or-keyword arguments
        fkwargs = {
            k: v
            for k, v in fsig.parameters.items()
            if k not in gsig.parameters
               and (v.kind == v.KEYWORD_ONLY or not kwonly and v.kind == v.POSITIONAL_OR_KEYWORD)
        }
        # Make all parameters keyword-only
        fkwargs = {
            k: v.replace(kind=v.KEYWORD_ONLY)
            for k, v in fkwargs.items()
        }
        # Add parameters to g
        # If the last parameter of f is **kwargs, add the new parameters before it
        if list(gsig.parameters.values())[-1].kind == inspect.Parameter.VAR_KEYWORD:
            parameters = list(gsig.parameters.values())[:-1] + list(fkwargs.values())
        else:
            parameters = list(gsig.parameters.values()) + list(fkwargs.values())
        # Transfer it
        print(parameters)
        g.__signature__ = gsig.replace(parameters=parameters)
        if doc:
            g.__doc__ = f.__doc__
        # Return g
        return g

    return decorator


if "pytest" in sys.modules:
    import pytest


    def func(b: int, c=None, *, d, e=None):
        "A docstring"


    def func2(**kwargs):
        return func(**kwargs)


    def func2_expected(*, b: int, c=None, d, e=None):
        "A docstring"


    @pytest.mark.parametrize(
        "delegatee,delegator,expected",
        [
            (func, func2, func2_expected),
        ],
    )
    def test_delegate(delegatee, delegator, expected):
        delegated = delegate(delegatee)(delegator)
        assert delegated.__doc__ == expected.__doc__
        assert delegated.__doc__ == expected.__doc__
        assert inspect.signature(delegated) == inspect.signature(expected)
