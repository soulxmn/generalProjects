## File Information
#**********************************************************
# Assignment 2 - Recursion and Backtracking 
# CSC148H5-S: LEC0101 [Tiffany Tong]
# mirzasul
# Suleiman 
# Mirza
# 1001633155
# 22:00 2/3/2015
# 
# Honour Code: I pledge that this program represents my own 
# program code and that I have coded on my own. I received
# help from no one in designing and debugging my program.
# I have also read the plagiarism section in the course info 
# sheet of CSC 148 and understand the consequences. 
#*********************************************************


## Module(s)
from letterManager import * 
from itertools import permutations


## Helper Function(s)
def finder(phraseLog: "LetterManager", wordDict: list, temp: list, \
           tempS: list=[]) -> list:
  ''' Pre-condition: dictionary is in alphabetical order, temp is provided with
  at least one element, and tempS is empty.
  
  Return a sorted list of at least one combination of elements from dictionary 
  that create phrase inclusive of duplicates, given they are in a different 
  order.

  >>> dictionary = ['hell', 'hello', 'oh', 'wrong']
  >>> phrase = 'hello'
  >>> finder(phrase, dictionary, ['placeholder'])
  [['hello']]
  ''' 
  
  # Recursive path (initial run).
  if len(temp) != 0: 
    
    # Current count of letters in an element of tempS. 
    combinedWord = ''
    for word1 in temp:
      combinedWord += word1 
    tempWord = LetterManager(combinedWord)
    tempN = phraseLog.Subtract(tempWord) 
    
    # Checking if currentWord has cycled through all potential combinations.
    if len(temp) > 1:
      counter = 0
      for word2 in temp[1:]:
        if word2 == wordDict[-1]:
          counter += 0
        else:
          counter += 1      
          
    # Avoiding 'calling variable before assignment' error.
    else:
      counter = 1
    
    # Base case 1: last word traversed (actual base case in terms of 
    # recursion).
    if counter == 0 and temp[0] == wordDict[-1]:
      if not tempN == None and sum(tempN.counts) == 0:
        tempS.append(temp)
      
      return tempS 
    
    # Base case 2: anagram not made, word incompatible.        
    elif tempN == None and temp[-1] != wordDict[-1]:
      # Move on to the next word to compare with current. 
      ind = wordDict.index(temp[-1]) + 1
      temp[-1] = wordDict[ind]
    
    # Base case 3: anagram not made, word incompatible, wordDict traversed 
    # entirely.
    elif tempN == None and counter == 0 and temp[0] != wordDict[-1]:
      ind1 = wordDict.index(temp[0]) + 1
      temp = []
      temp.append(wordDict[ind1])      
      
    # Base case 4: anagram not made, word incompatible, wordDict traversed for 
    # current word.
    elif tempN == None and temp[-1] == wordDict[-1] and \
         len(temp) > 1: 
      temp.pop()
      temp[-1] = wordDict[(wordDict.index(temp[-1])) + 1] 
    
    # Base case 5: traversing wordDict using last word as currentWord.
    elif tempN == None and temp[0] == wordDict[-1]:
      if len(temp) == 1:
        temp.append(wordDict[0])
      else:
        ind = wordDict.index(temp[-1]) + 1
        temp[-1] = wordDict[ind]       
    
    # Base case 6: anagram made
    elif sum(tempN.counts) == 0:  
      # Add anagram set to temporary storage. 
      x = temp[:]
      if sorted(x) not in tempS:
        tempS.append(x) 
      if counter == 0:
        # Move current word one further down the wordDict.
        currentWord = temp[0]
        temp = []
        temp.append(wordDict[wordDict.index(currentWord) + 1])  
      elif temp[-1] != wordDict[-1]:
        ind1 = wordDict.index(temp[-1]) + 1
        temp[-1] = wordDict[ind1]
      elif temp[-1] == wordDict[-1]:
        temp.pop()
        temp[-1] = wordDict[(wordDict.index(temp[-1])) + 1]
   
    # Base case 7: anagram not made, word compatible.
    elif sum(tempN.counts) > 0:   
      # Record next word in wordDict, keeping previous one.
      if len(temp) == 1:
        temp.append(wordDict[0]) 
      # To avoid calculating unnecessary combinations, we will simply begin 
      # from the next word to follow. Previous iterations will cover any cases
      # in which the same anagram set has already been calculated, but in a 
      # different order.
      else:
        temp.append(wordDict[(wordDict.index(temp[-1]))]) 
        
    # Call the function on itself again, having altered its lists.
    finder(phraseLog, wordDict, temp, tempS) 
  
  # Pass to generateAnagrams call.
  return tempS
 
 
