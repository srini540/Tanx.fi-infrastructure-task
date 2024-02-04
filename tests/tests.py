import unittest


# Importing compute_revenue function from the orders.py
from orders import compute_revenue

class TestComputeRevenue(unittest.TestCase):
   

    def test_missing_column(self):
        with self.assertRaises(SystemExit):
            compute_revenue('colmissing.csv')

    def test_missing_data(self):
        with self.assertRaises(SystemExit):
            compute_revenue('rowmissing.csv')

    def test_invalid_date_format(self):
         with self.assertRaises(SystemExit):
             compute_revenue('date.csv')

if __name__ == '__main__':
    unittest.main()
