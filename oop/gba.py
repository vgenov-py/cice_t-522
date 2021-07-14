from pokemons import *
from funcs import *
import random

print("POKEMON".center(50, "-"))
print("Oak: Select your first pokemon...")
[print(f"{i+1}. {pokemon.name}") for i, pokemon in enumerate(pokemons)]
user = int(input("Choose: ")) - 1
pokemon_a = pokemons[user]
pokemons.remove(pokemon_a)
pokemon_d = random.choice(pokemons)
total = pokemon_d.HP

while pokemon_a.is_alive and pokemon_d.is_alive:
    print_attacks(pokemon_a)
    user = int(input("Choose an attack: ")) - 1
    before_HP = pokemon_d.HP
    pokemon_d.receive_damage(pokemon_a.attacks[user])
    after_HP = pokemon_d.HP
    received_damage = before_HP - after_HP
    # print(("#" * int(((after_HP*total)/2))).(50,"-"))
    print(f"{pokemon_a.name} used {pokemon_a.attacks[user]}!")
    print(f"{pokemon_d.name} received {received_damage} damage!")
    user = input("")
    if pokemon_d.is_alive:
        pokemon_d_attack = random.choice(pokemon_d.attacks)
        before_HP = pokemon_a.HP
        pokemon_a.receive_damage(pokemon_d_attack)
        after_HP = pokemon_a.HP
        received_damage = before_HP - after_HP
        print(f"{pokemon_d.name} used {pokemon_d_attack}!")
        print(f"{pokemon_a.name} received {received_damage} damage!")
        user = input("")

if pokemon_a.is_alive:
    print(f"{pokemon_d.name} was defeated!")
    user = input("")
else:
    print(f"{pokemon_a.name} was defeated!")
    


