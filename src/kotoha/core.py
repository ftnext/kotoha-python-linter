import ast

KTH101 = (
    "KTH101 "
    "Use abstract type hint by `collections.abc.Iterable` or "
    "`collections.abc.Sequence` "
    "instead of concrete type hint `list`"
)
KTH102 = (
    "KTH102 "
    "Use abstract type hint by `collections.abc.Iterable` or "
    "`collections.abc.Sequence` "
    "instead of concrete type hint `tuple`"
)
KTH103 = (
    "KTH103 "
    "Use abstract type hint by `collections.abc.Iterable` "
    "instead of concrete type hint `set`"
)
KTH104 = (
    "KTH104 "
    "Use abstract type hint by `collections.abc.Iterable` "
    "instead of concrete type hint `dict`"
)

LineNumber = int
ColumnOffset = int
ErrorMessage = str


class ArgumentConcreteTypeHintChecker(ast.NodeVisitor):
    _concrete_type_hint_error_codes: dict[str, ErrorMessage] = {
        "list": KTH101,
        "tuple": KTH102,
        "set": KTH103,
        "dict": KTH104,
    }

    def __init__(self) -> None:
        self.errors: list[tuple[LineNumber, ColumnOffset, ErrorMessage]] = []

    def visit_arg(self, node: ast.arg) -> None:
        if node.annotation is not None:
            annotation: ast.expr = node.annotation
            if (
                hasattr(annotation, "value")
                and annotation.value.id in self._concrete_type_hint_error_codes
            ):
                self.errors.append(
                    (
                        node.lineno,
                        node.col_offset,
                        self._concrete_type_hint_error_codes[
                            annotation.value.id
                        ],
                    )
                )
        self.generic_visit(node)


def run(code: str) -> None:
    tree = ast.parse(code)
    ArgumentConcreteTypeHintChecker().visit(tree)
