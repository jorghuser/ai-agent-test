import unittest
from utils import add_numbers, greet, parse_query_string

class TestUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_parse_query_string(self):
        self.assertEqual(parse_query_string(""), {})
        self.assertEqual(parse_query_string("name=Alice"), {"name": "Alice"})
        self.assertEqual(parse_query_string("name=Alice&age=30"), {"name": "Alice", "age": "30"})
        self.assertEqual(parse_query_string("name="), {"name": ""})
        self.assertEqual(parse_query_string("name"), {})
        self.assertEqual(parse_query_string("&name=Alice"), {"name": "Alice"})
        self.assertEqual(parse_query_string("name=Alice&"), {"name": "Alice"})

if __name__ == '__main__':
    unittest.main()
