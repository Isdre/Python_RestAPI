import requests

class TestDelete:
    def test_delete_one_success(self):
        response = requests.delete(f'http://localhost:5000/api/pokemon/{3}')
        assert response.status_code == 204

    def test_delete_one_failure(self):
        response = requests.delete(f'http://localhost:5000/api/pokemon/{3}')
        assert response.status_code != 204