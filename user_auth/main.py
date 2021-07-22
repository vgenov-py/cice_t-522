import funcs
import datetime
import bcrypt

user = "0"
server_token = None
user_token = None

while user != "q":
    funcs.menu()
    user = input("Choose: ")

    if user == "1": # Create user
        user_name = input("Name: ")
        users = funcs.read_json("users.json")
        users_names = [user["name"] for user in users["data"]]
        try:
            users_names.index(user_name)
            print("El user existe")
        except ValueError:
            user_pwd = input("Password: ")
            new_user = {"name": user_name, "pwd": bcrypt.hashpw(user_pwd.encode(), bcrypt.gensalt()).decode(), "user_since": datetime.date.today().isoformat()}
            users["data"].append(new_user)
            funcs.create_user(users, "users.json")
            
    elif user == "2": # Log in
        user_name = input("Name: ")
        user_pwd = input("Password: ")
        users = funcs.read_json("users.json")
        
        for user in users["data"]:
            if user["name"] == user_name:
                if bcrypt.checkpw(user_pwd.encode(), user["pwd"].encode()):
                    print("Log in!")
                    user_token = {"expired_date": datetime.datetime.today(), "token": bcrypt.hashpw((user_pwd + user_name).encode(), bcrypt.gensalt())}
                    server_token = user_token["token"]
                else:
                    print("User or password incorrect!")

    elif user == "3":
        if user_token:
            if (user_token["expired_date"] + datetime.timedelta(seconds=10)) > datetime.datetime.today():
                if user_token["token"] == server_token:
                    user_new_pwd_1 = input("New password: ")
                    user_new_pwd_2 = input("Repeat password: ")
                    if user_new_pwd_1 == user_new_pwd_2:
                        for user in users["data"]:
                            if user["name"] == user_name:
                                user["pwd"] = bcrypt.hashpw(user_new_pwd_1.encode(), bcrypt.gensalt()).decode()
                                funcs.create_user(users, "users.json")
                    else:
                        print("passwords don't match")