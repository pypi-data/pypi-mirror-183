"""
POC to investigate automatic handling of contexts.
"""
from contextlib import AbstractContextManager
from typing import cast, Generic, Type, TypeVar, Protocol

T = TypeVar("T", covariant=True)
ContextT = TypeVar("ContextT", bound=AbstractContextManager)
KT = TypeVar("KT")


class ActivationScope:
    def __init__(self) -> None:
        self.entered = False
        self.disposed = False
        self.activated_services: list = []
        self.scoped_services: dict = {}
        self.contexts: list[AbstractContextManager] = []

    def enter(self, obj: AbstractContextManager):
        obj.__enter__()
        self.contexts.append(obj)

    def __enter__(self):
        print(f"{self.__class__.__name__} entered...")
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.__class__.__name__} disposed...")
        self.disposed = True

        for context in self.contexts:
            context.__exit__(exc_type, exc_val, exc_tb)


class TypeActivator(Generic[T], Protocol):
    def activate(self, scope: ActivationScope) -> T:
        ...


class TransientTypeActivator(TypeActivator[T]):
    def __init__(self, type: Type[T]):
        self._type = type

    def activate(self, scope: ActivationScope) -> T:
        return self._type()


class ScopedTypeActivator(TypeActivator[T]):
    def __init__(self, type: Type[T], base_activator: TypeActivator[T]) -> None:
        self._type = type
        self._base_activator = base_activator

    def activate(self, scope: ActivationScope) -> T:
        try:
            return scope.scoped_services[self._type]
        except KeyError:
            instance = self._type()
            scope.scoped_services[self._type] = instance
            return instance


class ContextTypeActivator(TypeActivator[ContextT]):
    # ??????????????????????????????????????????????
    def __init__(
        self, type: Type[ContextT], base_activator: TypeActivator[ContextT]
    ) -> None:
        self._type = type
        self._base_activator = base_activator

    def activate(self, scope: ActivationScope) -> ContextT:
        instance = self._base_activator.activate(scope)
        scope.contexts.append(instance)
        instance.__enter__()
        return instance


class Container(Generic[KT]):
    def __init__(self) -> None:
        self._map: dict[Type[KT], TypeActivator[KT]] = {}

    def register(self, type: Type[KT]):
        self._map[type] = TransientTypeActivator(type)

    def resolve(self, type: Type[KT], scope: ActivationScope | None = None) -> KT:
        if scope is None:
            owned_scope = True
            scope = ActivationScope()
            scope.__enter__()
        else:
            owned_scope = False

        # TODO: enter automatically!
        # TODO: exit automatically!
        # TODO: dispose automatically!
        instance = self._map[type].activate(scope)
        if not owned_scope and isinstance(instance, AbstractContextManager):
            scope.enter(instance)
        return cast(KT, instance)

    def scope(self) -> ActivationScope:
        return ActivationScope()


####
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


container = Container()
container.register(Disposable1)
container.register(Disposable2)
container.register(Disposable3)

disposable = container.resolve(Disposable1)
# not entered because no scope was provided
assert disposable.entered is False
assert disposable.disposed is False


services = []

with container.scope() as scope:
    for service_type in [Disposable1, Disposable2, Disposable3]:
        disposable = container.resolve(service_type, scope)
        services.append(disposable)
        # ?????????????????????????????????????????????????
        # entered because a scope was provided
        # Because Python also supports async disposables (__aenter__, __aexit__),
        # the code API would need to be asynchronous to support them. ????
        # ?????????????????????????????????????????????????
        assert disposable.entered is True
        assert disposable.disposed is False

for disposable in services:
    assert disposable.entered is True
    assert disposable.disposed is True


try:
    with container.scope() as scope:
        for service_type in [Disposable1, Disposable2, Disposable3]:
            disposable = container.resolve(service_type, scope)
            services.append(disposable)
            assert disposable.entered is True
            assert disposable.disposed is False

        raise RuntimeError("Crash test")
except RuntimeError:
    pass


for disposable in services:
    assert disposable.entered is True
    assert disposable.disposed is True

# TODO: ha senso questo per DI?
# async with container.async_scope() as scope:
#     # ??????
#     service = await container.resolve(service_type, scope)
#
