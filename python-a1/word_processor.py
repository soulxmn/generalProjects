## Date: February 4, 2015
## Author(s): Suleiman Mirza 
#-------------------------------------------------------------------------------

## Central Program 
# Imported Modules
import sys

# Global Variables
commands = ('D', 'UNDO', 'REDO') 
document = []

# UI Messages
introduction = "Welcome to this program! Here, you can create and modify your \
own document. Here is a list of all commands: \n  d - delete a specific line \
\n  undo - undo the last action made \n  redo - redo the most recent action \
that was undone \nIf you wish to just add a line to the document, simply type \
the line in and hit enter. Happy writing!" 
exit_message = "\nYou have successfully terminated this program. Thanks for \
using! \n \n"

run_confirmation = "If you would like to run this program, please type 'RUN'. \
If you would like to exit this program, then simply enter a blank line: " 

main_program_message = "You may now write lines to the document, or use a \
command of your choice. If you wish to enter a blank line to your document and \
not quit the program, type '\\n'." 
invalid_command = "Sorry, that is an invalid command."

remove_line = "Please type the number of the line you would like removed: "
error_line_number = "\nPlease ensure your response \
meets the following critera: \n  is greater than or equal to 1, \n  does not \
exceed the number of lines in this document,\n  does not use any mathematical \
operators or symbols,\n  and is not in the format of a fraction or decimal.\n" 

# Command, Exception, and Helper Functions                                                    
def N_Exception(value: int) -> Exception or None:
    r""" Raise an error if value is not an element of the natural number set 
    (i.e. greater than or equal to 1). 
    
    >>> test1 = -1
    >>> N_Exception(test1)
    __main__.element_of_N: 
    """ 
    
    if value > 0:
        pass
    else:
        raise element_of_N 
    
    return

def quit_program(message: str, file: list) -> str:
    r""" Return and message and file, and exit program by raising SystemExit. 
    
    >>> message = "Good bye!"
    >>> quit_program(message) 
    "Good bye!"
    Traceback (most recent call)...
    builtins.SystemExit:
    """ 
    
    print(file)
    print(message)
    sys.exit()
    
    return

# Please check the bottom of the document for the full explanation of 
# implementing the undo and redo commands.
def undo_redo_cmd(direct_actions_log: "Log", redo_log: "Log", \
                  document1: list) -> None:
    r""" Based on actions defined in direct_actions_log, either add or delete 
    an element of document1. Record this action in redo_log, and remove the most
    recently undone action from direct_actions_log.
    
    >>> actions = [["A", 'hello', 1], ["D", 'bye', 2]]
    >>> actions_undone = []
    >>> document = ['hello'] 
    >>> undo_command(direct_actions_log, redo_log, document1) 
    >>> document
    ['hello', 'bye'] 
    >>> actions_undone
    [["A", 'bye', 2]] 
    >>> actions
    [["A", 'hello', 1]]
    """ 
    
    if direct_actions_log.stack[-1][0] == "D": 
        # Retrieve line index and content.
        temp_index = direct_actions_log.stack[-1][-1]
        line_deleted = direct_actions_log.stack[-1][1] 
        # Undo a delete by adding in the deleted line.
        document1.insert(temp_index, line_deleted) 
        # Record this undo action in the redo logs.
        redo_log.push(["A", line_deleted, temp_index]) 
        # Remove this action so that undo may keep going in backwards 
        # chronological order appropriately.
        direct_actions_log.pop() 
    # Same concept as above, except for line addition.
    elif direct_actions_log.stack[-1][0] == "A": 
        temp_index = direct_actions_log.stack[-1][-1] 
        document1.pop(temp_index)   
        redo_log.push(["D", direct_actions_log.stack[-1][1], temp_index]) 
        direct_actions_log.pop() 
    
    return
    
def delete_line(stack1: list, stack2: "Log", value: object) -> None:
    r""" Modify a stack object by deleting an element. Record line information 
    in log stack2. 
    
    >>> actions_log = Log()    
    >>> test1 = []
    >>> test1.append('this line will be removed')
    >>> test1.append(45)
    >>> delete_line(test1, actions_log)
    Please type the number of the line you would like removed: 1
    >>> test1
    [45]
    >>> actions_log
    [["D", 'this line will be removed', 1]]                                      
    """
    
    try: 
        # Testing for ValueError
        line_number = int(value) 
        # Testing for IndexError.
        stack1[line_number - 1]                     
        # Ensuring value is greater than 0. 
        N_Exception(line_number)                                         
    except ValueError:
        print("\nValue must be an integer.")
    except element_of_N:
        print("\nEnsure that the number is greater than 0.")        
    except IndexError:
        print("\nSorry that line number does not exist.")
        print("Currently, the total number of lines in this document is", \
              str(len(stack1)) + ".") 
    else: 
        # Action Information: 0 - action, 1 - content, 2 - index
        stack2.push(["D", stack1[line_number - 1], line_number - 1])    
        stack1.pop(line_number - 1) 
        error_output = 'No exceptions were raised!' 
        
    return 

