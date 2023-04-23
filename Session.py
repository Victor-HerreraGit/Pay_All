#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:50:01 2023

@author: buzz66boy
"""

from collections import deque
import sys

#local imports
import CommandLineInterface

class CLISession:
    def __init__(self, cli, sessID, rootSess = False, user = None, histLen = 10):
        self.__sessionID = sessID
        self.cli = cli
        self.rootSess = rootSess
        self.user = user
        
        self.history = deque(maxlen = histLen) #user accessible to see previous commands
        self.internalHistory = deque(maxlen = 100) #this is for debugging purposes
        
        #Syntax Map dict(key=ScreenName, val=dict(key = function names, val = list([args & description, function pointer])))
        self.syn_map = dict()
        
        #map non-common homescreen commands
        self.syn_map[cli.homeScreenName] = dict()
        self.syn_map[cli.homeScreenName][cli.kwLogin] = ["usage: '" + cli.kwLogin + " username password', logs into the specified user's account", self.login]
        self.syn_map[cli.homeScreenName][cli.kwCreateAcct] = ["usage '" + cli.kwCreateAcct + " username password' creates a new account with username specified if one doesn't exist", None] #FIXME: Add function
        
        self.syn_map[cli.adminScreenName] = dict()
        
        self.syn_map[cli.userHomeScreenName] = dict()
        # self.syn_map[self.userHomeScreenName][cli.kwLogin] = 
        
        self.syn_map[cli.billViewScreenName] = dict()
        
        #help, history, and logout population on all screens
        for keyScrn in self.syn_map:
            self.syn_map[keyScrn][cli.kwHelp] = [cli.helpMsg, self.__help]
            self.syn_map[keyScrn][cli.kwHist] = ["usage '" + cli.kwHist + "' displays last 10 commands", self.__hist]
            self.syn_map[keyScrn][cli.kwExit] = ["Exits the program", None] #Special case #FIXME: add logout and exit methods
            if keyScrn != cli.homeScreenName:
                self.syn_map[keyScrn][cli.kwLogout] = [cli.logoutMsg, None] #FIXME: Add function
        
        self.curScreen = cli.homeScreenName
    
    def __sanitize(self, string):
        return string.lower()

    def __help(self):
        helpStr = ""
        for key in self.syn_map[self.curScreen]:
            helpStr +=  key + " -- " + self.syn_map[self.curScreen][key][0] + "\n"
           
        self.display(helpStr)
        
    def __hist(self):
        histStr = ""
        for i in range(len(self.history)):
            histStr += str(len(self.history) - i) + ": " + self.history[i] + "\n"
        self.display(histStr)
    
    def getSessionID(self):
        return self.__sessionID
    
    def display(self, string):
        print(string)
        #FIXME: add to log file
    
    def login(self, user, password):
        #FIXME multiprocess query for user
        success, usr = self.cli.login(user, password)
        if success:
            self.curScreen = self.cli.userHomeScreenName
            #admin
            #if self.user != None and self.user.isAdmin(): #FIXME
            if True: #FIXME hardcoded admin
                #populate admin commands
                pass
    
    def sessionLoop(self):
        kw = ""
        while kw != self.cli.kwExit:
            inp = input(self.cli.prompt)
            self.history.append(inp)
            self.internalHistory.append(inp)
            self.display(inp)
            cmd = inp.split()
            kw = self.__sanitize(cmd[0])
            if len(cmd) > 1:
                args = cmd[1:]
            else:
                args = []
            if kw in self.syn_map[self.curScreen]:
                if self.syn_map[self.curScreen][kw][1] != None: #check for keyword associated function
                    #try: #except arg issues and notify user
                    try:
                        self.syn_map[self.curScreen][kw][1](*args)
                    except TypeError as e:
                        self.display("Args error")
                        self.display(e)
            else:
                self.display("'" + kw + "'" + self.cli.unrecCmdMsg)