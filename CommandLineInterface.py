from collections import deque

class CommandLineInterface:

    def __init__(self, histLen = 10):
        
        self.histLen = histLen
        self.history = deque(maxlen = histLen) #user accessible to see previous commands
        self.internalHistory = deque(maxlen = 100) #this is for debugging purposes
        
        self.kwExit = "exit"
        self.kwHelp = "help"
        self.kwLogout = "logout"
        self.kwLogin = "login"
        self.kwCreateAcct = "newacct"
        self.kwHist = "history"
        
        self.prompt = ">"
        self.welcome_msg = "Welcome to Pay All, the Bill centralizer!"
        self.helpMsg = "Displays a help message showing available commands"
        self.logoutMsg = "Signs-out the current user of the system"
        self.unrecCmdMsg = " is an unrecognized keyword, type '" + self.kwHelp + "' if you need help"
        
        self.homescreenName = "syshome"
        self.adminScreenName = "admin"
        self.userHomeScreenName = "userhome"
        self.billViewScreenName = "billview"
        
        #Syntax Map dict(key=ScreenName, val=dict(key = function names, val = list([args & description, function pointer])))
        self.syn_map = dict()
        
        #map non-common homescreen commands
        self.syn_map[self.homescreenName] = dict()
        self.syn_map[self.homescreenName][self.kwExit] = ["Exits the program", None] #Special case
        self.syn_map[self.homescreenName][self.kwLogin] = ["usage: '" + self.kwLogin + " username password', logs into the specified user's account", None] #FIXME: Add function
        self.syn_map[self.homescreenName][self.kwCreateAcct] = ["usage '" + self.kwCreateAcct + " username password' creates a new account with username specified if one doesn't exist", None] #FIXME: Add function
        
        
        self.syn_map[self.adminScreenName] = dict()
        self.syn_map[self.userHomeScreenName] = dict()
        self.syn_map[self.billViewScreenName] = dict()
        
        #help population
        for keyScrn in self.syn_map:
            self.syn_map[keyScrn][self.kwHelp] = [self.helpMsg, self.__help]
            self.syn_map[keyScrn][self.kwHist] =["usage '" + self.kwHist + "' displays last 10 commands", self.__hist]
            if keyScrn != self.homescreenName:
                self.syn_map[keyScrn][self.kwLogout] = [self.logoutMsg, None] #FIXME: Add function
            
        self.curScreen = self.homescreenName

    def __sanitize(self, string):
        return string.lower()

    def __help(self, args):
        helpStr = ""
        for key in self.syn_map[self.curScreen]:
            helpStr +=  key + " -- " + self.syn_map[self.curScreen][key][0] + "\n"
        self.display(helpStr)
        
    def __hist(self, args):
        histStr = ""
        for i in range(len(self.history)):
            histStr += str(len(self.history) - i) + ": " + self.history[i] + "\n"
        self.display(histStr)
    
    def submitText(self, string):
        return string

    def startSession(self):
        self.display(self.welcome_msg)
        
        kw = ""
        while kw != self.kwExit:
            inp = input(self.prompt)
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
                    self.syn_map[self.curScreen][kw][1](args)
            else:
                self.display("'" + kw + "'" + self.unrecCmdMsg)

    def display(self, string):
        print(string)

if __name__ == "__main__":
    #FIXME: add logging (or incl in main func)
    cmd = CommandLineInterface()
    try:
        cmd.startSession()
    finally:
        pass #FIXME: Print history of commands to log file