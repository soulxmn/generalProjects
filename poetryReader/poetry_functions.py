"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

## ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result

def cleaned_up_list(lines):
    r""" (list of str) -> list of list of str
    
    Precondition: lines must have at least 1 string element.
    
    Return a list in which each element is a list of words in each line in 
    lines that has been stripped of punctuation from both sides and made 
    uppercase. 
    
    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.'] 
    >>> cleaned_up_list(poem_lines)
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'], ['THEN', 'THE', 'POEM', 'ENDS']]
    """
    
    # Ensures each line is distinguished by creating a list for its words.
    new_poem_lines = []
    for ch in lines: 
        temp = ch.split()
        new_poem_lines.append(temp)
    
    # Applies clean_up on every element within each element of new_poem_lines.
    for element in new_poem_lines: 
        for word in range(len(element)):
            element[word] = clean_up(element[word]) 
    
    return new_poem_lines

# ===================== Required Functions =====================

def count_lines(lst):
    r""" (list of str) -> int

    Precondition: each str in lst[:-1] ends in \n.

    Return the number of non-blank, non-empty strings in lst.

    >>> count_lines(['The first line leads off,\n', '\n', '  \n',
    ... 'With a gap before the next.\n', 'Then the poem ends.\n'])
    3
    """ 
    
    # Removes the newline character to identify empty or blank strings.
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i].strip('\n')) 
    
    # Counts lines that are not empty, and consist of more than just whitespace.
    counter = 0
    for line in new_lst:
        if not line.isspace() and len(line) > 0:
            counter += 1

    return counter 

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed 
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
    
    # Separate lines based on the newline character.
    new_lst = []
    new_poem = poem # Avoid tampering with the original argument.
    for ch in new_poem:
        if ch == '\n':
            marker = new_poem.index('\n')
            new_lst.append(new_poem[:marker])
            new_poem = new_poem[marker+1:] # Updates line to make index  
                                           # access the next instance. 
                                           
    # Include last element if it does not have a newline character at the end. 
    if '\n' in poem:    # Ensure poem is not just one line.                   
        if poem[-1] != '\n':
            new_lst.append(poem[poem.rindex('\n')+1:])
    
    # Return lines that are not empty strings or only whitespace.
    result = []
    for element in new_lst:
        if element != '' and not element.isspace():
            result.append(element.strip())
            
    return result  

def check_syllables(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllables(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """ 
    
    npl = cleaned_up_list(poem_lines)
    
    # Add 1 if syllable is encountered. 
    counted_syllables = []
    for i in range(len(npl)):
        for j in range(len(npl[i])):
            if npl[i][j] in word_to_phonemes:
                for ch in word_to_phonemes[npl[i][j]]: 
                    if ch[-1] in '012':
                        counted_syllables.append(1)
        counted_syllables.append('marker') # Distinguish between lines.

    # Sum the 1s in list up until the next marker which separates the lines.
    syllables = []
    for ele in counted_syllables:
        if ele == 'marker':
            marker = counted_syllables.index(ele)
            syllables.append(sum(counted_syllables[0:marker]))
            counted_syllables = counted_syllables[marker+1:] 
    
    # Compare line syllables to the poetry pattern. 
    # Due to the precondition, one i suffices for all lists of the same length.
    results = []
    for i in range(len(syllables)):
        if pattern[0][i] != syllables[i] and pattern [0][i] != 0:
            results.append(poem_lines[i])
            
    return results 

def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    """ 
    
    npl = cleaned_up_list(poem_lines)
    
    # Creates list in which each element is the rhyme phoneme of the last word
    # of each line in poem_lines.
    rhymes = []
    for i in range(len(npl)):
        if npl[i][-1] in word_to_phonemes:
            temp = word_to_phonemes[npl[i][-1]]
            j = len(temp) - 1                  
            while j >= 0:                     # Loop backwards to get the last
                if temp[j][-1].isdigit():     # syllable, and append from there
                    rhymes.append(temp[j:])   # until the end (rhyme phoneme)
                    j = -1
                j -= 1
    
    # Create a key in the dictionary for every rhyme letter in pattern[1].
    rhyme_scheme = {}
    for element in pattern[1]:
        if element not in rhyme_scheme and element != '*':
            rhyme_scheme[element] = [] 
    
    # Append the rhyme of each line according to its rhyme letter in the 
    # dictionary, only if it is not already in there.
    for i in range(len(pattern[1])):
        if pattern[1][i] in rhyme_scheme and rhymes[i] not in \
           rhyme_scheme[pattern[1][i]]:
            rhyme_scheme[pattern[1][i]].append(rhymes[i]) 

    # Add the lines which do not rhyme with each other in results. The first 
    # element in each list in results will always be the rhyme letter.
    results = []
    for key in rhyme_scheme:
        results.append([])
        for i in range(len(rhymes)):
            if rhymes[i] in rhyme_scheme[key] and len(rhyme_scheme[key]) > 1:
                if results[-1] == []:
                    results[-1].append(key)  # Append rhyme letter to later
                if key == pattern[1][i]:     # order the results from the dict.
                    results[-1].append(poem_lines[i]) 
    
    # Order the results of the dictionary using the rhyme letter appended - 
    # sorted function only takes in the first element.
    results1 = [] 
    results = sorted(results)
    for element in results:
        if element != []:
            results1.append(element[1:]) 
            
    return results1 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
