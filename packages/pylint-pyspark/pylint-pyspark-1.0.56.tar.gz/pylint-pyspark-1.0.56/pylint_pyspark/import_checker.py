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
        super(PySparkImportChecker, self).__init__(linter)
        self._check_import = []
        self._check_importfrom = []

    def _check_importfrom(self, node: nodes.Import):
        if node.modname == "pyspark.sql.function" and node.names[0][0] == '*':
            self.add_message(
                "wildcard-function-import", node=node
            )
        if node.modname == "pyspark.sql.types" and node.names[0][0] == '*':
            self.add_message(
                "wildcard-type-import", node=node
            )

    def _check_import(self, node: nodes.Import):
        print(node.names[0])
        if node.names[0] == "pyspark.sql.function" and node.names[0][0] == 'f':
            self.add_message(
                "lower-function-case", node=node
            )
        if node.names[0] == "pyspark.sql.types" and node.names[0][0] == 't':
            self.add_message(
                "lower-type-case", node=node
            )

    def visit_import(self, node):
        self._check_import.append(node)
    
    def visit_importfrom(self, node):
        self._check_importfrom.append(node)

    def leave_import(self, node):
        self._check_import.pop()
        
    def leave_importfrom(self, node):
        self._check_importfrom.pop()
