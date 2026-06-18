# Word counter - Exercise 5 starting point
# This version is clean. In the exercise you will add messy debug code,
# commit it by mistake, then use 'git reset' to undo the commit.

def count_words(text):
    print("DEBUG:", text)
    return len(text.split())
print(count_words("git is a version control system"))   # 6
