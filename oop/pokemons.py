elements = ["fire", "grass", "water"]

class Pokemon:
    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []
    
    def __str__(self):
        return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"
    
    def learn(self, attack):
        self.attacks.append(attack)

class Attack:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
    



charmander = Pokemon("Charmander", elements[0], 120)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)


flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor leaf", elements[1], 25)
surf = Attack("surf", elements[2], 35)
charmander.learn(flamethrower)
charmander.learn(razor_leaf)
charmander.learn(surf)

# print(flamethrower)
print(charmander)



# print(charmander)
# print(squirtle)
# print(bulbasaur)

