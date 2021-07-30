class Employee:

    salary_raise = 1.04

    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
    
    def __str__(self):
        return f"Name: {self.name}\nLast: {self.last}"

    def apply_raise(self):
        self.salary *= self.salary_raise

    @classmethod
    def set_salary_raise(cls, value):
        cls.salary_raise = value

class Developer(Employee):
    salary_raise = 1.10
    def __init__(self, name, last, salary, p_language):
        super().__init__(name, last, salary)
        self.p_language = p_language
    
    def __str__(self):
        return f"Name: {self.name}\nLast: {self.last}\nP_lang: {self.p_language}"


nicolas = Employee("Nicolas", "Guzzetti", 10000)
renzo = Developer("Renzo", "Rámirez", 12000, "Python")

# 2010:

print(f"En el 2010 {nicolas.name} cobra {nicolas.salary}€")
print(f"En el 2010 {renzo.name} cobra {renzo.salary}€")

# 2011:

nicolas.apply_raise()
renzo.apply_raise()

print(f"En el 2011 {nicolas.name} cobra {nicolas.salary}€")
print(f"En el 2011 {renzo.name} cobra {renzo.salary}€")

# ¡¡¡¡A partir del 2012 el aumento salarial es del 2%!!!!

# 2012:
print(Employee.salary_raise)
Employee.salary_raise = 1.05
print(Employee.salary_raise)

nicolas.apply_raise()
print(f"En el 2012 {nicolas.name} cobra {nicolas.salary}€")









# print(user_developer)



# class Carro:
#     def __init__(self, caballos):
#         self.caballos = caballos
        
# class Coche:
#     nivel_contaminacion = 10
#     def __init__(self, motor, contaminacion):
#         self.motor = motor
#         self.contaminacion = contaminacion

#     @property
#     def is_legal(self):
#         return True if self.contaminacion <= self.nivel_contaminacion else False

# clio = Coche("Gasolina", 7)
# carro_de_pepe = Carro(2)
# ferrari = Coche("Gasolina", 12)
# peugeot_504 = Coche("Diesel", 20)
# print(clio.is_legal)
# print(ferrari.is_legal)
