# -*- coding: utf-8 -*-
"""
This example demonstrates the use of pyqtgraph's parametertree system. This provides
a simple way to generate user interfaces that control sets of parameters. The example
demonstrates a variety of different parameter types (int, float, list, etc.)
as well as some customized parameter types

"""



import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType


params = [
    {'name': 'Integer', 'type': 'int', 'value': 10},
    {'name': 'Float', 'type': 'float', 'value': 10.5, 'step': 0.1},
    {'name': 'String', 'type': 'str', 'value': "hi"},
    {'name': 'List', 'type': 'list', 'values': [1,2,3], 'value': 2},
    {'name': 'Named List', 'type': 'list', 'values': {"one": 1, "two": "twosies", "three": [3,3,3]}, 'value': 2},
    {'name': 'Boolean', 'type': 'bool', 'value': True, 'tip': "This is a checkbox"},
    {'name': 'Color', 'type': 'color', 'value': "FF0", 'tip': "This is a color button"},
    {'name': 'Gradient', 'type': 'colormap'},
    {'name': 'Text Parameter', 'type': 'text', 'value': 'Some text...', "fuck": "shit"},
    {'name': 'Action Parameter', 'type': 'action'}
]

## Create tree of Parameter objects
p = Parameter.create(name='params', type='group', children=params)

## If anything changes in the tree, print a message
def change(param, changes):
    print("tree changes:")
    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        print('  parameter: %s'% childName)
        print('  change:    %s'% change)
        print('  data:      %s'% str(data))
        print('  ----------')

def valueChanging(param, value):
    print("Value changing (not finalized):", param, value)

p.sigTreeStateChanged.connect(change)


pint = p.param('Integer')

pint.setValue(3)
import time
time.sleep(1)
pint.setValue(5)