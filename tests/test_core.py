import ast
from textwrap import dedent
from unittest.mock import ANY

from kotoha.core import ArgumentConcreteTypeHintChecker


def test_ArgumentConcreteTypeHintChecker() -> None:
    code = dedent(
        """\
    from collections.abc import Iterable

    print("Hello, world!")


    def plus_one_ng(numbers: list[int]) -> list[int]:
        return [n + 1 for n in numbers]


    def plus_one_ok(numbers: Iterable[int]) -> list[int]:
        return [n + 1 for n in numbers]
    """
    )

    checker = ArgumentConcreteTypeHintChecker()
    checker.visit(ast.parse(code))

    assert len(checker.errors) == 1
    assert checker.errors[0] == (6, 16, ANY)
    assert checker.errors[0][2].startswith("KTH000")
