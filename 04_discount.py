# Discount calculator - Exercise 4 starting point
# This version is CORRECT. In the exercise you will deliberately make a
# "bad commit" that breaks it, then undo that commit with 'git revert'.

def apply_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price - (price * percent / 100)

print(apply_discount(100, 20))   # 80.0
print(apply_discount(50, 10))    # 45.0
