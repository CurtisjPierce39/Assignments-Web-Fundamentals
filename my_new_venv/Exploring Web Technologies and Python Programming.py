import requests #Question 1 Task 1
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu') #Question 1 Task 2
json_data = response.text
pikachu_data = json.loads(json_data)
print(f"Name: {pikachu_data['name']} \nAbilities: {pikachu_data['abilities']}")

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data = response.text
    pokemon_data = json.loads(json_data)
    return pokemon_data

def calculate_average_weight(pokemon_names):#Question 1 Task 3
    for pokemon_name in pokemon_names:
        pokemon_data = fetch_pokemon_data(pokemon_name)
        name = pokemon_data.get("name", "no name")
        abilities = pokemon_data.get("abilities", ["no abilities"])
        print(f"Name: {name}\nAbilities: {abilities}")
        
    weight_sum = 0        
    for pokemon_name in pokemon_names:
        pokemon_data = fetch_pokemon_data(pokemon_name)
        weight = pokemon_data.get("weight")
        weight_sum += weight
    print(f"Average weight: {weight_sum / len(pokemon_names)}")

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight(pokemon_names)