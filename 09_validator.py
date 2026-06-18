# Email validator - Exercise 9 starting point
# PROBLEM: this validation is too weak (it accepts "@" and "a@").
# In the exercise you will write a proper fix on a separate branch, then
# use 'git cherry-pick' to bring ONLY that one fix commit into main.

def is_valid_email(email):
    return "@" in email          # too weak

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("not-an-email"))      # False
print(is_valid_email("@"))                 # True (this is the bug)
