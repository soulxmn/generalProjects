import unittest
from poetry_functions import check_syllables

# Global variables to avoid repetitve code.
poem_lines = ['The first line leads off,', 'With a gap before the next.', \
              'Then the poem ends.']
pattern = ([5, 5, 4], ['*', '*', '*'])
word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                    'GAP': ['G', 'AE1', 'P'],
                    'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                    'LEADS': ['L', 'IY1', 'D', 'Z'],
                    'WITH': ['W', 'IH1', 'DH'],
                    'LINE': ['L', 'AY1', 'N'],
                    'THEN': ['DH', 'EH1', 'N'],
                    'THE': ['DH', 'AH0'], 
                    'A': ['AH0'], 
                    'FIRST': ['F', 'ER1', 'S', 'T'], 
                    'ENDS': ['EH1', 'N', 'D', 'Z'],
                    'POEM': ['P', 'OW1', 'AH0', 'M'],
                    'OFF': ['AO1', 'F']} 

class Test_check_syllables(unittest.TestCase):
    def test_partial_syllables(self):
        ''' Test for some lines having the correct number of syllables, and 
        some not having the correct number of syllables.
        '''
        returned = check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['With a gap before the next.', 'Then the poem ends.'] 
        self.assertEqual(returned, expected, 'Expected value not returned.') 
    
    def test_all_correct_syllables(self):
        ''' Test for all lines having the correct number of syllables.
        '''
        pattern = ([5, 7, 5], ['*', '*', '*'])
        returned = check_syllables(poem_lines, pattern, word_to_phonemes) 
        expected = []
        self.assertEqual(returned, expected, 'Expected value not returned.')  
    
    def test_all_incorrect_syllables(self):
        ''' Test for all lines having an incorrect number of syllables.
        '''
        poem_lines = ['The first line leads a gap,', \
                      'With a gap before the next.', \
                      'Then the poem ends.'] 
        pattern = ([4, 5, 4], ['*', 'A', 'B'])
        returned = check_syllables(poem_lines, pattern, word_to_phonemes)
        self.assertEqual(returned, poem_lines, 'Expected value not returned.')
    
    def test_empty_str(self): 
        ''' Test if there is only one line, which is empty, and does not contain
        the correct number of syllables.
        '''
        poem_lines = ['']
        pattern = ([5], ['A'])
        returned = check_syllables(poem_lines, pattern, word_to_phonemes)
        self.assertEqual(returned, poem_lines, 'Expected value not returned.') 
    
    def test_no_req(self):
        ''' Test if there is no requirement on the number of syllables in each
        line.
        '''
        pattern = ([0, 0, 0], ['*', '*', '*'])
        returned = check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(returned, expected, 'Expected value not returned.') 
    
    def test_mixed_reqs(self): 
        ''' Test if some lines require syllables, but some do not.
        '''
        pattern = ([4, 7, 0], ['*', '*', '*'])
        returned = check_syllables(poem_lines, pattern, word_to_phonemes) 
        expected = ['The first line leads off,']
        self.assertEqual(returned, expected, 'Expected value not '\
                         + 'returned')
        
        
unittest.main(exit=False)
