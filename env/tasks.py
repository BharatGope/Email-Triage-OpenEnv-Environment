import json

def load_tasks():
    with open("data/emails.json", "r") as f:
        return json.load(f)