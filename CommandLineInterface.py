from os.path import exists, getsize
import pickle

#local imports
import Session

class CommandLineInterface:
       
    rootAcctName = 'root'
    
    #define static keywords and screen names
    kwExit = "exit"
    kwHelp = "help"
    kwLogout = "logout"
    kwLogin = "login"
    kwCreateAcct = "newacct"
    kwHist = "history"
    
    #Userhome specific
    kwUserSummary = "show"
    kwDelAcct = "deleteacct"
    kwModAcct = "modacct"
    
    #Admin specific
    kwPromoteAdmin = "promote"
    kwAnnounce = "announce"
    kwDelInactAcct = kwDelAcct
    
    prompt = ">"
    welcomeMsg = "Welcome to Pay All, the Bill centralizer!"
    helpMsg = "Displays a help message showing available commands"
    unrecCmdMsg = " is an unrecognized keyword, type '" + kwHelp + "' if you need help"
    
    logoutMsg = "Signs-out the current user of the system"
    acctExistsMsg = "username is taken"
    acctCreateOkMsg = "Account created succesfully"
    loginOkMsg = "login succesful"
    loginBadMsg = "login failed"
    
    homeScreenName = "syshome"
    adminScreenName = "admin"
    userHomeScreenName = "userhome"
    billViewScreenName = "billview"
    
    def __init__(self, users):
        self.sessions = [] #start with empty session list
        self.users = users #user dict is {key='username', value=userObject}
    
    def __addSession(self, session): #threadsafe eventually
        ind = len(self.sessions)
        self.sessions.append(session)
        return ind
    
    def login(self, userName, password):
        if userName in self.users:
            #if self.users[userName].password == password: #FIXME: authenticate
                return (True, self.users[userName])
        return (False, None)
    
    def createAccount(self, userName, password): #FIXME: threadsafe
        if userName in self.users:
            return (False, None)
        else:
            #FIXME: call User create acct method
            usr = None
            self.users[userName] = usr
            return (True, usr)

    def startSession(self, superUser = False): #superUser is root user spawning system
        #create admin user if one doesn't exist
        session = None
        if superUser:
            if CommandLineInterface.rootAcctName not in self.users:
                suprUsr = None #FIXME with actual user obj
                self.users[CommandLineInterface.rootAcctName] = suprUsr 
            session = Session.CLISession(self, 0, rootSess = True, user = self.users[CommandLineInterface.rootAcctName]) #FIXME add session ID logic
        else:
            pass
        
        self.__addSession(session)
        
        #if superUser: #spawn root session FIXME: unnecessary?
        session.sessionLoop()

if __name__ == "__main__":
    if True: #FIXME: add case for an already running program using multiprocess manager
        #FIXME: add logging (or incl in main func)
        userFileName = 'savedusers.pkl'
        users = {}
        if exists(userFileName) and getsize(userFileName) > 0:
            f = open(userFileName, 'rb')
            users = pickle.load(f)
            f.close()
        cmd = CommandLineInterface(users)
        try:
            cmd.startSession(superUser=True) #FIXME: migrate to manager framework, requiring separate login
        finally:
            f = open(userFileName, 'wb')
            pickle.dump(cmd.users, f)
            f.close()