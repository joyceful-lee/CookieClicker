import unittest
import store

class Test(unittest.TestCase):

    def test_number_exchange(self):
        self.assertEqual(store.number_exchange(100,2), "100", ' < 1000 - Number Exchange Error.')
        self.assertEqual(store.number_exchange(10000,0), "10 Thousand", '0 - Number Exchange Error.')
        self.assertEqual(store.number_exchange(1000000,1), "1.0 Million", '1 - Number Exchange Error.')
        self.assertEqual(store.number_exchange(1000000000,2), "1.00 Billion", '2 - Number Exchange Error.')
        self.assertEqual(store.number_exchange(1000000000000,3), "1.000 Trillion", '3 - Number Exchange Error.')

if __name__ == '__main__':
    unittest.main()