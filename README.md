# LPP
Optimization problem 

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Define the problem
problem = LpProblem("TD_Balance_Optimization", LpMaximize)

# Define decision variables
x1 = LpVariable("x1", lowBound=0, upBound=1, cat='Continuous')
x3 = LpVariable("x3", lowBound=0, upBound=1, cat='Continuous')
x6 = LpVariable("x6", lowBound=0, upBound=1, cat='Continuous')
x12 = LpVariable("x12", lowBound=0, upBound=1, cat='Continuous')

# Define the objective function
objective = lpSum([
    8{,}006.664 * x1,
    12{,}045 * x3,
    16{,}160 * x6,
    20{,}600 * x12
])
problem += objective

# Define the budget constraint
budget_constraint = lpSum([
    500 * x1,
    750 * x3,
    1{,}000 * x6,
    1{,}250 * x12
]) <= 500
problem += budget_constraint

# Solve the problem
problem.solve()

# Print the results
print(f"Optimal x1: {x1.varValue}")
print(f"Optimal x3: {x3.varValue}")
print(f"Optimal x6: {x6.varValue}")
print(f"Optimal x12: {x12.varValue}")
print(f"Optimal objective value: {problem.objective.value()}")
