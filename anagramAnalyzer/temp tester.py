list1 = ['bca', 'cba', '0', 'abc']
list2 = ['cba', 'abc', 'bca', '0']
print(sorted(list1) == sorted(list2))

word1 = 'oh'
word2 = 'hello'
if word1 in word2:
    print('Success!') 

list1.pop(list1.index('cba'))
print(list1) 

list1 = []
list1 += list2
list1.append(9)
print(list1)
print(list2)

list1 = [0, 1, 1]
list2 = [0, 2, 0]
print(list1 < list2) 

lst1 = ['hi', 'hello']
cWord = lst1[0]
lst1 = []
print(cWord)

cond = ''
temp = ['hi', 'hello']
for word in temp:
    cond += word
wordDict = ['a', 'b', 'hi', 'hello', 'z']
ind = wordDict.index(temp[-1])
temp[-1] = wordDict[ind + 1]
print(temp[-1])
print(cond)


###********************TEMPORARY STORAGE**********************###       1
#for wordLog in logs[word]:
## Guaranteed to work on first run, due to nature of dictionary.
#if phraseLog.Subtract(logs[word]) != None:
  ##temp.append(word) 
  #temp.append(containsConf.__str__())
  #if containsConf.Size() > 0:
    ### Reduce processing time further at each recursion level.
    ##remains2 = dictionary.pop(dictionary.index(word))
    #finder(containsConf, dictionary)
#temp.append('M0') 

###********************TEMPORARY STORAGE**********************###       2
#if len(temp) != 0:
  #cLetters = phraseLog.Subtract(logs[temp[0]].Add(logs[temp[1]]))
  #if cLetters != None:
    #tempN = sum(cLetters.counts)

#for word in logs: 
  #if word not in temp:
    #if len(temp) != 0:
      #if tempN <= sum(phraseLog.counts):
        #temp.append(word) 
    #else:
      #temp.append(word)
      #cLetters = sum(phraseLog.Subtract(logs[word]))

  #finder(phraseLog, logs)