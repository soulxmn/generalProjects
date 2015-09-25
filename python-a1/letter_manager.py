## Date: February 4, 2015
## Author(s): Suleiman Mirza
#-------------------------------------------------------------------------------

## Central Program
# Imported Modules
import string

# Helper and Exception Functions
def non_letter_Exception(letter) -> None or Exception:
    ''' Raise the non_letter exception class if letter is not part of the
    alphabet, regardless of case.
    
    >>> non_letter_Exception('!')
    __main__.non_letter: 
    >>> non_letter_Exception('h')
    >>> 
    '''
    
    if letter not in string.ascii_letters and len(letter) != 1:
        raise non_letter
    
    return

# Program and Exceptions Classes
class LetterManager(object):
    ''' Keep count of letters and retrieve information of a given string.
    ''' 
    
    def __init__(self: 'LetterManager', s: str) -> None:
        ''' Log all occurrences of letters in s.
        ''' 
        
        # Initialize the 26 counters for the list.
        letters_count = []
        for ch in string.ascii_lowercase:
            letters_count.append(0)
        
        # Each indice corresponds to the correct letter in alphabetical order.
        for ch in s:
            if ch.lower() in string.ascii_lowercase: 
                ind_num = string.ascii_lowercase.index(ch.lower())
                letters_count[ind_num] = s.count(ch)
               
        self.letters_count = letters_count
        self.size = sum(self.letters_count)
        
        return 
    
    def Get(self: 'LetterManager', letter: str) -> int or Exception: 
        ''' Return a count of how many occurrences of letter were logged.
        
        >>> s = 'hello'
        >>> test1 = LetterManager(s)
        >>> test1.Get('l')
        2
        ''' 
        
        try:
            # Testing for invalid character.
            non_letter_Exception(letter)
            x = self.letters_count[string.ascii_lowercase.index(letter.lower())]
        except non_letter:
            print('The character passed in was not a letter.')
        else:
            return x
        
        return 
    
    def Set(self: 'LetterManager', letter: str, value: int) -> None:
        ''' Set the number of logged occurrences of letter to value.
        
        >>> test1 = LetterManager('aaa')
        >>> test1.Set('a', 2)
        >>> test1.letters_count('a')
        2        
        '''
        
        try: 
            # letter test.
            non_letter_Exception(letter) 
            # value test.
            int(value)
        except ValueError:
            print('The value passed in was not an integer.')
        except non_letter:
            print('The character passed in was not a letter.')
        else:
            ind = string.ascii_lowercase.index(letter.lower())
            self.letters_count[ind] = value  
            # Update size of counters.
            self.size = sum(self.letters_count)
                    
        return
    
    def Size(self: 'LetterManager') -> int:
        ''' Return the sum of the occurrences of each letter from s.
        
        >>> test1.LetterManager('aabbc')
        >>> test1.Size()
        5
        ''' 
        
        return self.size 
    
    def IsEmpty(self: 'LetterManager') -> bool:
        ''' Return True iff all letter occurrences are 0.
        
        >>> test1.LetterManager('')
        >>> test1.IsEmpty()
        True
        ''' 
        
        return self.size == 0 
    
    def __str__(self: 'LetterManager') -> str:
        ''' Return a string representation of the letter counts in alphabetical
        order.
        
        >>> test1.LetterManager('hellohi')
        >>> test1
        '[ehhillo]'
        ''' 
        
        self.characters = ''
        for ind in range(len(self.letters_count)):
            if self.letters_count[ind] != 0:  
                # Repeatedly add into string until count has reached 0.
                i = self.letters_count[ind]
                while i != 0:
                    self.characters += string.ascii_lowercase[ind] 
                    i -= 1
        
        # Return with brackets.
        return '[' + self.characters + ']'
    
    def Add(self: 'LetterManager', other: 'LetterManager') -> 'LetterManager':
        ''' Return a new 'LetterManager' object whose counts are added together
        with those of other.
        
        >>> test1 = LetterManager('aabbcc')
        >>> test2 = LetterManager('ccddee')
        >>> test1.Add(test2)
        <class '__main__.test3'>
        >>> test3
        '[aabbccccddee]'
        ''' 
        
        # Simply add their strings together. The class will order it  
        # alphabetically, and reasses their now combined counts.
        temp_1 = self.__str__()
        temp_2 = other.__str__()
        new_s = temp_1[1:-1] + temp_2[1:-1]
        new_LM = LetterManager(new_s)
        
        return new_LM 
    
    def Subtract(self: 'LetterManager', other: 'LetterManager') -> \
        'LetterManager' or None:
        ''' Return a third object of type 'LetterManager' whose counters are the
        result of subtracting the other's count from self's count. Return None
        if any of the counts result in a negative.
        
        >>> test1 = LetterManager('aabbcc')
        >>> test2 = LetterManager('ccddee')
        >>> test1.Subtract(test2)
        <class '__main__.test3'> 
        >>> test3
        '[aabbddee]'
        '''
        
        # Each count will be redefined later.
        new_LM = LetterManager('')
        for i in self.letters_count:
            new_LM.letters_count[i] = (self.letters_count[i] - \
                                       other.letters_count[i]) 
            
            # Check right away if the number is negative, instead of doing all 
            # possible 26 calculations and then going back and checking each.
            if new_LM.letters_count[i] < 0:
                return None
        
        return new_LM
    
    
class non_letter(Exception):
    pass
#-------------------------------------------------------------------------------