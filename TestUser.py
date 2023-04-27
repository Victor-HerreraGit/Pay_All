import unittest
from User import User
from PaymentMethod import PaymentMethod
from Bill import Bill


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Victor", "password123", False, "credit card", [])

    def test_create_account(self):
        self.user.create_account("Victor", "newpassword456")
        self.assertEqual(self.user.username, "Victor")
        self.assertEqual(self.user.password, "newpassword456")
        with self.assertRaises(ValueError):
            self.user.create_account(None, 'password')
        with self.assertRaises(ValueError):
            self.user.create_account('username', None)

    def test_modify_account(self):
        self.user.modify_account(None,None,None,None,None)
        self.user.modify_account(administrator=True, payment_method="paypal")
        self.assertTrue(self.user.administrator)
        self.assertEqual(self.user.payment_method, "paypal")

    def test_delete_account(self):
        self.user.delete_account()
        self.assertIsNone(self.user.username)
        self.assertIsNone(self.user.password)
        self.assertIsNone(self.user.administrator)
        self.assertIsNone(self.user.payment_method)
        self.assertIsNone(self.user.bills)


if __name__ == '__main__':
    unittest.main()
