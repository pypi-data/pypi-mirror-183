from neoteroi.di import Container


class Disposable:
    def __init__(self) -> None:
        self.entered = False
        self.disposed = False

    def __enter__(self):
        print(f"{self.__class__.__name__} entered...")
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.__class__.__name__} disposed...")
        self.disposed = True


class Disposable1(Disposable):
    ...


class Disposable2(Disposable):
    ...


class Disposable3(Disposable):
    ...


container = Container()
container.add_singleton(Disposable1)

disposable = container.resolve(Disposable1)

assert disposable.entered is False
assert disposable.disposed is False

with disposable:
    assert disposable.entered is True
    assert disposable.disposed is False

assert disposable.disposed is True
