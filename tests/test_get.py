import requests

class TestGet:
    def test_get_all(self):
        response = requests.get('http://localhost:5000/api/pokemons/')
        assert response.status_code == 200

    def test_get_one_failure(self):
        response = requests.get(f'http://localhost:5000/api/pokemon/{0}')
        assert response.status_code != 200

    def test_get_one_success(self):
        response = requests.get(f'http://localhost:5000/api/pokemon/{1}')
        assert response.status_code == 200