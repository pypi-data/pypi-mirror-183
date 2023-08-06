from typing import Any

from nolog.logic_engine.predicate import Predicate


class Truthy(Predicate):

    def eval(self, variable: Any = None) -> bool:
        return True


class Falsy(Predicate):
    def eval(self, variable: Any = None) -> bool:
        return False
