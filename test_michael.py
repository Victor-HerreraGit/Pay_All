#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:59:42 2023

@author: buzz66boy
"""

import unittest

#local
from CommandLineInterface import CommandLineInterface

class MichaelUnitTests(unittest.TestCase):
    def test_CLI(self):
        cli = CommandLineInterface()
        
        usrName = "michael"
        cli.createAccount(usrName, "1234")
        self.assertIn(usrName, cli.users)