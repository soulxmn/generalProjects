## Date: February 4, 2015
## Author(s): Suleiman Mirza
#-------------------------------------------------------------------------------

## Central Program
# Imported Modules
import string
from letter_manager import LetterManager 

# Main Function
def main(word1: str, word2: str) -> bool and str: 
    ''' Return wheter 2 words are anagrams of each other, and false if either
    contains non-alphabetical characters. 
    
    >>> main('horse', 'shore')
    True
    'These two words are anagrams of each other!'
    >>> main('horse9, 'sh   ore')
    False
    'Invalid input was given.'
    '''
    
    word3 = word1 + word2
    # This checks against empty strings.
    if len(word1) != 0 and len(word2) != 0:
        for ch in word3:
            # This checks against spaces, punctuation, numbers, and symbols.
            if ch not in string.ascii_lowercase:
                print('Invalid input was given.')
                return False 
    else:
        print('Invalid input was given.')
        return False
        
    W1 = LetterManager(word1)
    W2 = LetterManager(word2) 
    # Checking if number of letters and their occurrences match.
    if W2.letters_count == W1.letters_count:
        print('These two words are anagrams!')
        return True
    else:
        print('These two words are not anagrams!')
    
    return
#-------------------------------------------------------------------------------

## Main Program
# Execution Code
if __name__ == '__main__':
    print('Welcome to this program! Type 2 words when prompted to check if \
they are anagrams. Type "run" to run the program, and "q" to exit.') 
    # Loop in case user wants to check more than just one pair of words.
    line = input('What would you like to do? ')
    while line != 'q':
        if line == 'run':
            word1 = input('What is your first word? ')
            word2 = input('Your second? ') 
            main(word1, word2)
        elif line == 'q':
            print('Thanks for using!')
            quit() 
        else:
            print("Sorry, that's not a valid command!")
        line = input('What would you like to do? ') 
#-------------------------------------------------------------------------------