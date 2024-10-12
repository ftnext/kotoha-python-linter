import ast
from collections.abc import Generator
from typing import Any, Type

import kotoha


class Flake8KotohaPlugin:
    name = "flake8-kotoha"
    version = kotoha.__version__

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]:
        yield (1, 0, "KTH kawaiine", type(self))
