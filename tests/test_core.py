from textwrap import dedent

from kotoha.core import run


def test_引数の型ヒントをlistにしてはいけません(capsys):
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

    run(code)

    actual = capsys.readouterr().out
    expected = """\
Fix at 6:16
arg(arg='numbers', annotation=Subscript(value=Name(id='list', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load()))
"""  # NOQA: E501
    assert actual == expected
