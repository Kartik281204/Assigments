import requests
base_url = "https://pokeapi.co/api/v2"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Failed to retreive your pokemon , why do you want a pokemon tho arent you like 30 🤡🤡🤡🤡")


pokemon_name = "charizard"
pokedex = get_pokemon_info(pokemon_name)
if pokedex:
    print(f"Name:{pokedex["name"]}")
    print(f"Height::{pokedex["height"]}")
    print(f"ID:{pokedex["id"]}")
    print(f"Weight:{pokedex["weight"]}")
else:
    print("Fail Fail Fail")
