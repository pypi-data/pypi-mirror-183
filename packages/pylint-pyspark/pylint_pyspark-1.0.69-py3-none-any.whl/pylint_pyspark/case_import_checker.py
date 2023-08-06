
import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.checkers.imports import ImportsChecker

class CaseImportChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "import-case-checker"

    priority = -1
    msgs = {
        'C4003': ('pyspark.sql.functions module should be imported as F instead of f',
                  'lower-case-function-import',
                  'Follow AstrumU convention by importing the functions module using capital F.'),
        'C4004': ('pyspark.sql.types module should be imported as T instead of t',
                  'lower-case-type-import',
                  'Follow AstrumU convention by importing the types module using capital T.'),
    }
    def __init__(self, linter):
        super(CaseImportChecker, self).__init__(linter)
        self._check_import_stack = []

    def _check_import(self, node: nodes.Import):
        print(node.names[0][0])
        print(node.names[0][1])
        print(node.names[0][0] == "pyspark.sql.functions")
        print(node.names[0][1] == "f")
        print('------------------------------------------------------')
        if node.names[0][0] == "pyspark.sql.functions" and node.names[0][1] == 'f':
            print('here')
            self.add_message(
                "lower-case-function-import", node=node
            )
        elif node.names[0][0] == "pyspark.sql.types" and node.names[0][1] == 't':
            self.add_message(
                "lower-case-type-import", node=node
            )

    def visit_import(self, node):
        self._check_import_stack.append([])
        

    def leave_import(self, node):
        self._check_import(node)
        self._check_import_stack.pop()