# Actions Log and Exception Classes
class Log(object):
    """ Stack object to store actions inputted by user. Standard methods.
    """
    
    def __init__(self: "Log") -> None:
        """ Initialize the empty list. 
        """ 
        
        self.stack = [] 
        
        return 
    
    def push(self: "Log", item: object) -> None: 
        r""" Add an item to the current stack. 
        
        >>> test1.push(1)
        >>> test1.push('1')
        >>> len(test1)
        2
        """ 
        
        self.stack.append(item) 
        
        return
    
    def pop(self: "Log") -> object:
        r""" Remove and return the most recently added item in the stack. 
        
        >>> test1.push(int('45'))
        >>> test1.pop()
        45
        """ 
        
        self.stack.pop() 
        
        return
    
    def is_empty(self: "Log") -> bool:
        r""" Return True iff the current stack has no elements.
        
        >>> test1 = Document()
        >>> test1.is_empty()
        True
        """  
        
        return len(self.stack) == 0 
    
class element_of_N(Exception):
    pass
#-------------------------------------------------------------------------------   

## Main Program
if __name__ == '__main__':
    print('\n' + introduction, '\n') 
    conf = input(run_confirmation) 
    while not conf.isspace() or not (len(conf)) == 0 or conf != "RUN":
        if conf.upper() == "RUN":
            title = input("Please enter a title for this document: ")
            author = input("Please enter the author's name: ") 
            # Keeping track of actions that might need to be undone.
            actions = Log() 
            # Keeping track of undos that might need to be redone.
            actions_undone = Log()
            print('\n' + main_program_message)
            user_input = input("Command? ")
            while not user_input.isspace() and not len(user_input) == 0: 
                if user_input.upper() in commands:               
                    # Delete                      
                    if user_input.upper() == commands[0] \
                       and len(document) != 0: 
                        # Check if document is altered or not. 
                        # Update at every call.
                        old_document = []
                        for element in document:
                            old_document.append(element)
                        incorrect_input = True
                        while incorrect_input:
                            value = input(remove_line)
                            delete_line(document, actions, value) 
                            if old_document != document:
                                incorrect_input = False
                            else:
                                print(error_line_number)
                    # Undo
                    elif user_input.upper() == commands[1] and \
                         len(actions.stack) != 0:
                        undo_redo_cmd(actions, actions_undone, document)
                    # Redo
                    elif user_input.upper() == commands[-1] and \
                         len(actions_undone.stack) != 0: 
                        undo_redo_cmd(actions_undone, actions, document)
                        
                    else: 
                        # Check for deleting non-existent content.
                        if user_input.upper() == commands[0]: 
                            print("There is nothing left to delete!") 
                        # When everything has been undone to the first command. 
                        elif user_input.upper() == commands[1]:
                            print("There is nothing left to undo!")  
                        # When all undone commands were redone.
                        else:
                            print("There is nothing left to redo!")              
                            
                elif user_input.upper() not in commands:
                    document.append(user_input)
                    actions.push(["A", user_input, len(document) - 1]) 
                    
                print("\nCurrent document: \n", document, '\n') 
                user_input = input("Command? ") 
            quit_program(exit_message, document)
        # Check for when user enters a blank space (blank / empty line).
        elif conf.isspace() or len(conf) == 0:
            quit_program(exit_message, document)
            
        else:
            print(invalid_command)
            conf = input("Please re-type what you would like to do: ") 
#------------------------------------------------------------------------------- 

## Program Description
"""
This program uses stacks for both the undo and redo commands. All actions that 
are input by the user (excluding commands redo and undo) are automatically 
added into the stack called 'actions' (i.e. addition and deletion of a line). 
Anytime the user calls undo, the action performed by the undo will be recorded 
in a stack called 'actions_undone'. Due to the stack's LIFO nature, the most 
recent action recorded in each can be executed by doing the opposite. In both 
cases, every time an action from either stack is completed, it is deleted from
that respective stack in order to ensure that if the user calls once more the 
same command, the program will execute the opposite for the second most recent 
action done, and so on and so forth.

In detail, each stack records a list of information per action. This list is
structured as such: [action_by_user, content_acted_upon, index_of_content]. 
The first element can only ever be "D" or "A" (delete and add respectively). The
second is just the line which is either deleted or added, and the third, the 
index.

In order to implement the relationship between undo and redo, I wrote the 
function undo_redo_cmd. The reason it has both commands in one is that it can 
work for either. What this function does is it looks at the stack passed in 
that is for it's command. If we call it in for a redo command, it will look at
the stack 'actions_undone', and the stack 'actions' for undo. In either case,
it checks the first element to know what it must do; if it's an "A" then we must
delete, and vice versa. It then retrieves the line and it's index, and 
appropriately alters list document (containing all lines of the user). 
The reason this can work for both undo and redo is that before deleting the 
completed action from it's respective stack, the function will add that action
into the other command's stack. If we call it in for redo, before deleting the 
action from the redo stack, it will add it in to the undo stack, and vice versa.
This allows both commands to be up-to-date with one another, and accordingly 
perform the "undo of a redo" or the "redo of an undo" command according to the 
most recent action performed. Since the function deletes the action from the
appropriate command's list each time, the user doesn't need to worry about
continuously "undoing" or "redoing", as successive undos and redos will also
work in the same manner.
"""