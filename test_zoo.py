import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    # Add your additional test cases here.

    #Equivalent Class Partitioning

    def test_invalid_age(self):  #class invalid
        self.assertEqual(self.zoo.get_ticket_price(-1), 'Invalid Age')

    def test_child_price(self): #class 0-12
        self.assertEqual(self.zoo.get_ticket_price(6), 50)

    def test_teenager_price(self): #class 13-20
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test_worker_price(self): #class 21-60
        self.assertEqual(self.zoo.get_ticket_price(42), 150)
    
    def test_older_price(self): #class higher 60 (> 60)
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

    #Boundary Value Analysis 

    #class invalid
    def test_invalid_age2(self):  
        self.assertEqual(self.zoo.get_ticket_price(-1), 'Invalid Age')

    #class 0-12
    def test_child_price1(self): 
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child_price2(self): 
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    #class 13-20
    def test_teenager_price1(self): 
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teenager_price2(self): 
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    #class 21-60
    def test_worker_price1(self): 
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_worker_price2(self): 
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    #class higher 60 (> 60)
    def test_older_price1(self): 
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

           
if __name__ == '__main__':
    unittest.main()