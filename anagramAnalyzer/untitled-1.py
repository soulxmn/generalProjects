dictFile = "dict.txt"
file = open(dictFile, "r")
anagramDict = [] 
line = file.readline()
while line != "":
  # Ignore '\n' character at end.
  anagramDict.append(line[:-1])
  line = file.readline()
file.close()  

from anagram import *

x = AnagramSolver(anagramDict)
y = x.generateAnagrams('hello', 0)
print(y)

x = AnagramSolver(anagramDict)
y = x.generateAnagrams('office key', 0)
print(y)