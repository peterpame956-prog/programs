# Inventory tracker - Exercise 6 starting point
# PROBLEM: you will start building a new feature (remove_item), but an urgent
# bug on main needs fixing first. You will 'git stash' your half-done work,
# fix the bug, then restore the work with 'git stash pop'.
#
# Urgent bug to fix during the exercise: add_item should reject negative qty.

inventory = {"apples": 10, "bananas": 5}

def add_item(name, qty):
    inventory[name] = inventory.get(name, 0) + qty   # accepts negative qty (bug)

def total_items():
    return sum(inventory.values())

add_item("apples", 3)
print(total_items())   # 18
