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
    8006.664 * x1,
    12045 * x3,
    16160 * x6,
    20600 * x12
])
problem += objective

# Define the budget constraint
budget_constraint = lpSum([
    500 * x1,
    750 * x3,
    1000 * x6,
    1250 * x12
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
