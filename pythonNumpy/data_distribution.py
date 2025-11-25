# data distribution 
#data distribution is a list of all possible values and how often each value occurs in the dataset.
"""
NumPy Distribution Notes & Practice Code
---------------------------------------
This file explains the most common probability distributions in NumPy
and shows example code for each. You can run this file directly or copy
sections into your notebook.

Distributions covered:
1. Uniform Distribution
2. Normal (Gaussian) Distribution
3. Binomial Distribution
4. Poisson Distribution
5. Exponential Distribution
6. Beta Distribution
7. Gamma Distribution

Each section includes:
- What the distribution is
- When it's used
- Code examples
"""

# Always start by importing numpy
import numpy as np

# -----------------------------------------------------------
# 1. UNIFORM DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Every number in a given interval has the same probability.
- Often used in simulations, randomness, and initializing parameters.

np.random.uniform(low, high, size)
"""

uniform_data = np.random.uniform(0, 1, 10)  # 10 numbers between 0 and 1

# -----------------------------------------------------------
# 2. NORMAL (GAUSSIAN) DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Bell-curve distribution.
- Used in statistics, ML (weights initialization), natural phenomena.

np.random.normal(mean, std_dev, size)
"""

normal_data = np.random.normal(0, 1, 10)  # mean 0, std 1

# -----------------------------------------------------------
# 3. BINOMIAL DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Counts number of successful outcomes.
- Example: flipping a coin 10 times — how many heads?

np.random.binomial(n_trials, probability, size)
"""

binomial_data = np.random.binomial(10, 0.5, 10)  # 10 experiments

# -----------------------------------------------------------
# 4. POISSON DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Measures number of events happening in a fixed interval.
- Example: number of customers arriving per hour.

np.random.poisson(lambda_rate, size)
"""

poisson_data = np.random.poisson(3, 10)  # lambda = 3 events per interval

# -----------------------------------------------------------
# 5. EXPONENTIAL DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Time between events in a Poisson process.
- Example: time between customer arrivals.

np.random.exponential(scale, size)
(scale = 1/lambda)
"""

exponential_data = np.random.exponential(1, 10)

# -----------------------------------------------------------
# 6. BETA DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Used to model probabilities (values between 0 and 1).
- Popular in Bayesian statistics.

np.random.beta(alpha, beta, size)
"""

beta_data = np.random.beta(2, 5, 10)

# -----------------------------------------------------------
# 7. GAMMA DISTRIBUTION
# -----------------------------------------------------------
"""
Definition:
- Used for modeling wait times or lifetime of components.
- Very useful in Bayesian modeling.

np.random.gamma(shape, scale, size)
"""

gamma_data = np.random.gamma(2, 2, 10)

# -----------------------------------------------------------
# PRINT EXAMPLES (optional)
# -----------------------------------------------------------
print("Uniform:", uniform_data)
print("Normal:", normal_data)
print("Binomial:", binomial_data)
print("Poisson:", poisson_data)
print("Exponential:", exponential_data)
print("Beta:", beta_data)
print("Gamma:", gamma_data)
