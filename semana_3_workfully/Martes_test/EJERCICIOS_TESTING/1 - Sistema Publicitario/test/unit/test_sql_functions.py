

import unittest
from src.utils import sql_query, create_or_insert

class TestSqlFunctions(unittest.TestCase):

    # No cursor, must raise AttributeError
    def test_sql_query(self):
        with self.assertRaises(AttributeError):
            sql_query(query='SELECT * FROM users;', cursor=None)

    def test_create_or_insert(self):
        with self.assertRaises(AttributeError):
            create_or_insert(query='SELECT * FROM users;',
                             cursor=None, connection=None)

if __name__ == '__main__':
    unittest.main()