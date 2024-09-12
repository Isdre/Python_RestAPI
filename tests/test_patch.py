import requests

class TestPatch:
    def test_patch_one_failure(self):
        pokemon_not_exists = {
            'name': "Bulbasaur",
            'edible': False,
            'description': "Salad"
        }

        response = requests.get(f'http://localhost:5000/api/pokemon/{55}',json=pokemon_not_exists)
        assert response.status_code != 200

    def test_patch_one_success(self):
        pokemon_old = {
            'name': "Bulbasaur",
            'edible': True,
            'description': "Salad"
        }
        response = requests.get(f'http://localhost:5000/api/pokemon/{1}',json=pokemon_old)
        assert response.status_code == 200