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
            "Calling .display() or display() can clutter the module when running a pipeline.",
        ),
    }

    def __init__(self, linter=None):
        super(ModuleDisplayChecker, self).__init__(linter)
        self._function_stack = []
        
    def visit_functiondef(self, node):
        self._function_stack.append([])

    def visit_expr(self, node):
        contains_func_attribute = hasattr (node, "func")
        contains_attrname = hasattr(node.func, "attrname")
        contains_display_attr = node.func.attrname == "display"
        contains_display_func = node.func.name == "display"
        if (contains_func_attribute and contains_attrname and contains_display_attr) or (contains_func_attribute and contains_display_func):
            self.add_message("module-contains-display", node=node)

    def leave_functiondef(self, node):
        self._function_stack.pop()
