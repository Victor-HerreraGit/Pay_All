from os.path import exists, getsize
import pickle

#local imports
import Session

class CommandLineInterface:
    sessions = [] #start with empty session list
    users = dict() #user dict is {key='username', value=userObject}
    
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
    logoutMsg = "Signs-out the current user of the system"
    unrecCmdMsg = " is an unrecognized keyword, type '" + kwHelp + "' if you need help"
    acctExistsMsg = "username is taken"
    
    homeScreenName = "syshome"
    adminScreenName = "admin"
    userHomeScreenName = "userhome"
    billViewScreenName = "billview"
    
    def __init__(self):
        pass
    
    def __addSession(self, session): #threadsafe eventually
        ind = len(CommandLineInterface.sessions)
        CommandLineInterface.sessions.append(session)
        return ind
    
    def login(self, userName, password):
        if userName in CommandLineInterface.users:
            #if CommandLineInterface.users[userName].password == password: #FIXME: authenticate
                return (True, CommandLineInterface.users[userName])
        return (False, None)
    
    def createAccount(self, userName, password): #FIXME: threadsafe
        if userName in CommandLineInterface.users:
            return (False, None)
        else:
            #FIXME: call User create acct method
            usr = None
            CommandLineInterface.users[userName] = usr
            return (True, usr)

    def startSession(self, superUser = False): #superUser is root user spawning system
        #create admin user if one doesn't exist
        session = None
        if superUser:
            if CommandLineInterface.rootAcctName not in CommandLineInterface.users:
                suprUsr = None #FIXME with actual user obj
                CommandLineInterface.users[CommandLineInterface.rootAcctName] = suprUsr 
            session = Session.CLISession(self, 0, rootSess = True, user = CommandLineInterface.users[CommandLineInterface.rootAcctName]) #FIXME add session ID logic
        else:
            pass
        
        self.__addSession(session)
        
        if superUser: #spawn root session
            session.sessionLoop()

if __name__ == "__main__":
    if True: #FIXME: add case for an already running program using multiprocess manager
        #FIXME: add logging (or incl in main func)
        userFileName = 'savedusers.pkl'
        if exists(userFileName) and getsize(userFileName) > 0:
            f = open(userFileName, 'rb')
            CommandLineInterface.users = pickle.load(f)
            f.close()
        cmd = CommandLineInterface()
        try:
            cmd.startSession(superUser=True) #FIXME: migrate to manager framework, requiring separate login
        finally:
            f = open(userFileName, 'wb')
            pickle.dump(CommandLineInterface.users, f)
            f.close()