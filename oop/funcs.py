def menu():
    print("POKEMON".center(50, "#"))
    print("Oak: Select your first pokemon...")

def print_attacks(pokemon_a):
    [print(f"{i + 1}. {attack.name}") for i, attack in enumerate(pokemon_a.attacks)]