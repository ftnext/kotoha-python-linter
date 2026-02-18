import ast


class ArgumentListTypeHintChecker(ast.NodeVisitor):
    def __init__(self):
        self.violations = []

    def visit_arg(self, node):
        annotation = node.annotation
        if annotation.value.id == "list":
            as_is = f"{node.arg}: {annotation.value.id}[{annotation.slice.id}]"
            message = f"Fix type hint `{as_is}`"
            self.violations.append((node.lineno, node.col_offset, message))
        self.generic_visit(node)
