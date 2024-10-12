import ast

KTH000 = (
    "KTH000 "
    "concrete type (`list`, `dict`, `set`, `tuple`) in function parameters, "
    "use abstract type (`Iterable`, `Sequence` or `Mapping` "
    "from `collections.abc`)"
)
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

LineNumber = int
ColumnOffset = int
ErrorMessage = str


class ArgumentConcreteTypeHintChecker(ast.NodeVisitor):
    def __init__(self) -> None:
        self.errors: list[tuple[LineNumber, ColumnOffset, ErrorMessage]] = []

    def visit_arg(self, node: ast.arg) -> None:
        if node.annotation is not None:
            annotation: ast.expr = node.annotation
            if hasattr(annotation, "value"):
                if annotation.value.id == "list":
                    self.errors.append((node.lineno, node.col_offset, KTH101))
                elif annotation.value.id == "tuple":
                    self.errors.append((node.lineno, node.col_offset, KTH102))
                elif annotation.value.id == "set":
                    self.errors.append((node.lineno, node.col_offset, KTH103))
                elif annotation.value.id in {"dict"}:
                    self.errors.append((node.lineno, node.col_offset, KTH000))
        self.generic_visit(node)


def run(code: str) -> None:
    tree = ast.parse(code)
    ArgumentConcreteTypeHintChecker().visit(tree)
