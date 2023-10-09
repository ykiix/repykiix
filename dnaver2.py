class DNA(object):
    def __init__(self, string : str) -> None:
        """
        Input:
        - string : a sequence of 'A's, 'T's, 'G's, 'C's

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Create an attribute of DNA class with attribute_name                #
        # and type str from the given string.                                 #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.string = string
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'T', 'G', 'C' and their 
        corresponding amounts in attribute_name. 
        {'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'T's, 'G's, 'C's either by                           #
        # looping over attribute_name or using a standard string method.      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        count_A = 0
        count_T = 0
        count_C = 0
        count_G = 0
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                count_A += 1
            if self.string[i] == 'T':
                count_T += 1
            if self.string[i] == 'C':
                count_C += 1
            if self.string[i] == 'G':
                count_G += 1
        print('A:', count_A, 'T:', count_T, 'C:', count_C, 'G:', count_G)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'T's were changed to 'U's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        transcript = ''
        for i in range(len(self.string)):
            if self.string[i] == 'T':
                transcript += 'U'
            if self.string[i] == 'A':
                transcript += 'A'
            if self.string[i] == 'G':
                transcript += 'G'
            if self.string[i] == 'C':
                transcript += 'C'
        print(transcript)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def complement_dna(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'A's were changed to 'T's
        and vice versa, all 'C's changed to 'G's and vice versa
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        complementstring = ''
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                complementstring += 'T'
            if self.string[i] == 'T':
                complementstring += 'A'
            if self.string[i] == 'C':
                complementstring += 'G'
            if self.string[i] == 'G':
                complementstring += 'C'
        print(complementstring)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def hamming_distance(self, string2 : str) -> int:
        """
        Input:
        - string2 : another sequence of 'A's, 'T's, 'G's, 'C's

        Output: number of different letters 
        between attribute_name and given string
        """
        #######################################################################
        # TODO:                                                               #
        # First, check that attribute_name and given string have the same     #
        # length, if not raise Error.                                         #
        # If the length of strings is the same, loop over one of the strings  #
        # and count different letters.                                        #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.string2 = string2
        hd = 0
        if len(self.string)==len(self.string2):
            for i in range(len(self.string)):
                if self.string[i] != self.s2[i]:
                    hd += 1
            print(hd)
        else:
            print('Error')
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


class RNA(object):
    def __init__(self, string : str) -> None:
        """
        Input: 
        - string : a sequence of 'A's, 'U's, 'G's, 'C's

        Output: None
        """
       ########################################################################
        # TODO:                                                               #
        # Create an attribute of RNA class with attribute_name                #
        # and type str from the given string.                                 #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.string = string
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'U's were changed to 'T's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        transcript = ''
        for i in range(len(self.string)):
            if self.string[i] == 'U':
                transcript += 'T'
            if self.string[i] == 'A':
                transcript += 'A'
            if self.string[i] == 'G':
                transcript += 'G'
            if self.string[i] == 'C':
                transcript += 'C'
        print(transcript)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****