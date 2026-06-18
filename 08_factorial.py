# Factorial - Exercise 8 starting point
# PROBLEM: you will commit this file with (a) a typo in the commit message and
# (b) a forgotten file (README.txt). You will use 'git commit --amend' to fix
# the message AND include the forgotten file in the same commit.

def factorial(n):
    if n < 0:
        raise ValueError("n must be zero or positive")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
