#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import datetime
import unittest
from unittest.mock import patch

from main import RegUsr, admin, listAccountsRegUsr

# Create three dummy lastLogin dates in the past (Boundary Test Cases)
lastLogin1 = datetime.datetime.now() - datetime.timedelta(days=89)
lastLogin2 = datetime.datetime.now() - datetime.timedelta(days=90)
lastLogin3 = datetime.datetime.now() - datetime.timedelta(days=91)

# Set the lastLogin attribute of the RegUsr objects in the listAccountsRegUsr list to the dummy dates
listAccountsRegUsr[0].lastLogin = lastLogin1
listAccountsRegUsr[1].lastLogin = lastLogin2
listAccountsRegUsr[2].lastLogin = lastLogin3


class TestAdminMethods(unittest.TestCase):

    def setUp(self):
        # Create a new admin account and set its lastLogin attribute to the current date and time
        self.admin = admin("admin1", "admin-password1")
        self.admin.lastLogin = datetime.datetime.now()

    def test_delete_inactive_account(self):
        # Test the delete_inactive_account method
        # 3 Boundary Test Cases
        self.assertTrue(self.admin.delete_inactive_account("user1"), "Delete inactive account")
        self.assertFalse(self.admin.delete_inactive_account("user2"), "Do not delete active account")
        self.assertFalse(self.admin.delete_inactive_account("user3"), "Do not delete account that does not exist")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_announce(self, mock_stdout):
        # Test Case 1: Default importance level
        self.assertEqual(self.admin.announce("This is a regular announcement"), "This is a regular announcement")
        self.assertEqual(mock_stdout.getvalue(), "This is a regular announcement\n")

        # Test Case 2: High importance level
        self.assertEqual(self.admin.announce("This is an important announcement", 1), "IMPORTANT: This is an "
                                                                                      "important announcement")
        self.assertEqual(mock_stdout.getvalue(), "IMPORTANT: This is an important announcement")


if __name__ == '__main__':
    unittest.main()
