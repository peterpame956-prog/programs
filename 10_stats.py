# Stats helper - Exercise 10 starting point
# PROBLEM: you will add a new function, commit it, then accidentally throw the
# commit away with 'git reset --hard'. You will recover the lost commit using
# 'git reflog' and 'git reset'.

def mean(numbers):
    return sum(numbers) / len(numbers)

print(mean([2, 4, 6]))   # 4.0
