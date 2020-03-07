'''
DEFINE COMMANDS HERE:
'''

def add(inputs):
    a = inputs["arg1"]
    b = inputs["arg2"]
    return a + b

'''
The command handler reads the command, and processes the inputs accordingly.
'''
class CommandHandler:
    
    def __init__(self):
        self.__commandList = {
            #insert commands here.
            "add": add
        }

    '''
        command - the command to execute
        inputs - the inputs provided in the form of a dictionary
        returns something depending on what command is being executed.
    '''
    def processCommand(self, command, inputs):
        if self.__commandList[command] != None:
            return self.__commandList[command](inputs)
        else:
            return None

print("running add command: ")
commandHandler = CommandHandler()
result = commandHandler.processCommand("add", {"arg1": 5, "arg2": 10})
print("Result is: " + str(result))