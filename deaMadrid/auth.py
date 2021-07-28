import auth_dep
import datetime
import bcrypt

def auth():
    user = "0"
    server_token = None
    user_token = None

    while user != "q":
        auth_dep.menu()
        user = input("Choose: ")

        if user == "1": # Create user
            user_name = input("Name: ")
            users = auth_dep.read_json("users.json")
            users_names = [user["name"] for user in users["data"]]
            try:
                users_names.index(user_name)
                print("El user existe")
            except ValueError:
                user_pwd = input("Password: ")
                new_user = {"name": user_name, "pwd": bcrypt.hashpw(user_pwd.encode(), bcrypt.gensalt()).decode(), "user_since": datetime.date.today().isoformat()}
                users["data"].append(new_user)
                auth_dep.create_user(users, "users.json")
                
        elif user == "2": # Log in
            user_name = input("Name: ")
            user_pwd = input("Password: ")
            users = auth_dep.read_json("users.json")
            user_not_found = True
            for user in users["data"]:
                if user["name"] == user_name:
                    user_not_found = False
                    if bcrypt.checkpw(user_pwd.encode(), user["pwd"].encode()):
                        print("Log in!")
                        user_token = {"name": user["name"], "expired_date": datetime.datetime.today(), "token": bcrypt.hashpw((user_pwd + user_name).encode(), bcrypt.gensalt())}
                        auth_dep.create_user_token(user_token, "cookies.json") # cookies
                        user["token"]= user_token["token"] # saving into users.json
                        auth_dep.create_user(users, "users.json") # saving into users.json
                        server_token = user_token["token"]
                    else:
                        print("User or password incorrect!")
            if user_not_found:
                print("User not found")
            

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
                                    auth_dep.create_user(users, "users.json")
                        else:
                            print("passwords don't match")

def validation():
    user_token = auth_dep.read_json("cookies.json")["user_session"]
    print(user_token)
    server_token = auth_dep.get_user_by_name("users.json" ,user_token["name"])["token"]
    print(server_token)
    if user_token:
        if (datetime.datetime.fromisoformat(user_token["expired_date"]) + datetime.timedelta(seconds=60)) > datetime.datetime.today():
            print("Date")
            if user_token["token"] == server_token:
                print("Equal between user and server")
                return user_token
