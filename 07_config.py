# Config loader - Exercise 7 starting point
# PROBLEM: running this program creates files that should NOT be committed:
#   - secrets.txt (contains a token)
#   - __pycache__/ (created when Python imports this module)
# You will write a .gitignore so Git stops tracking these files.

API_KEY = "demo-key-please-change"

def save_secret():
    with open("secrets.txt", "w") as f:
        f.write("token=" + API_KEY + "\n")

def load_config():
    return {"debug": True, "api_key": API_KEY}

if __name__ == "__main__":
    save_secret()
    print(load_config())
