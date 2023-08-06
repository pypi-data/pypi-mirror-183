##
# Copyright 2020 Palantir Technologies, Inc. All rights reserved.
# Licensed under the MIT License (the "License"); you may obtain a copy of the
# license at https://github.com/palantir/pyspark-style-guide/blob/develop/LICENSE
##


import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from pylint.checkers.imports import ImportsChecker

class PySparkImportChecker(BaseChecker):
    __implements__ = IAstroidChecker

    name = "import-case-checker"

    priority = -1
    msgs = {
        'C4003': ('pyspark.sql.functions module should be imported as F instead of f',
                  'lower-function-case-import',
                  'Follow AstrumU convention by importing the functions module using capital F.'),
        'C4004': ('pyspark.sql.types module should be imported as T instead of t',
                  'lower-type-case-import',
                  'Follow AstrumU convention by importing the types module using capital T.'),
        'C4005': ("pyspark.sql.functions module shouldn't be imported using wildcard",
                  'wildcard-function-import',
                  'Follow AstrumU convention by importing the functions module using capital F.'),
        'C4006': ("pyspark.sql.types module shouldn't be imported using wildcard",
                  'wildcard-type-import',
                  'Follow AstrumU convention by importing the types module using capital T.'),
    }
    options = ()

    def __init__(self, linter):
        super().__init__(linter)
        self.imports_checker = ImportsChecker(linter)

    def visit_import(self, node):
        """
        copy & paste from ImportsChecker, so it can classify import later
        """
        names = [name for name, _alias in node.names]
        sorted_names = sorted(names)

        # new code in this method - copy & paste from ImportsChecker
        # so it can classify import later
        basename = node.modname
        imported_module = self.imports_checker._get_imported_module(node, basename)

        if isinstance(node.scope(), astroid.Module):
            self.imports_checker._record_import(node, imported_module)
    def _check_function_case(self, node: nodes.Import):
        if "pyspark.sql.function" in node.modname:
            if "*" in node.as_string:
                self.add_message(
                    "wildcard-function-import", node=node
                )
            if "as f" in node.as_string:
                self.add_message(
                    "lower-function-case", node=node
                )
        if "pyspark.sql.types" in node.modname:
            if "*" in node.as_string:
                self.add_message(
                    "wildcard-type-import", node=node
                )
            if "as t" in node.as_string:
                self.add_message(
                    "lower-type-case", node=node
                )

    def leave_module(self, node):
        std_imports, ext_imports, loc_imports = self.imports_checker._check_imports_order(node)
        for group in std_imports, ext_imports, loc_imports:
            self._check_function_case(group)
        
        pass
