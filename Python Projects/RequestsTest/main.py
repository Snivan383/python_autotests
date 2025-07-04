import requests
url='https://api.pokemonbattle.ru/v2'
token='TRAINER_TOKEN'
hader={'content_type': 'application/json', 'trainer_token': token}
body_create={
    "name": "Бульбазавр",
    "photo_id": -1
}
responce_create=requests.post(url=f'{url}/pokemons', headers=hader, json=body_create)
print(responce_create.text)
data=responce_create.json()
pokemon_id=data['id']
body_change_name={
    "pokemon_id": str(pokemon_id),
    "name": "Заяц",
    "photo_id": -1
}
responce_change_name=requests.put(url=f'{url}/pokemons', headers=hader, json=body_change_name)
print(responce_change_name.text)
body_add_pokeball={
    "pokemon_id": str(pokemon_id)
}
responce_catch_pokemon=requests.post(url=f'{url}/trainers/add_pokeball', headers=hader, json=body_add_pokeball)
print(responce_catch_pokemon.text)
