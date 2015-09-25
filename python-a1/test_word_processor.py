## Date: February 4, 2015
## Author(s): Suleiman Mirza 
#-------------------------------------------------------------------------------

## Central Program 
# Imported Modules
import unittest
from word_processor import * 

# Global Variables 
doc_unaltered = 'Document failed to successfully alter!'
undo_unupdated = 'Undo log failed to update!'
redo_unupdated = 'Redo log failed to update!' 
v_fail_catch = 'ValueError exception not caught!' 
n_fail_catch = 'element_of_N exception not caught!'
i_fail_catch = 'IndexError exception not caught!' 
number_prompt = "Please enter a line number: " 
empty_stack_conf = 'Cannot determine emptiness of stack!'

# Testing Functions and Classes
class testUndoandRedo(unittest.TestCase):
    ''' Test the 4 cases of the undo_redo_cmd function. 
    
    Note: Each test will check three things, due to the function's multi-purpose
    nature. Notice the difference between Undo and Redo tests is that their
    parameters are switched around, yielding a different result. The program
    checks for invalid input before issuing this function, so invalid input is
    not tested here.
    ''' 
    
    def setUp(self: 'testUndoandRedo') -> None:
        ''' Set up the basic variables to use this function.
        '''
        
        self.test_document = ['line 1', 'line 2', 'line 3'] 
        self.actions = Log()
        self.actions_undone = Log() 
        
        return
    
    def tearDown(self: 'testUndoandRedo') -> None:
        ''' Reset the variables to avoid incorrect updating of logs and list.
        ''' 
        
        while not self.actions.is_empty:
            self.actions.pop()
        
        while not self.actions_undone.is_empty:
            self.actions_undone.pop() 
        
        return
    
    def testUndoAdd(self: 'testUndoandRedo') -> None:
        ''' Addition case for undo.
        '''  
        
        self.actions.push(["A", 'line 2', 1])
        undo_redo_cmd(self.actions, self.actions_undone, self.test_document) 
        
        # Document check.
        result1 = self.test_document
        self.assertEqual(result1, ['line 1', 'line 3'], doc_unaltered)
        
        # Logs check.
        result2 = self.actions.stack
        self.assertEqual(result2, [], undo_unupdated)  
        
        result3 = self.actions_undone.stack
        self.assertEqual(result3, [['D', 'line 2', 1]], redo_unupdated) 
        
        return 
    
    def testUndoDelete(self: 'testUndoandRedo') -> None:
        ''' Deletion case for undo.
        '''  
        
        self.actions.push(['D', 'line 2', 1])
        self.test_document = ['line 1', 'line 3']
        undo_redo_cmd(self.actions, self.actions_undone, self.test_document) 
        
        # Document check.
        result1 = self.test_document
        self.assertEqual(result1, ['line 1', 'line 2', 'line 3'], doc_unaltered)
        
        # Logs check.
        result2 = self.actions.stack
        self.assertEqual(result2, [], undo_unupdated)   
        
        result3 = self.actions_undone.stack
        self.assertEqual(result3, [['A', 'line 2', 1]], redo_unupdated) 
        
        return         
    
    def testRedoAdd(self: 'testUndoandRedo') -> None:
        ''' Addition case for redo.
        ''' 
        
        self.actions_undone.push(['A', 'line 2', 1]) 
        undo_redo_cmd(self.actions_undone, self.actions, self.test_document) 
        
        # Document check.
        result1 = self.test_document
        self.assertEqual(result1, ['line 1', 'line 3'], doc_unaltered) 
        
        # Logs check.
        result2 = self.actions_undone.stack
        self.assertEqual(result2, [], redo_unupdated)
        
        result3 = self.actions.stack
        self.assertEqual(result3, [['D', 'line 2', 1]], undo_unupdated)
        
        return 
    
    def testRedoDelete(self: 'testUndoandRedo') -> None:
        ''' Deletion case for redo.
        ''' 
        
        self.actions_undone.push(['D', 'line 2', 1])
        self.test_document = ['line 1', 'line 3']
        undo_redo_cmd(self.actions_undone, self.actions, self.test_document) 
        
        # Document check. 
        result1 = self.test_document
        self.assertEqual(result1, ['line 1', 'line 2', 'line 3'], doc_unaltered)
        
        # Logs check.
        result2 = self.actions_undone.stack
        self.assertEqual(result2, [], redo_unupdated)
        
        result3 = self.actions.stack
        self.assertEqual(result3, [['A', 'line 2', 1]], undo_unupdated)
        
        return    

