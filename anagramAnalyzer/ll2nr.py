## File Information
#**********************************************************
# Assignment 2 - Recursion and Backtracking 
# CSC148H5-S: LEC0101 [Tiffany Tong]
# 22:00 2/3/2015
# 
# Honour Code: I pledge that this program represents my own 
# program code and that I have coded on my own. I received
# help from no one in designing and debugging my program.
# I have also read the plagiarism section in the course info 
# sheet of CSC 148 and understand the consequences. 
#*********************************************************


## Module(s)
from nodesrefs import BinaryTree

# To avoid confusion about what constitutes an empty tree, this tuple has both.
empty_tree = ([], None) 

## Main Function(s) and Program
def ll2nr (l):
  ''' (list of lists) -> "Binary Tree" class with multiple .____
  
  Convert a binary tree in a list of lists representation into a nodes
  and references form, where each .____ is assigned using the BinaryTree class.  
  
  A short explanation: By taking 'right path' or 'left path' what I mean is 
  passing in that value again into this function, except now since we're looking 
  at a tree, we will eventually reduce to a single list of elements 
  (which are not lists). And then that will go to just values which are None or 
  something else. By saying None, we cover the part where it is a list or it is
  something else. At that point, I just put in the appropriate values from the 
  class.
  
  Note: Here [] means there is nothing there, equivalent to None. The lecture
  slides showed None but some students said they would be represented by [], so
  I just put both for now.
  '''
  
  # Real base case: turning it into a Binary Tree. This is on default because
  # we have to come here.
  # Initially convert the very first root to a binary tree of a list. It doesn't
  # matter about the other elements because the first must always be the root 
  # node, and therefore holds a value for sure.
  greaterTree = BinaryTree(l[0])
  
  # Below are the different 'secondary' base cases:
  # If both are nodes, then pass in both at the same time.
  if l[1] not in empty_tree and l[2] not in empty_tree:
    greaterTree.left = ll2nr(l[1])
    greaterTree.right = ll2nr(l[2]) 

  # If the left is a node and the right is not, then take the right path.
  elif l[1] in empty_tree and l[2] not in empty_tree:
    greaterTree.right = ll2nr(l[2]) 
    
  # If the left is not a node and the right is, then take the left path.
  elif l[1] not in empty_tree and l[2] in empty_tree:
    greaterTree.left = ll2nr(l[1])    
   
  # If both sides are empty trees, then we give the root. This will slowly trace 
  # back to the above statement, giving them 'root' values throughout.
  elif l[1] in empty_tree and l[2] in empty_tree:
    return greaterTree.getRootValue()  
  
  # Final output - literally returning instance because no rep method in class.
  return greaterTree
