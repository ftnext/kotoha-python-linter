import ast


class ArgumentConcreteTypeHintChecker(ast.NodeVisitor):
    def visit_arg(self, node):
        annotation = node.annotation
        if annotation.value.id in {"list", "dict", "set", "tuple"}:
            print(f"Fix at {node.lineno}:{node.col_offset}")
            print(ast.dump(node))
        self.generic_visit(node)


def run(code: str) -> None:
    tree = ast.parse(code)
    ArgumentConcreteTypeHintChecker().visit(tree)
