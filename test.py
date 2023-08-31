import unittest
import json
from app import app


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_create_prompt(self):
        data = {"prompt": "Hi, How are You?"}
        response = self.app.post('/create', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {
                         "message": "Prompt created successfully"})

    def test_read_prompt(self):
        # Assuming an index exists, replace with actual index
        response = self.app.get('/read?index=0')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("prompts" in json.loads(response.data))

    def test_read_prompt_invalid_index(self):
        response = self.app.get('/read?index=100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Invalid index"})

    def test_get_response(self):
        # Assuming an index exists, replace with actual index
        response = self.app.get('/get_response?index=0')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("response" in json.loads(response.data))

    def test_get_response_invalid_index(self):
        response = self.app.get('/get_response?index=100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Invalid index"})

    def test_update_prompt(self):
        data = {"index": 0, "new_prompt": "Greetings!"}
        response = self.app.put('/update', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {
                         "message": "Prompt updated successfully"})

    def test_update_prompt_invalid_index(self):
        data = {"index": 100, "new_prompt": "Greetings!"}
        response = self.app.put('/update', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Invalid index"})

    def test_delete_prompt_invalid_index(self):
        data = {"index": 100}
        response = self.app.delete('/delete', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"error": "Invalid index"})


if __name__ == '__main__':
    unittest.main()
