import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000'

class TestSecurity(unittest.TestCase):

    def test_basic_protected_no_credentials(self):
        response = requests.get(f'{BASE_URL}/basic-protected')
        self.assertEqual(response.status_code, 401)

    def test_login_and_jwt_protected(self):
        login_response = requests.post(f'{BASE_URL}/login', json={
            'username': 'user1',
            'password': 'password1'
        })
        self.assertEqual(login_response.status_code, 200)
        access_token = login_response.json().get('access_token')
        self.assertIsNotNone(access_token)

        headers = {'Authorization': f'Bearer {access_token}'}
        jwt_protected_response = requests.get(f'{BASE_URL}/jwt-protected', headers=headers)
        self.assertEqual(jwt_protected_response.status_code, 200)

    def test_admin_only_route(self):
        login_response = requests.post(f'{BASE_URL}/login', json={
            'username': 'admin1',
            'password': 'adminpass'
        })
        self.assertEqual(login_response.status_code, 200)
        access_token = login_response.json().get('access_token')
        self.assertIsNotNone(access_token)

        headers = {'Authorization': f'Bearer {access_token}'}
        admin_only_response = requests.get(f'{BASE_URL}/admin-only', headers=headers)
        self.assertEqual(admin_only_response.status_code, 200)

        # Test with non-admin user
        login_response_user = requests.post(f'{BASE_URL}/login', json={
            'username': 'user1',
            'password': 'password1'
        })
        self.assertEqual(login_response_user.status_code, 200)
        access_token_user = login_response_user.json().get('access_token')
        self.assertIsNotNone(access_token_user)

        headers_user = {'Authorization': f'Bearer {access_token_user}'}
        admin_only_response_user = requests.get(f'{BASE_URL}/admin-only', headers=headers_user)
        self.assertEqual(admin_only_response_user.status_code, 403)

if __name__ == '__main__':
    unittest.main()
