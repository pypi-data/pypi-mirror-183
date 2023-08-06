from typing import Any, Dict, List, Callable, Optional, cast


class Node:
    @staticmethod
    def of(construct: "Construct") -> "Node":
        return construct.node

    def __init__(
        self, host: "Construct", scope: Optional["Construct"] = None, id: str = ""
    ) -> None:
        self.id = id
        self.scope = scope

        if self.scope != None and self.id == "":
            raise ValueError("Only root constructs may have an empty id")

        self._host = host
        self._locked = False
        self._children: Dict[str, "Construct"] = dict()
        self._validations: List[Callable[[], List[str]]] = list()
        self._context: Dict[str, Any] = dict()

        if scope is not None:
            scope.node._add_child(host, self.id)

    @property
    def children(self) -> List["Construct"]:
        return list(self._children.values())

    @property
    def locked(self) -> bool:
        if self._locked:
            return True

        if self.scope is not None and self.scope.node.locked:
            return True

        return False

    def find_child(self, id: str) -> Optional["Construct"]:
        return self._children.get(id)

    def find_all(self) -> List["Construct"]:
        ret: List["Construct"] = list()

        def visit(c: "Construct") -> None:
            ret.append(c)

            for c in c.node.children:
                visit(c)

        visit(self._host)

        return ret

    def add_validation(self, validate: Callable[[], List[str]]) -> None:
        self._validations.append(validate)

    def validate(self) -> List[str]:
        return [error for validate in self._validations for error in validate()]

    def lock(self) -> None:
        self._locked = True

    def unlock(self) -> None:
        self._locked = False

    def _add_child(self, child: "Construct", id: str) -> None:
        if self.locked:
            raise RuntimeError("Cannot add children")

        self._children[id] = child


class Construct:
    def __init__(self, scope: Optional["Construct"], id: str) -> None:
        self.id = id
        self.node = Node(self, scope, self.id)
