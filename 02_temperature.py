# Celsius to Fahrenheit converter - Exercise 2 starting point
# PROBLEM: the conversion formula is wrong (it forgets to add 32).
# You will fix this on a feature branch, then merge the branch into main.

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32      # wrong: should be c * 9 / 5 + 32

print(celsius_to_fahrenheit(0))     # prints 0.0, but should be 32.0
print(celsius_to_fahrenheit(100))   # prints 180.0, but should be 212.0
