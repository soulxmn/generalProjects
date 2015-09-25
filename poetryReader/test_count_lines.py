import unittest
from poetry_functions import count_lines

class Test_count_lines(unittest.TestCase):
    def test_empty_lst(self):
        ''' Test for no lines being passed in.
        '''
        empty_lst = []
        returned = count_lines(empty_lst)
        self.assertEqual(returned, 0, 'value should be 0, but returned '\
                         + str(returned))
    
    def test_empty_strings(self):
        ''' Test for the last line being an empty string (this can only occur
        at the last line because of the precondition).
        '''
        empty_str_lst = ['testing\n', '']
        returned = count_lines(empty_str_lst)
        self.assertEqual(returned, 1, 'value should be 1 but returned '\
                         + str(returned))
    
    def test_blank_strings(self): 
        ''' Test for blank lines in the list of string.
        '''
        blank_str_lst = ['    \n', 'testing\n', '   ']
        returned = count_lines(blank_str_lst)
        self.assertEqual(returned, 1, 'value should be 1 but returned ' \
                         + str(returned))
    
    def test_last_no_newline_char(self): 
        ''' Test if the last line does not end with a newline character.
        '''
        last_no_newline_char_lst = ['test\n', 'another test\n', 'test'] 
        returned = count_lines(last_no_newline_char_lst)
        self.assertEqual(returned, 3, 'value should be 3, but returned '\
                         + str(returned)) 
    
    def test_only_newline_char(self): 
        ''' Test if all lines contain only newline characters, and thus, also if
        the last line ends with a newline character.
        '''
        only_newline_lst = ['\n', '\n', '\n', '\n']
        returned = count_lines(only_newline_lst)
        self.assertEqual(returned, 0, 'value should be 0, but returned '\
                         + str(returned))
    
    def test_punctuation(self): 
        ''' Test if each line contains punctuation regardless of grammatical
        correctness.
        '''
        punct_lst = ['testing!\n', ';;{]hello:)\n', '[]\\?last value!!!'] 
        returned = count_lines(punct_lst)
        self.assertEqual(returned, 3, 'value should be 3, but returned '\
                         + str(returned)) 
    
    def test_regular_input(self): 
        ''' Test a regular input in which all lines are non-blank, non-empty 
        strings and meet the precondition.
        '''
        normal_lst = ['Hello there!\n' ,'Hi, how are you?\n', \
                      "I'm fine thanks!"] 
        returned = count_lines(normal_lst)
        self.assertEqual(returned, 3, 'value should be 3, but returned '\
                         + str(returned))


unittest.main(exit=False)
