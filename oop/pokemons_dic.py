elements = ["fire", "grass", "water"]

def create_pokemon(name, element, HP):
    pokemon = {
        "name": name,
        "element": element,
        "HP": HP,
        "attacks": []
    }
    return pokemon

def create_attack(name, element, damage):
    attack = {
        "name": name,
        "element": element,
        "damage":damage
    }
    return attack

def receive_damage(pokemon_a, pokemon_d, attack):
    pokemon_d["HP"] -= attack["damage"]
    if pokemon_d.element == attack.element:
            pokemon_d["HP"] -= attack.damage
        else:
            remain_elements = elements.copy()
            remain_elements.remove(pokemon_d["element"])
            if attack.element == remain_elements[0]:
                pokemon_d["HP"] -= attack.damage * 1.5
            else:
                pokemon_d["HP"] -= attack.damage * 0.5

def learn(pokemon, attack):
    pokemon["attacks"].append(attack)

# Pokemons 
charmander = create_pokemon("Charmander", elements[0], 120)
squirtle = create_pokemon("Squirtle", elements[2], 140)
bulbasaur = create_pokemon("Bulbasaur", elements[1], 160)
# Attacks
flamethrower = create_attack("Flamethrower", elements[0], 40)
razor_leaf = create_attack("Razor leaf", elements[1], 25)
surf = create_attack("Surf", elements[2], 35)

learn(charmander, flamethrower)
print(charmander)

for i, attack in enumerate(charmander["attacks"]):
    print(f"{i + 1}. {attack}")

user = int(input("Choose: "))
receive_damage(charmander, bulbasaur, charmander["attacks"][user - 1])
print(bulbasaur)
