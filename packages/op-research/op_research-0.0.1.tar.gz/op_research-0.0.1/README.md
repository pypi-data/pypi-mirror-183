# OP-Research

A unified collection of algrithms for solving operational research problems in an effiecient way

#### Purpose of the Package
The purpose of the package is to provide a collection of tools to solve operation research problems and help researchers.
### Features
The current implementation uses two phase method and is able to identify case for Infeasible solution, Unbounded solution, Degeneracy and Alternate Solution. In case of Infeasible solution and Unbounded solution it raises an ValueError and in case of Degeneracy and Alternate Solution it gives a warning and returns a optimum solution.

The constraints right hand side should be positive and all variables should hold non-negativity conditions.

## Rules for constraint representation:

Each variable should have coefficient if it is in constraint i.e x_1 is not allowd instead use 1x_1. Note that it is not necessary to represent each variable in a constraint, but if a variable is there then it should have a coefficient.
Only single spaces should be used.
For a variable x_i i should be an integer in [1, num_vars], where num_vars is number of variables
Objective function should be a tuple with first element as objective ie to maximize or minimize and second element should value that is to be optimized.

Simplex solution solver
The package can be found on pypi hence you can install it using pip

## Installation
pip install op_research
### Usage


>>> from op_research import Simplex
>>> objective = ('maximize', '7x_1 + 4x_2')
>>> constraints = ['5x_1 + 2x_2 = 7', '1x_1 + 8x_2 >= 9', '3x_1 + 4x_2 <= 8']
>>> Lp_system = Simplex(num_vars=2, constraints=constraints, objective_function=objective)
>>> print(Lp_system.solution)
{'x_1': Fraction(6, 7), 'x_2': Fraction(19, 14)}



## Contribution
Contributions are welcome Notice a bug let us know. Thanks

### Author
Main Maintainer: Rehan Ahmed
