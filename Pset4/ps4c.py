 # Problem Set 4C
# Name: Olivia Dias
# Collaborators: 6.0001 Office Hours
# Time Spent: 2:00

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###

def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    # initialization section
    decrypt_cipher = ""     # best decrypted message
    best_pad = []           # best pad for decrypting message
    num_words = []          # list of number of english words in each decrypted message
    msg_list = []           #
    word_list = load_words('words.txt') # creates a list of valid words
    
    # goes through each pad and tries decrypting the cipher text message
    for pad in pads:
        # gets the message
        message = ciphertext.decrypt_message(pad).get_text()   # decrypts message based on one of the pads
        msg_list.append(message)    # adds the decrypted message to 

    # loops over each message in message list            
    for message in msg_list:
        cnt = 0     # resets number of english words found
        # splits the message into invidual words
        words = message.split(" ")
        
        # loops over each word in the word list
        for w in words:
            # checks if word is an english word
            if is_word(word_list, w):
                cnt+=1 #increments the number of english words in list
        num_words.append(cnt)
        
    max_words = max(num_words)  # finds the max number of english words out of all the decrypted messages 
    
    # loops over all the elements in num word list to find the index of max number of english words
    for i in range(len(num_words)):
        ele = num_words[i]
        
        # finds the last pad with the max number of english words
        if ele == max_words:
            best_pad = pads[i]  # gets the best pad
            decrypt_cipher = msg_list[i]    # gets the best decrypted message

    # returns the decrypt cipher and the best pad
    return ps4b.PlaintextMessage(decrypt_cipher, best_pad)

def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    story_encrypt = get_story_string()  # gets the cipher text 
    pads = get_story_pads()             # gets all the potential pads
    # creates a string that decrypts the cipher text message
    story_decrypt = decrypt_message_try_pads(ps4b.EncryptedMessage(story_encrypt), pads).get_text()
    
    # returns the decrypted message
    return story_decrypt

if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    #pass