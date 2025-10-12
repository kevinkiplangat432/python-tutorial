# 🐍 Python Mastery Roadmap — From Core to Data Science

> **Author:** Kevin Kiplangat  
> **Goal:** Build deep, practical mastery of Python — from fundamentals to libraries like `pandas`, `numpy`, and `matplotlib`.

---

## 📘 Overview

This repository is a **personal learning playground** for mastering Python.  
It’s divided into **two phases**:

1. **Core Python Refresher** — Deep understanding of syntax, logic, and language behavior.
2. **Data Science Foundations** — Building with Python’s scientific libraries.

Every file, exercise, and experiment here aims to help you not just write Python — but *think like Python.*

---

## 🧩 Structure

### 🥇 **Phase 1: Core Python Refresher**

Folder: `python_basics/`

Covers 15 essential topics:

| # | Topic | Description |
|---|--------|-------------|
| 1 | Variables | Declaration, scope, global/local usage |
| 2 | Data Types | Numbers, strings, lists, tuples, sets, dicts |
| 3 | Casting | Type conversions and pitfalls |
| 4 | Numbers | Arithmetic, rounding, power, random |
| 5 | Strings | Slicing, formatting, concatenation, methods |
| 6 | Booleans | Logic, truthiness, conditions |
| 7 | Operators | Arithmetic, comparison, bitwise, precedence |
| 8 | Lists | Manipulation, comprehension, sorting, joining |
| 9 | Tuples | Access, unpacking, immutability |
| 10 | Sets | Unique data, operations, methods |
| 11 | Dictionaries | Key-value pairs, nesting, updates |
| 12 | If / Else | Conditional logic and branching |
| 13 | While Loops | Controlled iteration and break logic |
| 14 | For Loops | Iteration patterns and nesting |
| 15 | Functions | Definition, return values, scope |

Each topic contains:
- Short coding challenges (7 per topic for #1–#7)
- One integrated test for #8–#15

---

### 🧠 **Phase 2: Data Science Kickoff**

Folder: `data_science_basics/`

Start exploring libraries commonly used for analytics:

| Library | Purpose |
|----------|----------|
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computing and arrays |
| **matplotlib** | Visualization and plotting |
| **seaborn** | Statistical graphics |
| **scipy** | Scientific computations |
| **jupyterlab** | Interactive notebooks for analysis |

Example starter script:

```python
import pandas as pd

# Load datasets
abalone = pd.read_csv("abalone/abalone.data", header=None)
iris = pd.read_csv("iris/iris.data", header=None,
                   names=["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"])

# Explore data
print("Abalone dataset:")
print(abalone.head())

print("\nIris dataset:")
print(iris.head())

# Quick plot
iris.plot(kind="scatter", x="Sepal.Length", y="Petal.Length", title="Iris Scatter Plot")
