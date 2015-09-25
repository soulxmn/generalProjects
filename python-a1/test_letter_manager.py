## Date: February 4, 2015
## Author(s): Suleiman Mirza
#-------------------------------------------------------------------------------

## Central Program
# Importing Modules
import unittest
from letter_manager import *
from letter_manager_anagram import main

# Test Classes and Anagram Function
class testLetterManager(unittest.TestCase):
    ''' Test the various functions of LetterManager.
    ''' 
    
    def setUp(self: 'testLetterManager') -> None:
        new_s = 'Hello. My name is Suleiman.' 
        o = [2, 0, 0, 0, 3, 0, 0, 1, 2, 0, 0, 3, 3, 2, 1, 0, 0, 0, 2, 0, 1, 0, \
             0, 0, 1, 0]
        self.test1 = LetterManager(new_s)        
        
        new_s = '  ##   Hi!,-= $ M--y GgG N4|\/|3o0O0 !s$S,,.uuuuuuuuleiuuman! '  
        self.test2 = LetterManager(new_s)   
        
        new_s = ''
        self.test3 = LetterManager(new_s)        
        

    def testTypicalInput(self: 'testLetterManager') -> None:
        ''' Test a string of regular input for the initializer. This 
        includes basic punctuation and spacing.
        ''' 
        
        # Initializing class.
        new_s = 'Hello. My name is Suleiman.' 
        o = [2, 0, 0, 0, 3, 0, 0, 1, 2, 0, 0, 3, 3, 2, 1, 0, 0, 0, 2, 0, 1, 0, \
             0, 0, 1, 0]
        # Classify it as an attribute to later use for typical input testing
        # on other methods.
        self.test1 = LetterManager(new_s)
        
        # Testing correct letter log created.
        self.assertEqual(self.test1.letters_count, o, \
                         'Error in retrieving letters!') 
        
        # Testing occurrences recorded.
        self.assertEqual(self.test1.size, 17, 'Error in summing occurrences!')
        
        return
    
    def testAtypicalInput(self: 'testLetterManager') -> None:
        ''' Test a string of irregular and nonsense input for the initializer.
        This includes randomized punctuation, symbols, spacing, and digits.
        ''' 
        
        # Initializing class.
        new_s = '  ##   Hi!,-= $ M--y GgG N4|\/|3o0O0 !s$S,,.uuuuuuuuleiuuman! '  
        # Classified as an attribute to later use for atypical testing on other
        # methods.
        self.test2 = LetterManager(new_s)
        o = [2, 0, 0, 0, 1, 0, 3, 1, 2, 0, 0, 1, 2, 2, 2, 0, 0, 0, 2, 0, 10, \
             0, 0, 0, 1, 0] 
        
        # Testing correct letter log created.
        self.assertEqual(self.test2.letters_count, o, \
                         'Error in retrieving letters!')
        
        # Testing occurrences recorded.
        self.assertEqual(self.test2.size, 29, 'Error in summing occurrences!')
        
        return
    
    def testNoInput(self: 'testLetterManager') -> None:
        ''' Test an empty string against the initializer.
        ''' 
        
        # Initializing class.
        new_s = ''
        # Classified as an attribute to later use for empty string testing on 
        # other methods.
        self.test3 = LetterManager(new_s)
        o = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
             0, 0, 0, 0] 
        
        # Testing correct letter log.
        self.assertEqual(self.test3.letters_count, o, \
                         'Error in retrieving letters!') 
        
        # Testing occurrences recorded.
        self.assertEqual(self.test3.size, 0, 'Error in summing occurences!') 
        
        return
    
    def testGetValidInput(self: 'testLetterManager') -> None:
        ''' Test a string of input logs created with the get command, passing 
        in valid input.
        ''' 
        
        # Test on typical input.
        result1 = self.test1.Get('M')
        self.assertEqual(result1, 3, 'Miscount of letters!') 
        
        # Test on atypical input.
        result2 = self.test2.Get('U')
        self.assertEqual(result2, 10, 'Miscount of letters!')
        
        # Test on empty input.
        result3 = self.test3.Get('g')
        self.assertEqual(result3, 0, 'Miscount of letters!')
        
        return
    
    def testGetSpaces(self: 'testLetterManager') -> None:
        ''' Test a string of input passing in invalid input of spacing.
        ''' 
        
        ## Multiple spaces:
        # Test on typical input. 
        result1 = self.test1.Get('   ')
        self.assertRaises(non_letter) 
        
        # Test on atypical input.
        result2 = self.test2.Get('   ')
        self.assertRaises(non_letter) 
        
        # Test on no input.
        result3 = self.test3.Get('   ')
        self.assertRaises(non_letter) 
        
        ## One space:
        # Test on typical input.
        result1 = self.test1.Get(' ')
        self.assertRaises(non_letter) 
        
        # Test on atypical input.
        result2 = self.test2.Get(' ')
        self.assertRaises(non_letter) 
        
        # Test on no input.
        result3 = self.test3.Get(' ')
        self.assertRaises(non_letter) 
        
        ## Letters with padded spacing.                                          
        # Test on typical input.
        result1 = self.test1.Get(' A  ')
        self.assertRaises(non_letter)                     
        
        # Test on atypical input.
        result2 = self.test2.Get(' U  ')
        self.assertRaises(non_letter) 
        
        # Test on no input.
        result3 = self.test3.Get('  L   ')
        self.assertRaises(non_letter) 
        
        return
    
    def testGetMultipleLetters(self: 'testLetterManager') -> None:
        ''' Test for multiple letters inputting into Get.
        ''' 
        
        ## Multiple spaces:
        # Test on typical input. 
        result1 = self.test1.Get('ALM')
        self.assertRaises(non_letter) 
        
        # Test on atypical input.
        result2 = self.test2.Get('ABV')
        self.assertRaises(non_letter)
                
        # Test on no input.
        result3 = self.test3.Get('ABT')
        self.assertRaises(non_letter)      
        
        return
    
    def testSetValidInput(self: 'testLetterManager') -> None:
        ''' Test for valid input given into Set method.
        ''' 
        
        # Test on typical input.
        self.test1.Set('M', 9) 
        result1 = self.test1.Get('m')
        self.assertEqual(result1, 9, 'Failed to reset one counter!') 
        
        # Test on atypical input.
        self.test2.Set('U', 6)
        result2 = self.test2.Get('U')
        self.assertEqual(result2, 6, 'Failed to reset one counter!')
        
        # Test on empty input.
        self.test3.Set('g', 4)
        result3 = self.test3.Get('G')
        self.assertEqual(result3, 4, 'Failed to reset one counter!') 
        
        return
    
    def testSetValueError(self: 'testLetterManager') -> None:
        ''' Test for raising ValueError.
        ''' 
        
        # Test on typical input.
        self.test1.Set('M', 9.0) 
        result1 = self.test1.Get('m')
        self.assertRaises(ValueError) 
        
        # Test on atypical input.
        self.test2.Set('U', 6.0)
        result2 = self.test2.Get('U')
        self.assertRaises(ValueError)
        
        # Test on empty input.
        self.test3.Set('g', 4.0)
        result3 = self.test3.Get('G')
        self.assertRaises(ValueError)         
        
        return 
    
    def testSetnon_letterError(self: 'testLetterManager') -> None:
        ''' Test for raising non_letter.
        ''' 
        
        # Test on typical input.
        self.test1.Set('&', 9) 
        result1 = self.test1.Get('m')
        self.assertRaises(non_letter) 
        
        # Test on atypical input.
        self.test2.Set('!', 6)
        result2 = self.test2.Get('U')
        self.assertRaises(non_letter)
        
        # Test on empty input.
        self.test3.Set(' t6g  ', 4)
        result3 = self.test3.Get('G')
        self.assertRaises(non_letter)    
        
        return 
    
    def testSize(self: 'testLetterManager') -> None:
        ''' This function has no input, it's only purpose is to return the 
        object's attribute. Hence, there is no room for invalid or valid input.
        ''' 
        
        # This function was tested in the initializers above, under the 
        # 'correct occurrences' section of each.
        
        pass
    
    def testIsEmpty(self: 'testLetterManager') -> None:
        ''' Test to see if objects are empty.
        ''' 
        
        # Test on typical input.
        result1 = self.test1.IsEmpty() 
        self.assertEquals(result1, False, 'Failed to identify emptiness!') 
        
        # Test on atypical input.
        result2 = self.test2.IsEmpty() 
        self.assertEquals(result2, False, 'Failed to identify emptiness!') 
        
        # Test on empty input.
        result3 = self.test3.IsEmpty() 
        self.assertEquals(result3, True, 'Failed to identify emptiness!') 
        
        return
    
    def test__str__(self: 'testLetterManager') -> None:
        ''' Test to see if correct string representations are returned.
        ''' 
        
        # Test on typical input.
        result1 = self.test1 
        self.assertEquals(result1, '[aaeeehiilllmmmmmmmmmnnossuy]', \
                          'Failed to concatenate correctly!') 
        
        # Test on atypical input.
        result2 = self.test2
        self.assertEquals(result2, '[aaeggghiilmmnnoossuuuuuuy]', \
                          'Failed to concatenate correctly!') 
        
        # Test on empty input.
        result3 = self.test3 
        self.assertEquals(result3, '[gggg]', 'Failed to concatenate correctly!')   
        
        return  
    
    def testAdd(self: 'testLetterManager') -> None:
        ''' Test valid input for add using two objects.
        ''' 
        
        # Positive placement.
        self.test1 = LetterManager('Hello')
        test2 = LetterManager('Hheelloo') 
        
        result1 = self.test1.Add(test2)        
        self.assertEqual(result1, '[hhheeelllooo]', 'Failed to add!') 
        
        # Empty other.
        test2 = LetterManager('')
        
        result2 = self.test1.Add(test2)
        self.assertEqual(result2, '[hello]', 'Failed to add!')
        
        return
    
    def testSubtract(self: 'testLetterManager') -> None:
        ''' Test valid input for subtract using two objects.
        ''' 
        
        # Negative placement.
        self.test1 = LetterManager('Hello')
        test2 = LetterManager('Hheelloo')
        
        result1 = self.test1.Subtract(test2)
        self.assertEqual(result1, False, 'Failed to subtract!')
        
        # Positive Placement.
        self.test1 = LetterManager('Hheelloo')
        test2 = LetterManager('Hello')
        
        result2 = self.test1.Subtract(test2)
        self.assertEqual(result2, '[ehllo]', 'Failed to subtract!')
        
        # Empty other.
        self.test1 = LetterManager('Hello')
        test2 = LetterManager('')
        
        result3 = self.test1.Subtract(test2)
        self.assertEqual(result3, '[ehllo]', 'Failed to subtract!')
        
        return

class testAnagramChecker(LetterManager):
    ''' Test the function of AnagramChecker using methods from LetterManager.
    ''' 
    
    def testValidInput(self: 'testAnagramChecker') -> None:
        ''' Test valid input for anagram checker.
        ''' 
        
        # Test for correct anagrams.
        result1 = main('horse', 'shore')
        self.assertEqual(result1, True, 'Failed to identify anagrams!')
        
        # Test for incorrect anagrams.
        result2 = main('horse', 'shored')
        self.assertEqual(result2, None, 'Failed to identify anagrams!')
        
        return
    
    def testInvalidInput(self: 'testAnagramChecker') -> None:
        ''' Test invalid input for anagram checker.
        ''' 
        
        # Test for digits.
        result1 = main('horse', 'shore9')
        self.assertEqual(result1, False, 'Failed to identify invalid input!')
        
        # Test for multiple words as one.
        result2 = main('horse horse', 'shore')
        self.assertEqual(result2, False, 'Failed to identify invalid input!')
        
        # Test for spacing and empty lines.
        result3 = main('    ', '')
        self.assertEqual(result3, False, 'Failed to identify invalid input!')
        
        return

if __name__ == '__main__':
    unittest.main()