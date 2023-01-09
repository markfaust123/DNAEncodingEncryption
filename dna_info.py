"""
Created on Sat Jan  7

@author: Mark Faust (JHED: mfaust4)
"""
# import random for use in Task 4
import random
# base-pair dictionary
base_pair_dictionary = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
# bases tuple
bases_tuple = ('A', 'T', 'C', 'G')


# 1.1 - Encoder

def encode_sequence(string):
    """
    Parameters
    ----------
    string : String
        The String of characters that needs encoding.
        
    Returns
    -------
    dna_string : String
        The DNA-encoded version of the inputted string.
    """
    # Creates a binary string representation of the input
    binary_string = ""
    for character in string:
        binary_string += "{0:08b}".format(ord(character))

    # Creates a list containing each binary pair of the binary
    # string representation of the input
    pair_list = []
    for i in range(int(len(binary_string) / 2)):
        # adds each binary pair to the list
        # after every 2 indices
        pair_list.append(binary_string[i*2:(i+1)*2])
  
    # Creates a DNA string representation of the input 
    dna_string = ""
    for pair in pair_list:
        # finds the DNA base that corresponds with each binary
        # pair and returns a string containing the proper bases
        dna_string += str(list(base_pair_dictionary.keys())
        [list(base_pair_dictionary.values()).index(pair)])
    
    return dna_string




# 1.2 - Decoder

def decode_sequence(string):
    """
    Parameters
    ----------
    string : String
        The String of DNA bases that needs decoding.

    Returns
    -------
    character_string : String
        The english version of the inputted string.
    """
    # Creates a binary string representation of the input
    binary_string = ""
    for base in string:
        binary_string += base_pair_dictionary[base]

    # Creates a list containing each byte in the binary
    # string representation
    byte_list = []
    for i in range(int(len(binary_string) / 8)):
        byte_list.append(binary_string[i*8:(i+1)*8])
    
    # Creates an english character representation of the 
    # inputted DNA
    character_string = ""
    for byte in byte_list:
        character_string += chr(int(byte, 2))
    
    return character_string




# 1.3 - Encryption

def encrypt_decrypt(string, key = "CAT"):
    """
    Parameters
    ----------
    string : String
        The string that needs encryption/decryption.
    key : String, optional
        The key needed for code encryption/decryption.
        The default is "CAT".

    Returns
    -------
    String
        The encrypted/decrypted string.

    """
    # Checks if the key's length is 0. If so, end recursion
    if len(key) == 0:
        # When base case is met, the encrypted/decrypted string
        # is returned
        return string
    
    encrypted = ""
    # Finds first letter of key and it's associated 
    # index in the tuple containing the 4 base pairs
    key_index = bases_tuple.index(key[0])
    
    # Iterates through the entire string to ensure each 
    # character is encrypted
    while len(string) > 0:
        
        # Finds first letter of string and it's associated 
        # index in the tuple containing the 4 base pairs
        string_index = bases_tuple.index(string[0])
        # Use XOR operator to find new encrypted/decrypted
        # character's associated index in the base pair tuple
        index = string_index ^ key_index
        # Constructs encrypted/decrypted string character-
        # by-character
        encrypted += bases_tuple[index]
        # Updates string variable to change loop condition 
        string = string[1::]
    
    # Method recursively calls itself until the key's length
    # has reached 0
    return encrypt_decrypt(encrypted, key[1::])




# 1.4 - Error Assessment

def synthesizer(string):
    """
    Parameters
    ----------
    string : String
        The encoded DNA string that is to be synthesized.

    Returns
    -------
    synthesized : String
        The synthesized DNA string.
    """
    synthesized = ""
    
    # Iterates through each DNA base in the inputted string
    for base in string:
        # Declares random value for use in probabilities below
        rand = random.random()
        # Synthesizes DNA based on appropriate probability
        if base.__eq__('A'):
            synthesized += 'A'
        if base.__eq__('T'):
            add = 'G' if rand < 0.02 else 'C' if rand < 0.05 \
                else 'A' if rand < 0.10 else 'T'
            synthesized += add
        if base.__eq__('C'):
            add = 'A' if rand < 0.01 else 'T' if rand < 0.02 \
                else 'G' if rand < 0.03 else 'C'
            synthesized += add
        if base.__eq__('G'):
            add = 'A' if rand < 0.01 else 'T' if rand < 0.03 \
                else 'C' if rand < 0.05 else 'G'
            synthesized += add
    # Return the synthesized string
    return synthesized

def error_count(string_1, string_2):
    """
    Parameters
    ----------
    string_1 : String
        First string that will be compared to string_2.
    string_2 : String
        Second string that will be compared to string_1.

    Returns
    -------
    count : Integer
        The number of inconsistencies between the two strings.
    """
    # Counts the number of inconsistencies there are between the 
    # two inputted strings
    count = 0
    for i in range(len(string_1)):
        if not string_1[i].__eq__(string_2[i]):
            count += 1
    # Returns number of inconsistencies found
    return count




# 1.5 - Redundancy

def redundancy(n, string):
    """
    Parameters
    ----------
    n : integer
        Number of copies of the inputted string that are
        used to find the corrected output.
    string : String
        The string that's redundancies are being corrected.

    Returns
    -------
    correct_synthesis : String
        The corrected version of the input string.
    """
    
    correct_synthesis = ""
    
    # Creates a list containing n copies of the inputted string
    list_of_strings = []
    for i in range(n):
        list_of_strings.append(synthesizer(string))
        
    # Iterates though each index of the list_of_strings entries
    for i in range(len(list_of_strings[0])):
        
        a_count = 0
        t_count = 0
        c_count = 0
        g_count = 0
        
        # Iterates through each entry of list_of_strings
        for entry in list_of_strings:
            
            # Counts how many times each base appears at index i
            # of the entries in list_of_strings
            if entry[i].__eq__('A'):
                a_count += 1
            if entry[i].__eq__('T'):
                t_count += 1
            if entry[i].__eq__('C'):
                c_count += 1
            if entry[i].__eq__('G'):
                g_count += 1
                
        # Concatenates the most frequent character at each index i of 
        # the entries of list_of_strings to correct_synthesis
        if a_count > t_count and a_count > c_count and a_count > g_count:
            correct_synthesis += 'A'
        elif t_count > c_count and t_count > g_count:
            correct_synthesis += 'T'
        elif c_count > g_count:
            correct_synthesis += 'C'
        else:
            correct_synthesis += 'G'        
        
    # Returns corrected string
    return correct_synthesis


# Code used for Task 7

"""
my_string = ""

# create very large string in order to actually see the effect
# of increasing n
for i in range(10000):
    my_string += "GCTAGCTACGATCGATCGATGCTAGCACTATCATCTAGCGA"

# set n = 20 to watch error count decrease as n increases
x = 20
for n in range(1, x + 1):
    correct = redundancy(n, my_string)
    errors = error_count(correct, my_string)
    print(f"n = {n} --> errors:", errors)
"""