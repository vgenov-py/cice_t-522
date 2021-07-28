import os
import json
CWD = os.path.dirname(__file__)

def menu():
    print("1. Create user")
    print("2. Log in")
    print("3. Change password")
    print("Q. Quit")

def read_json(json_file):
    with open(f"{CWD}/{json_file}", encoding="utf8") as file:
        return json.load(file)

def get_user_by_name(json_file, name):
    users = read_json(json_file)["data"]
    user_to_find = list(filter(lambda user: user["name"] == name,users))
    return user_to_find[0]

def create_user(users, json_file):
    with open(f"{CWD}/{json_file}", "w", encoding="utf8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def create_user_token(user_token, json_file):
    user_token["expired_date"] = user_token["expired_date"].isoformat()
    user_token["token"] = user_token["token"].decode()

    with open(f"{CWD}/{json_file}", "w", encoding="utf8") as file:
        json.dump({"user_session": user_token}, file, ensure_ascii=False, indent=4)

