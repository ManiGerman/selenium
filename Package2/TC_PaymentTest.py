import unittest

class paymentTest(unittest.TestCase):
    def test_paymentindollar(self):
        print("This is payment in dollar test")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("This is payment in Rupees test")
        self.assertTrue(True)

if __name__== "__main__":
    unittest.main()