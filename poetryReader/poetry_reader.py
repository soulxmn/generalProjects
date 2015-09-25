"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""
def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """ 
    
    pronunciation_dictionary = {}
    
    # Assigns the key to its appropriate phonemes (thus creating it if it does
    # not exist).
    results = []
    for line in pronunciation_file:
        if line[0:3] != ';;;':
            results.append(line.split())
            if results[-1][0] not in pronunciation_dictionary:
                pronunciation_dictionary[results[-1][0]] = results[-1][1:] 
                
    return pronunciation_dictionary

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """ 
    
    syllables = []
    rhymes = [] 
    
    poetry_forms_file.readline()
    for line in poetry_forms_file:
        # Checking for blank line and end of file.
        if not line.isspace() and line != '': 
            x = line.split() 
            syllables.append(int(x[0]))
            rhymes.append(x[-1]) 
            poetry_forms_file.readline()    
        # Terminating loop if hitting blank line. Avoid reading rest of file.
        else: 
            temp = [syllables, rhymes]
            poetry_pattern = tuple(temp)
            return poetry_pattern 
        
    # Providing a return statement alternative for end of file line.
    temp = [syllables, rhymes]
    poetry_pattern = tuple(temp)
    return poetry_pattern 

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file. 
    """ 
    
    forms = {}
    previous_line = ' ' # Checking if line is a poetry form name.
    
    # Use function 2 as a helper for each form name found in file.
    for line in poetry_forms_file: 
        if not line.isspace() and previous_line.isspace():
            # Creating the key.
            forms[line[0:-1]] = read_poetry_form_description(poetry_forms_file) 
        previous_line = line
    
    return forms 