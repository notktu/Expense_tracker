import os
import json

FILE = os.path.join(os.path.dirname(__file__), "data", "accountInfo.json")

def ensure_file_ok():
    os.makedirs(os.path.dirname(FILE), exist_ok=True)

    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def atomic_write(path: str, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)

def get_accountInfo(): # returns a list of dicts of expenses and categories
    ensure_file_ok()
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        # File has bad JSON; reset to empty list
        atomic_write(FILE, [])
        return []


def save_accountInfo(accountInfo): # expects a list of dicts of expenses and categories to save in json file
    atomic_write(FILE, accountInfo)

def add_accountInfo(userName, password): # expects a float amount and a string category to add to the json file
    account = get_accountInfo()
    account.append({"username": userName, "password": password})
    save_accountInfo(account)
    print(f"Added: ${userName} to {password}")

def clear_accountInfo(): # clears all expenses from the json file
    save_accountInfo([])

def verify_login(username: str, password: str) -> tuple[bool, str]:
    u = (username or "").strip()
    p = password or ""
    accounts = get_accountInfo()
    # Find user
    for acc in accounts:
        if acc.get("username") == u:
            if acc.get("password") == p:
                return True, "ok"
            else:
                return False, "incorrect password"
    return False, "no such user"