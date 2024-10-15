import ast
from typing import cast

KTH101 = (
    "KTH101 "
    "Type hint with abstract type `collections.abc.Iterable` or "
    "`collections.abc.Sequence`, "
    "instead of concrete type `list`"
)
KTH102 = (
    "KTH102 "
    "Type hint with abstract type `collections.abc.Iterable` or "
    "`collections.abc.Sequence`, "
    "instead of concrete type `tuple`"
)
KTH103 = (
    "KTH103 "
    "Type hint with abstract type `collections.abc.Iterable`"
    "instead of concrete type `set`"
)
KTH104 = (
    "KTH104 "
    "Type hint with abstract type `collections.abc.Iterable`"
    "instead of concrete type `dict`"
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

    @staticmethod
    def is_annotated_with_subscript(arg: ast.arg) -> bool:
        if arg.annotation is None:
            return False
        # arg.annotation(: ast.expr) is
        # ast.Name, ast.Subscript or ast.Attribute.
        return isinstance(arg.annotation, ast.Subscript)

    def visit_arg(self, node: ast.arg) -> None:
        if self.is_annotated_with_subscript(node):
            annotation = cast(ast.Subscript, node.annotation)
            value_node = annotation.value
            assert isinstance(value_node, ast.Name)
            if value_node.id in self._concrete_type_hint_error_codes:
                self.errors.append(
                    (
                        node.lineno,
                        node.col_offset,
                        self._concrete_type_hint_error_codes[value_node.id],
                    )
                )
        self.generic_visit(node)


def run(code: str) -> None:
    tree = ast.parse(code)
    ArgumentConcreteTypeHintChecker().visit(tree)
