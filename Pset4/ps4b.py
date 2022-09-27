# Problem Set 4B
# Name: Olivia Dias
# Collaborators: 6.0001 Office Hours
# Time Spent: 2:00

import random


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            the message text
        '''
        self.input_text = input_text

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        '''
        Used to access the message text outside of the class

        Returns: (string) the message text
        '''
        return self.input_text

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        ######################
        # nonalpha ----> ASCII
        # Space -------> 32 
        # Assuming we are ignoring numbers
        # 48 through 57 (numbers) are ignored
        # 58 through 64 are used
        #
        ######################
        # letter ------> ASCII
        # A -----------> 65
        # Z -----------> 90
        # a -----------> 97
        # z -----------> 122
        #
        # initialization section
        ascii_char = ord(char)      # converts the char to an ascii value
        # shifts old ascii value of char to new ascii value
        # ascii_char-32 gets the ascii_char in the 32, 126 range
        # applys the shift and then wraps around the 32, 126 range
        # adds the value to beginning of range to go to correct corresponding element
        new_char = 32 + (ascii_char - 32 + shift)% 95
        # returns the shifted char value
        return chr(new_char)
        """
        # checks for a negative shift value and uppercase letter in alphabet
        if shift < 0 and char.isalpha() and char.isupper():
            # A ---> 65+1 = 66 - 65 = 1%26 = -1 90
            # ascii - 65 will find which uppercase letter needs to be shifted
            # then it'll get shifted
            # if shift causes the new letter to exceed the 26 letters in alphabet then 
            # wraps around the 26 letters in the alphabet
            # subtract remainder from end of alphabet and shifts backwards because of negative shift
            new_char = 91 + (ascii_char-65 + abs(shift))% 26
        # checks for negative shift value and lowercase letter in alphabet
        elif shift < 0  and char.isalpha() and char.islower():
            # calculates the backwards shifting lowercase alphabet letter
            new_char = 123 - (ascii_char-122 + abs(shift))%26
        # checks for negative shift value and for nonalphabetic chars
            # " " ---> 32 + 1 = 33 - 32 = 1%94 = 1  127-1 = 126
        # positive shift value and uppercase letter in alphabet
        elif shift > 0 and char.isalpha() and char.isupper():
            # A--> 65 + 5 = 70-65 = 5
            # ascii - 65 will find which lowercase letter needs to be shifted
            # then it'll get shifted
            # wrap around the 26 letters in the alphabet
            # add remainder to beginning of alphabet and shifts forwards because of positive shift
            new_char = 65 + (ascii_char-65+shift) % 26
        # positive shift value and lowercase letter in alphabet
        elif shift > 0 and char.isalpha() and char.islower():
            # calculates the positive shifting lowercase alphabet letter
            new_char = 97 + (ascii_char-97 + shift) % 26
        else:
            new_char = 32 + (ascii_char - 32 + shift)% 94
        # checks for a positive shift value for non alphabetic chars
            while chr(new_char).isalpha():
                if chr(new_char).isupper():
                    # finds which letter in the alphabet
                    new_char = (new_char - 65)        
        """
    
    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        #raise NotImplementedError  # delete this line and replace with your code here
        encode_str = ""
        message = self.get_text()
        # loops through each shift value of pad
        for i in range(len(pad)):
            char = self.shift_char(message[i], pad[i])
            encode_str = encode_str + char
            
        return encode_str
        
class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!=None then len(pad) == len(self.input_text)

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad==None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        # initialization of the class variables
        super().__init__(input_text)
        self.pad = pad
        self.cipher_text = ""

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt the message text.

        The pad should be generated by making a new list and for each character
            in the message chosing a random number in the range [0, 110) and
            adding that number to the list.

        Returns: (list of integers) the new one time pad
        '''
        # initializes a new list
        self.pad = []
        # loops through entire message text so that len(pad) = len(message)
        for ele in self.input_text:
            num = random.randint(0, 110)    # generates a random int from 0, 110
            self.pad.append(num)    # adds a random int (1,110) to pad
        
        # returns list of random int
        return self.pad

    def get_pad(self):
        '''
        Used to safely access your one time pad outside of the class

        Returns: (list of integers) a COPY of your pad
        '''
        # checks if pad is none
        if self.pad == None:
            # generates a pad
            self.pad = self.generate_pad()
            self.pad = self.pad.copy()   # assigns the pad attribute to a copy of itself
            
            #returns a copy of the generated random list of ints
            return self.pad
        
        # pads that are not none
        else:
            self.pad = self.pad.copy() # creates a copy of the pad
            
            # returns copy of the pad
            return self.pad   
                
    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying pad to the message text

        Returns: (string) the ciphertext
        '''
        # gets the pad from PlaintextMessage class
        # calls the Message class to use apply_pad method with generated pad
        # returns the cipher text
        return super().apply_pad(self.get_pad())
        #raise NotImplementedError  # delete this line and replace with your code here

    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)

        Returns: nothing
        '''
        self.pad = new_pad  # updates the pad attribute
        #self.cipher_text = self.get_ciphertext()    # updates the cipher te

class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        super().__init__(input_text)  # calls parent class-Message- to create input_text attribute

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: (PlaintextMessage) the decrypted message (containing the pad)
        '''
        # initialization section
        undo_pad = []
        decrypt_str = ""
        
        # goes through each element in pad to reverse the shift
        for ele in pad:
            un_shift = -ele
            undo_pad.append(un_shift)   # adds the negated shift element
        
        # goes through each element in message to decrypt it
        for i in range(len(self.input_text)):
            # creates the decrypted message
            decrypt_str = decrypt_str + super().shift_char(self.input_text[i], undo_pad[i])
            
        # returns decrypted message
        return PlaintextMessage(decrypt_str)

