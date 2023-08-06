from typing import Any, Optional

from nolog.logic_engine.predicate import Predicate


class Or(Predicate):
    def __init__(self, *args):
        predicates = args
        self.predicates = predicates

    def eval(self, variable: Optional[Any] = None) -> bool:
        return any(predicate.eval(variable) for predicate in self.predicates)
