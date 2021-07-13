class Animal:

    count = 0

    def set_count():
        Animal.count += 1

    def __init__(self, name):
        self.name = name
        Animal.set_count()
    
    def __str__(self):
        return f"{self.name}"


print(Animal.count)

perro = Animal("Kuga")
print(Animal.count)
gato = Animal("José")


print(Animal.count)