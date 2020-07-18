from PyInquirer import Separator

WELCOME_SCRIPT = '\n Welcome To The Python Polynomial Graphing Interface! \n Graph polynomial functions and their derivatives\n through an entry/selection interface (command-line interface).\n For this program to work properly you must ensure the following:\n - entries must not be left empty and must not contain any letters\n - degree of the polynomial must be a positive integer\n'

START_PROMPT = [
    {
        'type': 'confirm',
        'message': 'Hit Enter Or Y To Start Program',
        'name': 'Start'
    }
]

OPTIONS_PROMPT = [
    {
        'type': 'list',
        'name': 'functions',
        'message': 'Select Any Function Bellow',
        'choices': [
            'Graph Polynomial',
            'Graph Derivative',
            'Graph Second Derivative',
            Separator(),
            'New Polynomial',
            'Exit'
        ]
    },
]