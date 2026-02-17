import astroid
import pylint.testutils

import kotoha_plugin


class TestArgumentListTypeHintChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = kotoha_plugin.ArgumentListTypeHintChecker

    def test_find_argument_list_type_hint(self):
        node = astroid.extract_node("""\
def plus_one(numbers: list[int]) -> list[int]:
    return [n + 1 for n in numbers]
""")

        with self.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="avoid-list-arg-type",
                node=node.args.annotations[0],
                args=("list",),
                line=1,
                col_offset=22,
                end_line=1,
                end_col_offset=31,
            )
        ):
            self.checker.visit_arguments(node.args)
