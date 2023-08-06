A tiny utility for preserving signature information (parameter names, annotations, and docstrings) when delegating one function to another.

# Usage

```python
from delegatefn import delegate
import inspect


def foo(a, b, c):
    """This is the docstring for foo."""
    pass


@delegate(foo)
def bar(a, b, c):
    pass


assert inspect.signature(bar) == inspect.signature(foo)

print(inspect.signature(bar))
# (a, b, c)
```