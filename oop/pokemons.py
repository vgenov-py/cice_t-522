elements = ["fire", "grass", "water"]

class Pokemon:
    count = 0

    @classmethod
    def set_count(cls):
        cls.count += 1

    def __init__(self, name, element, HP):
        self.name = name
        self.element = element
        self.HP = HP
        self.attacks = []
        self.is_alive = True
        self.exp = 10
        Pokemon.set_count()
    
    @property
    def damage(self):
        return self.exp * 0.11

    @property
    def stamina():
        return self.damage * self.exp
    


    def __str__(self):
        return f"name: {self.name}\ntype: {self.element}\nHP: {self.HP}\nattacks: {self.attacks}"
    
    def learn(self, attack):
        self.attacks.append(attack)

    def receive_damage(self, attack, damage_rate):
        if self.element == attack.element:
            self.HP -= attack.damage * damage_rate
            self.is_alive = True if self.HP > 0 else False

        else:
            remain_elements = elements.copy()
            remain_elements.remove(self.element)
            if attack.element == remain_elements[0]:
                self.HP -= (attack.damage * damage_rate) * 1.5
                self.is_alive = True if self.HP > 0 else False

            else:
                self.HP -= (attack.damage * damage_rate) * 0.5
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

squirtle = Pokemon("Squirtle", elements[2], 140)
bulbasaur = Pokemon("Bulbasaur", elements[1], 160)


flamethrower = Attack("Flamethrower", elements[0], 40)
razor_leaf = Attack("Razor leaf", elements[1], 25)
surf = Attack("Surf", elements[2], 3)

charmander.learn(flamethrower)
charmander.learn(razor_leaf)
charmander.learn(surf)
bulbasaur.learn(razor_leaf)
squirtle.learn(surf)


print(charmander.damage)
# print(squirtle.HP)
squirtle.receive_damage(charmander.attacks[0], charmander.damage)
# print(squirtle.HP)

pokemons = [charmander, squirtle, bulbasaur]

# print(Pokemon.count)