# The two letters after each prompt help you identify which form of input is
# expected as per the test case.
class testDelete(testUndoandRedo):
    ''' Test the delete function and it's exceptions. 
    '''  
    
    print('Please ignore the exception print statements that will come after \
each test case in this class. They are only for the word_processor.py program, \
but print automatically as soon as the exception is raised. Simply look to the \
two letters at the end of each prompt to know what to input according to the \
test case.')
    
    def testValidInput(self: 'testDelete') -> None:
        ''' Raise no exceptions (valid input).
        ''' 
        
        # Assuming user gives valid input of '2'.
        value = input(number_prompt + "(VI) ")
        delete_line(self.test_document, self.actions, value)
        
        # Document check.
        result1 = self.test_document
        self.assertEqual(result1, ['line 1', 'line 3'], 'Document was not \
successfully altered!')
        
        # Log check.
        result2 = self.actions.stack
        self.assertEqual(result2, [['D', 'line 2', 1]], 'Undo log was not \
successfully altered!')
        
        return
    
    def testValueError(self: 'testDelete') -> None:
        ''' Attempt to catch ValueError.
        '''
        
        # Assuming user gives invalid input of '2.0'.
        value = input(number_prompt + "(VE) ")
        delete_line(self.test_document, self.actions, value)
        
        self.assertRaises(ValueError) 
        
        return
    
    def testIndexError(self: 'testDelete') -> None:
        ''' Attempt to catch IndexError.
        ''' 
        
        # Assuming user gives invalid input of '9'.
        value = input(number_prompt + "(IE) ")
        delete_line(self.test_document, self.actions, value)
        
        self.assertRaises(IndexError)
        
        return 
    
    def testelement_of_NError(self: 'testDelete') -> None:
        ''' Catch if input is less than one.
        ''' 
        
        # Assuming user gives invalid input of '0'.
        value = input(number_prompt + "(N)")
        delete_line(self.test_document, self.actions, value)
        
        self.assertRaises(element_of_N)
        
        return 
    
class testLog(unittest.TestCase):
    ''' Test methods of stack class Log.
    ''' 
    
    def setUp(self: 'testLog') -> None:
        ''' Set up variables to start testing this class' methods.
        '''
        
        self.stack = Log() 
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)        
        
        return
    
    def tearDown(self: 'testLog') -> None:
        ''' Reset the elements of the stack to 0 to avoid overlapping and
        incorrect updating of stacks.
        '''
        
        while len(self.stack.stack) != 0:
            self.stack.pop()
        
        return 
    
    def testPop(self: 'testLog') -> None:
        ''' Remove the most recently added item.
        ''' 
        
        self.stack.pop()        
        self.assertEqual(self.stack.stack, [1, 2], \
                         'Popping most recent item failed!')
        
        return 
    
    def testPush(self: 'testLog') -> None:
        ''' Add an item to the end of the stack (list).
        ''' 
        
        self.stack.push(4)
        self.assertEqual(self.stack.stack, [1, 2, 3, 4], \
                         'Failed to append item!')
        
        return
    
    def testIs_EmptyF(self: 'testLog') -> None:
        ''' Check if stack is empty (F).
        ''' 
        
        # Checking if it can identify being non-empty. 
        result1 = self.stack.is_empty()
        self.assertEqual(result1, False, empty_stack_conf)
        
    
    def testIs_EmptyT(self: 'testLog') -> None: 
        ''' Check if stack is empty (T).
        '''
        
        # Checking if it can identify being empty. 
        self.stack.stack = []
        result2 = self.stack.is_empty()
        self.assertEqual(result2, True, empty_stack_conf)
        
        return
#-------------------------------------------------------------------------------

## Main Program
# Execute unittest.
if __name__ == '__main__':
    unittest.main()