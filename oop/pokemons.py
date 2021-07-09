elements = ["fire", "grass", "water"]

class Pokemon:
    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []
        self.is_alive = True
    
    def __str__(self):
        return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"
    
    def learn(self, attack):
        self.attacks.append(attack)

    def receive_damage(self, attack):
        if self.element == attack.element:
            self.HP -= attack.damage
            self.is_alive = True if self.HP > 0 else False
            # if self.HP < 0:
            #     self.is_alive = False

        else:
            remain_elements = elements.copy()
            remain_elements.remove(self.element)
            if attack.element == remain_elements[0]:
                self.HP -= attack.damage * 1.5
                self.is_alive = True if self.HP > 0 else False

            else:
                self.HP -= attack.damage * 0.5
                self.is_alive = True if self.HP > 0 else False

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
print(charmander.attacks)
squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)


flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 3)

charmander.learn(flamethrower)
print(charmander.attacks)

charmander.learn(razor_leaf)
charmander.learn(surf)
bulbasaur.learn(razor_leaf)
squirtle.learn(surf)

pokemons = [charmander, squirtle, bulbasaur]

