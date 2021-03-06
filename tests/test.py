import unittest
from app import weigth, helpers, connect, config



class TestWeightsApp(unittest.TestCase):
    def test_connection(self):
        query = """SELECT current_database();"""
        self.assertEqual(connect.db_connect(query, None, 1), "Connection closed")
        self.assertEqual(connect.db_connect(query, None, 2), "Connection closed")
        
if __name__ == '__main__':
    unittest.main()
        
