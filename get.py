import requests

move_list = list()
move_type_list = list()
url_name = "https://pokeapi.co/api/v2/pokemon"
url_move = "https://pokeapi.co/api/v2/move"

id_pokemon = int(input("ID: "))

get_pokemon = requests.get(f"{url_name}/{id_pokemon}")
get_pokemon = get_pokemon.json()
print(f"Pokémon: {str(get_pokemon['name']).title()}")

for move in get_pokemon['moves']:
    move_list.append(f"{(move['move']['name'])}")

for element in range(0, len(move_list)):
    get_move = requests.get(f"{url_move}/{move_list[element]}")
    get_move = get_move.json()
    print(f"{move_list[element].title()}: {str(get_move['type']['name']).title()}")
