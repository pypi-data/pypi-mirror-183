from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class ModuleDisplayChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "module-display"
    priority = -1
    msgs = {
        "C4006": (
            "Production notebooks should not contain .display() or display() calls.",
            "module-contains-display",
            "Consider using proper logging tools instead of calling .display() or display().",
        ),
    }

    def is_line_split(self, function):
        line = function.lineno
        for arg in function.args.args:
            if arg.lineno != line:
                return True
        return False

    def __init__(self, linter=None):
        super(ModuleDisplayChecker, self).__init__(linter)
        self._function_stack = []

    def module_contains_display(node):
        contains_func_attribute = hasattr (node, "func")
        contains_attrname = hasattr(node.func, "attrname")
        contains_display_attr = node.func.attrname == "display"
        contains_display_func = node.func.name == "display"
        return (contains_func_attribute and contains_attrname and contains_display_attr) or (contains_func_attribute and contains_display_func)

    def visit_functiondef(self, node):
        self._function_stack.append([])

    def visit_expr(self, node):
        if module_contains_display(node):
            self.add_message("module-contains-display", node=node)

    def leave_functiondef(self, node):
        self._function_stack.pop()
