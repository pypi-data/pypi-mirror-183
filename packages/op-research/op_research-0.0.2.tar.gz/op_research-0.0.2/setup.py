# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['op_research']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'op-research',
    'version': '0.0.2',
    'description': 'package for solving operational research problems',
    'long_description': "# OP-Research\n\nA unified collection of algrithms for solving operational research problems in an effiecient way\n\n#### Purpose of the Package\nThe purpose of the package is to provide a collection of tools to solve operation research problems and help researchers.\n### Features\nThe current implementation uses two phase method and is able to identify case for Infeasible solution, Unbounded solution, Degeneracy and Alternate Solution. In case of Infeasible solution and Unbounded solution it raises an ValueError and in case of Degeneracy and Alternate Solution it gives a warning and returns a optimum solution.\n\nThe constraints right hand side should be positive and all variables should hold non-negativity conditions.\n\n## Rules for constraint representation:\n\nEach variable should have coefficient if it is in constraint i.e x_1 is not allowd instead use 1x_1. Note that it is not necessary to represent each variable in a constraint, but if a variable is there then it should have a coefficient.\nOnly single spaces should be used.\nFor a variable x_i i should be an integer in [1, num_vars], where num_vars is number of variables\nObjective function should be a tuple with first element as objective ie to maximize or minimize and second element should value that is to be optimized.\n\nSimplex solution solver\nThe package can be found on pypi hence you can install it using pip\n\n## Installation\n```\npip install op_research\n```\n### Usage\n\n```\n>>> from op_research import Simplex\n>>> objective = ('maximize', '7x_1 + 4x_2')\n>>> constraints = ['5x_1 + 2x_2 = 7', '1x_1 + 8x_2 >= 9', '3x_1 + 4x_2 <= 8']\n>>> Lp_system = Simplex(num_vars=2, constraints=constraints, objective_function=objective)\n>>> print(Lp_system.solution)\n{'x_1': Fraction(6, 7), 'x_2': Fraction(19, 14)}\n```\n\n\n## Contribution\nContributions are welcome Notice a bug let us know. Thanks\n\n### Author\nMain Maintainer: Rehan Ahmed\n",
    'author': 'rehan ahmed',
    'author_email': 'rehanahmedahmed007@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Rehan-stack/op-research',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
