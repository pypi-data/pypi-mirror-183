
```python
from contextlib import AbstractContextManager

isinstance(foo_factory(), AbstractContextManager)


def can_be_disposed(obj):
    return isinstance(obj, AbstractContextManager) or hasattr(Disposable, "__enter__") and hasattr(Disposable, "__exit__")


if can_be_disposed(obj):
    # use with, dispose automatically of the object
    ...

```
