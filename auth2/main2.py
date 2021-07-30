class Employee:
    salary_raise = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
    
    def __str__(self):
        return f"Name: {self.name}\nLast: {self.last}"

class Developer(Employee):
    def __init__(self, name, last, salary, p_language):
        super().__init__(name, last, salary)
        self.p_language = p_language
    
    def __str__(self):
        return f"Name: {self.name}\nLast: {self.last}\nP_lang: {self.p_language}"

user_employee = Employee("Kevin", "Smith", 10000)
user_developer = Developer("Pedro", "Rámirez", 12000, "Python")
print(user_employee.salary)
print(user_developer)


