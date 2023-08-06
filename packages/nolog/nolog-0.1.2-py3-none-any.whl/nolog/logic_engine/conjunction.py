from typing import Any, Optional


class And:
    def __init__(self, *args):
        predicates = args
        self.predicates = predicates

    def eval(self, variable: Optional[Any] = None) -> bool:
        return all(predicate.eval(variable) for predicate in self.predicates)
