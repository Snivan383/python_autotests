import pytest
import requests
url='https://api.pokemonbattle.ru/v2'
trainer_id=36124
def test_status_code():
    responce=requests.get(url=f'{url}/trainers')
    assert responce.status_code==200
def test_get_trainers():
    responce_id=requests.get(url=f'{url}/trainers', params={'trainer_id': trainer_id})
    assert responce_id.json()['data'][0]['id']==str(trainer_id)