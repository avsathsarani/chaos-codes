import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Parameters
r = 4  # Parameter for logistic map, chaotic region
n_steps = 100  # Number of time steps
epsilon = 1e-8  # Small difference in initial conditions

# Initial conditions (two nearby starting values)
x1 = np.random.random()
x2 = x1 + epsilon

# Arrays to store the evolution of the system
x1_values = np.zeros(n_steps)
x2_values = np.zeros(n_steps)
delta_values = np.zeros(n_steps)

# Calculate the evolution of the two nearby initial conditions
for i in range(n_steps):
    x1_values[i] = x1
    x2_values[i] = x2
    delta_values[i] = abs(x1 - x2)
    x1 = logistic_map(x1, r)
    x2 = logistic_map(x2, r)

# Logarithm of the difference
log_delta_values = np.log(delta_values)

# Perform a linear fit to determine the Lyapunov exponent
fit_range = slice(10, 50)  # Ignore initial transient period
slope, intercept = np.polyfit(np.arange(n_steps)[fit_range], log_delta_values[fit_range], 1)
lambda_exp = slope
K = np.exp(intercept)

# Plotting ln(Δ) vs. step number with intercept and slope
plt.figure(figsize=(10, 5))
plt.plot(range(n_steps), log_delta_values, label='ln(Δ)', color='blue')
plt.plot(
    np.arange(n_steps)[fit_range],
    slope * np.arange(n_steps)[fit_range] + intercept,
    label=f"Fit: slope={lambda_exp:.4f}, intercept={intercept:.4f}",
    color='red',
    linestyle='--'
)
plt.xlabel('Step number (n)')
plt.ylabel('ln(Δ)')
plt.title('ln(Δ) vs. Step number with Linear Fit')
plt.legend()
plt.grid(True)
plt.show()
