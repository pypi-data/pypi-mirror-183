import abc
import dataclasses
from typing import Any, List, Optional


@dataclasses.dataclass
class Predicate(abc.ABC):
    accepted_values: List[Any] = dataclasses.field(default_factory=list)

    @abc.abstractmethod
    def eval(self, variable: Optional[Any] = None) -> bool:
        raise NotImplementedError
