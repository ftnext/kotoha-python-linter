import argparse
import ast
import importlib
from collections.abc import Iterable
from pathlib import Path


def _load_rule(rule_spec: str) -> type[ast.NodeVisitor]:
    """Load a rule class from MODULE:CLASS specification."""
    module_name, class_name = rule_spec.split(":", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def _run_rules_for_file(
    filename: str, source: str, rule_classes: list[type[ast.NodeVisitor]]
) -> list[str]:
    tree = ast.parse(source, filename=filename)
    total_violations = []
    for rule_cls in rule_classes:
        visitor = rule_cls()
        visitor.visit(tree)
        total_violations.extend((filename, *v) for v in visitor.violations)
    return total_violations


def run(
    files: Iterable[Path], rule_classes: Iterable[type[ast.NodeVisitor]]
) -> list[str]:
    rule_classes = list(rule_classes)
    all_violations = []
    for file in files:
        source = file.read_text("utf8")
        all_violations.extend(_run_rules_for_file(file.name, source, rule_classes))
    return all_violations


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tiny AST linter")
    parser.add_argument("files", type=Path, nargs="+", help="Python files to lint")
    parser.add_argument(
        "--rule",
        action="append",
        required=True,
        metavar="MODULE:CLASS",
        help="Rule class to load (repeatable)",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    rule_classes = [_load_rule(rule_spec) for rule_spec in args.rule]
    violations = run(args.files, rule_classes)

    for violation in violations:
        print(f"{violation[0]}:{violation[1]}:{violation[2]}: {violation[3]}")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
