#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:59:42 2023

@author: buzz66boy
"""
import os
import unittest
from unittest import mock, TestCase

#local
from CommandLineInterface import CommandLineInterface
from Session import CLISession

class MichaelUnitTests(TestCase):
    
    #sample test
    def test_CLI(self):
        cli = CommandLineInterface({})
        
        usrName = "michael"
        cli.createAccount(usrName, "1234")
        self.assertIn(usrName, cli.users)
    
    #white-box unit test section
    def test_cli_create_acct(self):
        cli = CommandLineInterface({})
        
        usrName = "michael"
        (success, usrObj) = cli.createAccount(usrName, "1234")
        self.assertTrue(success, "Create non-existing account")
        
    def test_cli_create_exist_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({usrName: None})
        cli.createAccount(usrName, "1234")
        
        (success, usrObj) = cli.createAccount(usrName, "1234")
        self.assertFalse(success, "Create already existing account")
    
    def test_cli_login_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({usrName: None})
        
        (success, usrObj) = cli.login(usrName, "1234")
        self.assertTrue(success, "Login to existing account")
        
    def test_cli_login_nonexist_acct(self):
        cli = CommandLineInterface({})
        
        usrName = "michael"
        (success, usrObj) = cli.login(usrName, "1234")
        self.assertFalse(success, "Login to non-existing account")
        
    #black-box unit test section
    
    def test_ses_create_acct(self):
        cli = CommandLineInterface({})
        m = mock.Mock(return_value=(True, None))
        cli.createAccount = m
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.createAccount("michael", "1234")
        
        cli.createAccount.assert_called()
        mock_method.assert_called_once_with(cli.acctCreateOkMsg)
        # print(mock_method.call_args[0])

    def test_ses_create_exist_acct(self):
        cli = CommandLineInterface({})
        m = mock.Mock(return_value=(False, None))
        cli.createAccount = m
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.createAccount("michael", "1234")
        
        cli.createAccount.assert_called()
        mock_method.assert_called_once_with(cli.acctExistsMsg)
    
    def test_ses_login_acct(self):
        cli = CommandLineInterface({})
        m = mock.Mock(return_value=(True, None))
        cli.login = m
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.login("michael", "1234")
        
        cli.login.assert_called()
        mock_method.assert_called_once_with(cli.loginOkMsg)
    
    def test_ses_login_nonexist_acct(self):
        cli = CommandLineInterface({})
        m = mock.Mock(return_value=(False, None))
        cli.login = m
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.login("michael", "1234")
        
        cli.login.assert_called()
        mock_method.assert_called_once_with(cli.loginBadMsg)
        
    #Integration tests
    def test_integ_cli_ses_create_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({})
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.createAccount(usrName, "1234")
            
        # print(mock_method.call_args_list)
        
        self.assertIn(usrName, cli.users, "user added to user list")
        mock_method.assert_called_once_with(cli.acctCreateOkMsg)
        
    def test_integ_cli_ses_create_exist_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({usrName: None})
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.createAccount(usrName, "1234")
        # self.assertFalse(success, "Create already existing account")
        mock_method.assert_called_once_with(cli.acctExistsMsg)
    
    def test_integ_cli_ses_login_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({usrName: None})
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.login(usrName, "1234")
            
        mock_method.assert_called_once_with(cli.loginOkMsg)
        
    def test_integ_cli_ses_login_nonexist_acct(self):
        usrName = "michael"
        cli = CommandLineInterface({})
        
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            session = CLISession(cli, 0, rootSess = True, user = None)
            session.login(usrName, "1234")
        # self.assertFalse(success, "Login to non-existing account")
        mock_method.assert_called_once_with(cli.loginBadMsg)
        
    #WIP integration test
    @mock.patch('builtins.input', create=True)
    def test_cli_session_integration(self, mocked_input):#, mocked_output):
        cmds = [CommandLineInterface.kwHelp, CommandLineInterface.kwExit]
        with mock.patch.object(CLISession, 'display', return_value=None) as mock_method:
            mocked_input.side_effect = cmds
            cli = CommandLineInterface({})
            cli.startSession(superUser=True)
            
        # print(mock_method.call_args_list)
        self.assertEqual(mock_method.call_count, 4, "CLISession.display called 4 times")
        mock_method.assert_called_with(CommandLineInterface.kwExit)
        
if __name__ == "__main__":
    unittest.main()