import json
import os

CWD = os.path.dirname(__file__)
# a comment
class Auth:
    def __init__(self, db_path):
        if type(db_path) != str:
            raise ValueError("The db_path has to be an str instance")
        self.db_path = db_path
    
    @property
    def users(self):
        with open(self.db_path, "r", encoding="utf8") as file:
            return json.load(file)["data"]


    def create_user(self, user):
        if type(user) != dict:
            raise ValueError("The user has to be an dictionary instance")
        users = self.users.copy()
        users.append(user)
        with open(self.db_path, "w", encoding="utf8") as file:
            json.dump({"data":users}, file, ensure_ascii=False, indent=4)
    
    @staticmethod
    def create_form():
        user_name = input("Name: ")
        user_pwd = input("PWD: ")

        return {
            "user_name": user_name,
            "user_pwd": user_pwd
        }
    
    def login(self, user_to_log):
        if type(user_to_log) != dict:
            raise ValueError("The user has to be an dictionary instance")
        users = self.users.copy()
        user_exist = next(filter(lambda user: user["user_name"] == user_to_log["user_name"], users), False)
        if user_exist:
            return True if user_to_log["user_pwd"] == user_exist["user_pwd"] else False
    
    @staticmethod
    def login_form():
        user_name = input("Name: ")
        user_pwd = input("PWD: ")

        return {
            "user_name": user_name,
            "user_pwd": user_pwd
        }
        



test = Auth(f"{CWD}/users.json") # test_1
# test_user = test.create_form() # test_2
# test.create_user(test_user) # test_3
test_user = test.login_form()
print(test.login(test_user))
# print(test.users)


























# import datetime as dt
# class Employee:

#     salary_raise = 1.02

#     def __init__(self, name, last, salary):
#         self.name = name
#         self.last = last
#         self.salary = salary
#         self.workdays = []
    
#     def __str__(self):
#         return f"{self.name} - {self.last}"
    
#     @classmethod
#     def set_salary_raise(cls, value):
#         cls.salary_raise = value

#     def get_salary(self):
#         sundays = 0
#         for day in workdays:
#             is_sunday ? += 1
#         return (len(workdays) - sundays) )+ (sundays * (workdays - sundays) * 1.5) 
    
#     @staticmethod
#     def is_sunday():
#         day = dt.date.today()
#         return True if day.isoweekday() == 7 else False        
    
# test = Employee("Vito", "Genovese", 10.30)
# print(test.is_sunday())





    