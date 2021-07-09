from pokemons import *
import random

print("POKEMON".center(50, "-"))
print("Oak: Select your first pokemon...")
[print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
pokemons.remove(pokemon_a)
pokemon_d = random.choice(pokemons)

while pokemon_d.is_alive:
    for i, attack in enumerate(pokemon_a.attacks):
        print(f"{i + 1}. {attack.name}")
    user = int(input("Choose an attack: ")) - 1
    pokemon_d.receive_damage(pokemon_a.attacks[user])
    print(f"{pokemon_d.name} recibió {pokemon_a.attacks[user].damage} de daño!")

print("EL pokemon murió")


