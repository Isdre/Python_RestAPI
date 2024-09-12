import requests


class TestPost:
    def test_post_already_exists(self):
        pokemon_old = {
            'name': "Bulbasaur",
            'edible': True,
            'description': "Salad"
        }

        response = requests.post('http://localhost:5000/api/pokemons/', json=pokemon_old)

        assert response.status_code != 201

    def test_post_create(self):
        pokemon_new = {
            'id': 3,
            'name': "Venusaur",
            'edible': True,
            'description': "The biggest salad"
        }

        response = requests.post('http://localhost:5000/api/pokemons/', json=pokemon_new)

        assert response.status_code == 201