## Main Class(es) and Program
class AnagramSolver(object):
  def __init__ (self: "AnagramSolver", listOfWords: list) -> None:
    ''' Create inventories for a dictionary.
    
    >>> test1 = AnagramSolver(['hell', 'oh', 'hello'])
    >>> test1.dictWords
    ['hell', 'hello', 'oh']
    '''
    
    self.dictWords = sorted(listOfWords)  
    self.anagrams_dict = {}
    for word in self.dictWords:
      wordLog = LetterManager(word)
      # For later comapring sum of elements to log of phrase. 
      self.anagrams_dict[word] = wordLog 
    
    # Resetting values to avoid copying over into other test cases later.
    def reset(self):
      self.results = 0
    
    # Reset data at each instance call.
    self.reset = reset
    
    return    
    
  def generateAnagrams (self: "AnagramSolver", s: str, max: int) -> list:
    ''' Pre-condition: max is positive or 0. 
    
    Returns all combinations of words from dictionary attribute that are  
    anagrams of string s, at length mWords. Raises an exception if max is less 
    than 0, and defaults to unlimited number of words per anagram set, 
    if equating to 0. 
    
    Each anagram set will be a list of words making up the entire phrase s, and
    also an element of a larger list comprising of all these anagram sets. All 
    lists involved are in alphabetical order.
    
    >>> test1 = AnagramSolver(['home', 'lock', 'look', 'heck', 'loom', 'hole' 
                               'mock', 'oh', 'me', 'moo', 'mole', 'come' 'eh'
                               'cool', 'cook'])
    >>> test1.generateAnagrams("home lock", 0)
    [['heck', 'loom'], ['hole', 'mock'], ['home', 'lock'], ['lock', 'heck'], 
    ['lock', 'home'], ['mock', 'hole'], 'oh', 'me', 'lock']]
    ''' 
    
    # Test against basic invalid inputs to keep code robust and avoid
    # internal processing errors.
    if len(s) == 0 or len(self.dictWords) == 0:
      return [] 
    
    if max < 0:
      print('Max value cannot be negative!')
      raise ValueError   
    
    if len(self.dictWords) == 1: 
      if s == self.dictWords[0]:
        return [[s]]
      else:
        return [] 
    
    if len(s) == 1:
      if s in self.dictWords:
        return [[s.lower()]]
      else:
        return []
    
    results = []
    result = []
    
    # Reduce dictionary.
    s = LetterManager(s)
    new_dict = [] 
    for word in self.dictWords:
      if s.Subtract(self.anagrams_dict[word]) != None:
        new_dict.append(word.lower())
    
    test1 = []
    test1.append(sorted(new_dict)[0])
    temp = finder(s, sorted(new_dict), test1) 
    
    # Generate the combinations
    for lst in temp:
      y = [x for x in permutations(lst)] 
      for lst2 in y:
        lst3 = list(lst2[:])
        result.append(lst3)
    anagramCombos = sorted(result)
    
    if max == 0:
      for element in anagramCombos:
        results.append(element)
        
    else:
      for element in anagramCombos:
        if not len(element) > max:
          results.append(element) 
    
    self.results = sorted(results)
    
    return self.results