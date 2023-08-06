from neoteroi.di import ContainerProtocol
from typing import Iterable, Type


class Requirement:
    def authorize(self, context):
        ...


RequirementConf = Requirement | Type[Requirement]


class Policy:
    def __init__(self, requirements: list[RequirementConf]) -> None:
        self.requirements = requirements


class AuthorizationStrategy:
    def __init__(self, policies: list[Policy], container: ContainerProtocol) -> None:
        self.policies = policies
        self.container = container

    def _get_requirements(self, policy: Policy) -> Iterable[Requirement]:
        for obj in policy.requirements:
            if isinstance(obj, Requirement):
                yield obj
            else:
                yield self.container.resolve(obj)

    def authorize(self, context):
        for policy in self.policies:
            ...
