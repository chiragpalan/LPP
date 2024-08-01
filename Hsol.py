import random
import math

# Example Data
deposits = [1000000, 2000000, 1500000]
base_rates = [0.03, 0.035, 0.04]
max_increase = 0.01
budget = 15000
initial_temp = 100
cooling_rate = 0.95
num_iterations = 1000

# Initial Solution
current_solution = [0, 0, 0]
best_solution = current_solution
best_value = sum([d * (r + dr) for d, r, dr in zip(deposits, base_rates, current_solution)])

def calculate_cost(solution):
    # Calculate the total cost of the increased rates
    return sum([d * dr for d, dr in zip(deposits, solution)])

def calculate_value(solution):
    # Calculate the total value (deposits)
    return sum([d * (r + dr) for d, r, dr in zip(deposits, base_rates, solution)])

def get_neighbor(solution):
    # Generate a neighboring solution
    neighbor = solution[:]
    index = random.randint(0, len(solution) - 1)
    change = random.uniform(-max_increase/10, max_increase/10)
    neighbor[index] += change
    neighbor[index] = min(max(neighbor[index], 0), max_increase)  # Ensure within bounds
    return neighbor

# Simulated Annealing Process
temperature = initial_temp
for _ in range(num_iterations):
    new_solution = get_neighbor(current_solution)
    if calculate_cost(new_solution) <= budget:
        new_value = calculate_value(new_solution)
        current_value = calculate_value(current_solution)
        delta = new_value - current_value
        if delta > 0 or math.exp(delta / temperature) > random.random():
            current_solution = new_solution
            if new_value > best_value:
                best_value = new_value
                best_solution = new_solution
    temperature *= cooling_rate

print("Best Solution:", best_solution)
print("Best Value (Total Deposits):", best_value)
print("Total Additional Cost:", calculate_cost(best_solution))
