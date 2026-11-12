import unittest
from app import app

class SmartRailTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "Smart Rail Ticket Booking System is running"
        )

    def test_search_pune_mumbai(self):
        response = self.client.get("/search?from=Pune&to=Mumbai")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["no"], "12127")

    def test_search_pune_kolhapur(self):
        response = self.client.get("/search?from=Pune&to=Kolhapur")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Koyna Express")

    def test_search_no_matching_train(self):
        response = self.client.get("/search?from=Mumbai&to=Delhi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

if __name__ == "__main__":
    unittest.main()
