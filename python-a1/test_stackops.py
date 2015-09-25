## Date: February 4, 2015
## Author(s): Suleiman Mirza
#-------------------------------------------------------------------------------

## Central Program
# Imported Modules
import unittest
from stackops import *
from stack import *

# Helper Functions
def add_items(s: 'Stack', n: int) -> None:
    ''' Add whole values of 1 to n inclusive to stack s in ascending order.
    
    >>> s = Stack()
    >>> s.items
    []
    >>> add_items(s, 4)
    >>> s.items
    [1, 2, 3, 4]
    ''' 
    
    counter = 1
    while counter <= n:
        s.push(counter)
        counter += 1 
    
    return

# Testing Classes 
class testSwap(unittest.TestCase):
    ''' Test the swap method for exchanging top two items.
    ''' 
    
    def setUp(self: 'testSwap') -> None:
        ''' Initialize object as fresh stack for testing.
        '''
        self.stack = Stack() 
        
        return
    
    def tearDown(self: 'testSwap') -> None:
        ''' Remove all items in subject to avoid erronous overlap.
        '''
        
        while self.stack.size() > 0:
            self.stack.pop()
        
        return 
    
    def testItemLengthSmall(self: 'testSwap') -> None:
        ''' Valid stack size of 4.
        ''' 
        
        add_items(self.stack, 4)
        swap(self.stack)
        
        self.assertEqual(self.stack.items, [1, 2, 4, 3], 'Stack not swapped!')
        
        return
    
    def testItemLengthLarge(self: 'testSwap') -> None:
        ''' Valid stack size of 15.
        ''' 
        
        s_15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14] 
        add_items(self.stack, 15)
        swap(self.stack)
        
        self.assertEqual(self.stack.items, s_15, 'Stack not swapped!')
        
        return 
    
    def testNotEnoughItems(self: 'testSwap') -> None:
        ''' Lacking the minium 2 items to swap in stack s.
        ''' 
        
        add_items(self.stack, 1)
        swap(self.stack) 
        
        self.assertEqual(self.stack.items, [1], 'Stack not swapped!')
        
        return
    
    def testEmptyStack(self: 'testSwap') -> None:
        ''' Empty stack test.
        ''' 
        
        swap(self.stack)
        self.assertEqual(self.stack.items, [], 'Stack not swapped!')
        
        return 
    
class testRoll(testSwap):
    ''' Test function roll. 
    
    Note: Inheriting from testSwap because same tearDown method.
    ''' 
    
    def testValidInputLarge(self: 'testRoll') -> None:
        ''' Valid 5-element stack to be rolled at position 4.
        ''' 
        
        add_items(self.stack, 5)
        roll(self.stack, 4)
        self.assertEqual(self.stack.items, [1, 3, 4, 5, 2], 'Incorrect roll!')
        
        return
    
    def testValidInputSmall(self: 'testRoll') -> None:
        ''' Valid 5-element stack to be rolled at position 2.
        ''' 
        
        add_items(self.stack, 5)
        roll(self.stack, 2)
        self.assertEqual(self.stack.items, [1, 2, 3, 5, 4], 'Incorrect roll!')
        
        return 
    
    def testFirstElementRoll(self: 'testRoll') -> None:
        ''' Test if roll at element that is already at the top of the stack.
        ''' 
        
        add_items(self.stack, 5)
        roll(self.stack, 1) 
        # No change is expected.
        self.assertEqual(self.stack.items, [1, 2, 3, 4, 5], 'Incorrect roll!')
        
        return
    
    def testLastElementRoll(self: 'testRoll') -> None:
        ''' Test the last element's roll.
        ''' 
        
        add_items(self.stack, 5)
        roll(self.stack, 5)
        self.assertEqual(self.stack.items, [2, 3, 4, 5, 1], 'Incorrect roll!')
        
        return 
    
    def testEmptyStack(self: 'testRoll') -> None:
        ''' Test if stack is empty.
        ''' 
        
        roll(self.stack, 1)
        self.assertEqual(self.stack.items, [], 'Incorrect roll!')
        
        return
    
    def testOneElements(self: 'testRoll') -> None:
        ''' Test if stack does not have required number of items to roll.
        ''' 
        
        self.stack.push(1)
        roll(self.stack, 1)
        self.assertEqual(self.stack.items, [1], 'Incorrect roll!')
        
        return 
    
    def testInvalidn(self: 'testRoll') -> None:
        ''' Test if n exceeds amount of items in stack.
        ''' 
        
        add_items(self.stack, 5)
        roll(self.stack, 10)
        self.assertEqual(self.stack.items, [1, 2, 3, 4, 5], 'Incorrect roll!')
        
        return
#-------------------------------------------------------------------------------

## Main Program
# Execute unittest.
if __name__ == '__main__':
    unittest.main()