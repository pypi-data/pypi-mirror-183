from neoteroi.di import Container
from collections.abc import Iterator
from contextlib import contextmanager


class Foo:
    def __init__(self) -> None:
        self.disposed = False


@contextmanager
def foo_factory() -> Iterator[Foo]:
    foo = Foo()
    try:
        yield foo
    finally:
        foo.disposed = True


container = Container()
container.add_transient_by_factory(foo_factory)

disposable = container.resolve(Iterator[Foo])

with disposable as foo:
    assert isinstance(foo, Foo)
    assert foo.disposed is False

assert foo.disposed is True
