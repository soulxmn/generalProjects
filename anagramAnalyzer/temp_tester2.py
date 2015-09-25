## File Information
#**********************************************************
# Assignment 2 - Recursion and Backtracking 
# CSC148H5-S: LEC0101 [Tiffany Tong]
# mirzasul
# Suleiman 
# Mirza
# 1001633155
# 22:00 5/3/2015
# 
# Honour Code: I pledge that this program represents my own 
# program code and that I have coded on my own. I received
# help from no one in designing and debugging my program.
# I have also read the plagiarism section in the course info 
# sheet of CSC 148 and understand the consequences. 
#*********************************************************

## Module(s)
import unittest
from anagram import *


## Global Settings
# Create the list of words from dictFile.
dictFile = "dict.txt"
file = open(dictFile, "r")
anagramDict = [] 
line = file.readline()
while line != "":
  # Ignore '\n' character at end.
  anagramDict.append(line[:-1])
  line = file.readline()
file.close() 


## Main Class(es) and Program
class testAnagramSolver(unittest.TestCase):
  ''' Test the class AnagramSolver for regular forms of input.
  
  Note: An error will always be raised because one of the tests is to ensure
  ValueError is raised. Which it will be when it is tested for it.
  '''  
  
  def tearDown(self: "testAnagramSolver") -> None:
    ''' Tear down each function to reset it so that no data overlaps.
    ''' 
    
    x = AnagramSolver(anagramDict)
    
    return
  
  def testOneWordAnagram(self: "testAnagramSolver") -> None:
    ''' Test for when the function is trying to solve an anagram for only 
    one word. 
    
    This test is necessary to ensure that the function can solve both phrases 
    and single words.
    ''' 
    
    x = AnagramSolver(anagramDict)
    y = x.generateAnagrams('hello', 5)    
    self.assertEqual(y, [['hello']], 'Output incorrect!') 

    return   
  
  def testNoLimit(self: "testAnagramSolver") -> None:
    ''' Test when maxWords is set to 0.
    
    This is necessary to ensure the function knows when not to limit the number
    of anagrams in it's result. This test also checks for alphabetical 
    organization, due to the nature of the list when equating two.
    ''' 
    
    x = AnagramSolver(anagramDict)
    s = 'office key'    
    maxWords = 0
    y = x.generateAnagrams(s, maxWords) 
    self.assertEqual(y, [['eke', 'icy', 'off'], \
                       ['eke', 'off', 'icy'], \
                       ['ice', 'key', 'off'], \
                       ['ice', 'off', 'key'], \
                       ['icy', 'eke', 'off'], \
                       ['icy', 'off', 'eke'], \
                       ['key', 'ice', 'off'], \
                       ['key', 'off', 'ice'], \
                       ['key', 'office'], \
                       ['off', 'eke', 'icy'], \
                       ['off', 'ice', 'key'], \
                       ['off', 'icy', 'eke'], \
                       ['off', 'key', 'ice'], \
                       ['office', 'key']], 'Output incorrect!')
    
    return
  
  def testLimit(self: "testAnagramSolver") -> None:
    ''' Test when maxWords is set to a positive number.
    
    This test is to ensure the function can effectively set a limit as to how
    many anagrams it returns as a response. Additionally, it indirectly checks
    to see if the function returns anagrams of the full-phrase (which is 
    correct) as opposed to only a part of the phrase (which is incorrect) when
    given a limit.
    ''' 
    
    x = AnagramSolver(anagramDict)
    s = 'office key'     
    maxWords = 2
    y = x.generateAnagrams(s, maxWords)
    self.assertEqual(y, [['key', 'office'], \
                        ['office', 'key']], 'Output incorrect!') 
    
    return
  
  def testInvalidInput(self: "testAnagramSolver") -> None:
    ''' Test for when maxWords is set to a negative number.
    
    This test is necessary to ensure that the function differentiates between
    trying to get a specific number of anagram sets, and trying to get 
    an impossible number of anagram sets.
    ''' 
    
    x = AnagramSolver(anagramDict)
    s = 'office key'     
    maxWords = -1
    y = x.generateAnagrams(s, maxWords)
    self.assertRaises(ValueError)
    
    return 
  
  def testNoWordAnagram(self: "testAnagramSolver") -> None:
    ''' Test for when there is no word input given.
    
    This test is necessary to determine if the function can respond 
    appropriately to invalid input, instead of just breaking.
    ''' 
    
    x = AnagramSolver(anagramDict)
    s = ''
    maxWords = 0
    y = x.generateAnagrams(s, maxWords)
    self.assertEqual(y, [], 'Output incorrect!')
    
    return
  
  def testNoDictionary(self: "testAnangramSolver") -> None:
    ''' Test for when there is no dictionary to check phrase against.
    
    This test ensures the function can still work and will not break if no
    dictionary is given. The function should still run through its recursive
    tests and simply return an empty set of anagrams.
    '''
    
    x = AnagramSolver(anagramDict)
    s = 'office key'
    maxWords = 10
    temp_dict = []
    x = AnagramSolver(temp_dict)
    y = x.generateAnagrams(s, maxWords)
    self.assertEqual(y, [], 'Output incorrect!') 
    
    return
  
  def testOneWordDictionary(self: "testAnagramSolver") -> None:
    ''' Test to see if the function works correctly.
    
    This test ensures the function can still process successfully a phrase or
    word without encountering problems such as index errors or assignment
    errors while working with a dictionary of length 1.
    ''' 
    
    x = AnagramSolver(anagramDict)
    
    # Test for when the word is not in dictionary.
    s = 'hi'
    maxWords = 0
    temp_dict = ['hello']
    x = AnagramSolver(temp_dict)
    y = x.generateAnagrams(s, maxWords)
    self.assertEqual(y, [], 'Output incorrect!') 
    
    # Test for when the word is in dictionary.
    temp_dict = ['hi']
    x = AnagramSolver(temp_dict)
    y = x.generateAnagrams(s, maxWords)
    self.assertEqual(y, [['hi']], 'Output incorrect!')
    
    return 
  
  def testOneLetterWord(self: "testAnagramSolver") -> None:
    ''' Test for inputting a one-letter word (such as 'a', or 'I').
    
    A good test to see if the function experiences any index or assignment 
    errors, or to see if it can work correctly despite having nothing to 
    traverse.
    '''
    
    g = anagramDict[:]
    g.append('i')
    x = AnagramSolver(sorted(g))
    y = x.generateAnagrams('I', 0)
    self.assertEqual(y, [['i']], 'Output incorrect!')
    
    return

# Execute unittest.
if __name__ == '__main__':
    unittest.main()
    
## Reasoning for Implementation
''' 
I believe these tests are sufficient for checking to see if the function works
successfully, due to the fact that there are not a lot of things to test on.

The LetterManager class was writ by another person, so the ability to check 
if the main program identifies and doesn't break from punctuation, numbers, 
symbols, and other non-alphabetic characters doesn't test the sturdiness of the
function I wrote. 
Furthermore, other than these 3 cases, the most one could do is test for a 
multiple phrase anagram, but tests testOneWordAnagram and testNoLimit already 
cover this. Simply increasing the number won't test anything new if the base 
cases are already tested. 
You could also test words that are anagrams of one-letter words, like 'a', but
that will not make any sense unless the word itself is an anagram of itself.
Finally, the last thing left to test would be the maxWords parameter, in which 
we have three cases. If it's 0, has an upper limit, or if it can't process 
because it's negative (all three are tested above).  

Because of these reasons, I feel that there isn't a whole lot left to test on
other than the basic invalid input tests I've done above. So, by process of 
elimination, the above test cases are sufficient to conclude that my program 
works successfully.
'''