## Date: February 4, 2015
## Author(s): Suleiman Mirza
#-------------------------------------------------------------------------------

## Central Program
# Imported Modules
from stack import *

# Functions
def swap (s):
  '''swap top two items on stack s'''
  
  if s.size() >= 2: 
    # Retrieve items to be swapped.
    top_item = s.items[-1]
    second_item = s.items[-2]
    
    # Remove both items.
    s.pop()
    s.pop()
    
    # Re-insert in opposite order.
    s.push(top_item)
    s.push(second_item) 
  
  else:
    print('An insufficient number of items were provided.')
  
  return

def roll (s, n):
  '''perform the roll operation on a stack s.
  A roll with integer n causes the nth item from the top to be removed
  and placed on top of the stack.''' 
  
  if s.size() >= n and n > 0:  
    # Retrieve item to be put on top (counting from index -1).
    going_to_the_top = s.items[-n] 
        
    # Re-assign each item such that the item previuosly retrieved is sent to the
    # second-from-the-top position.
    counter = -n
    while counter < -1: 
      s.items[counter] = s.items[counter + 1]
      counter += 1 
    
    # Add after, otherwise indices will be one off.
    s.push(going_to_the_top) 
    # Switch the places of the retrieved item with the previuosly top item.
    swap(s)     
    # Remove the previous top item (already copied in while loop).
    s.pop()
  
  else:
    print('An insufficient number of items were provided.') 
  
  return 
#-------------------------------------------------------------------------------