import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    #-------------------------
    # INITIALIZATION SECTION
    #-------------------------
    game = False       # Sets the default value for if player won to false
    uni_let = []       # makes a list of all the unique letters in secret word 
    count = 0          # counter for if unique letters appear in letters_guessed
     
    
    # for loop to find the unique letters in the secret word
    for ele in secret_word:
        if ele not in uni_let:
            uni_let.append(ele)
    
    # for loop to find if the letters from secret word are in letters_guessed list
    for e in uni_let:
        if e in letters_guessed:
            count+=1
            
    # checks to see if all the unique letters in the secret word were guessed
    if count == len(uni_let):
        game = True
    
    # Return Section
    return game
    
def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    #-------------------------
    # Initialization Section
    #-------------------------
    progress_word = ""
    
    # for loop to create a string of the guessed letters 
    for ele in secret_word:
        #print("this is element in secret word", ele)
        # if statement to check for letter in secret word in letters guessed
        if ele in letters_guessed:
            # adds the guessed letter to the progress string
            progress_word = progress_word + ele
        # else statement to keep the letter hidden    
        else:
            # hides the letter from the user
            progress_word = progress_word + "*"
    
    # Return section
    return progress_word 


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    #-------------------------
    # Initialization Section
    #-------------------------
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    avail_let = ''
    
    for ele in letters_guessed:
        if ele in alphabet:
            alphabet.remove(ele)
    
    # creates a string of the available letters 
    avail_let = "".join(alphabet)
    """
    # if statement to check if no letters have been guessed
    if letters_guessed == []:
        avail_let = string.ascii_lowercase
        
    #else if statement to check if every letter has been guessed in the alphabet
    for ele in letter_guessed:
        
   #elif letters_guessed == alphabet:      
   #     avail_let = ''
    # else statement to creat string of available letters
    else:    
        # for loop to only add the available letters to a new list 
        for alpha in alphabet:
            if alpha not in letters_guessed:
                avail_let = avail_let + alpha
    """
    
    # Return section
    return avail_let

def invalid_let(with_help, avail_let, secret_word, guessed_word, letters_guessed, count):
    """
    avail_let: string, available letters that the user can guess from
    count: int, how many guesses the user has left 
    
    returns: list, containing a string(first element) and the amount to deduct 
    the guess count by (second element)
    """
    #------------------------
    #Initialization Section
    #------------------------
    in_let = True   # default is invalid input
    consonant = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    let_guess = ""
    reveal_let = ""
    help_list = ["", 0, letters_guessed]    # list that contains guessed character 
                                            # and the amount to decrement guess count by
    # while loop to check for valid inputs
    while in_let:
        # if statement for grammar
        if count  > 1:
            print("You currently have,", str(count),"guesses left.")
        # else if statement for grammar
        elif count == 1:
            print("You currently have", str(count),"guess left.")
    
        print("Available letters:",str(avail_let))
        let_guess = input("Please guess a letter:").lower()
        
        # checks to see if input is in alphabet
        if not(let_guess.isalpha()) and not(let_guess == "$"):
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", guessed_word)
            print("--------------")
        
        # else if statement to check if the user is trying to receive help
        elif (let_guess == "$") and count >= 3 and with_help:
            in_let = False
            reveal_let = guess_help(secret_word, avail_let)
            print("Letter revealed:",str(reveal_let))
            # when help_list[0] called gets rid of the letter revealed
            let_guess = reveal_let
            help_list[1] = 3
            help_list[2].append(reveal_let)
            guessed_word = get_word_progress(secret_word, letters_guessed)
            print(guessed_word)
            print("-------------")
            return help_list
        
        # else if statement to see if the user doesn't have enough guesses
        # left to use help feature
        elif (let_guess == "$") and count < 3 and with_help:
            print("Oops! Not enough guesses left:",guessed_word)    
            
        # checks to see if letter has already been guessed
        elif (let_guess not in avail_let) and not(let_guess =="$"):
            print("Oops! You've already guessed that letter:", str(guessed_word))
            print("-------------")
        
        # else statement to see if user made a valid guess
        elif ((let_guess.isalpha()) and (let_guess in avail_let)):    
            in_let = False
        
    help_list[0] = let_guess
    
    # if statement to check if letter is a consonant not in secret word
    if (let_guess in consonant) and not(let_guess in secret_word): 
        help_list[1] = 1 # will decrease guess count by one
        print("Oops! That letter is not in my word:", str(guessed_word))
        print("-------------")
    # else if statement to check if letter is a vowel not in secret word
    elif (let_guess in vowels) and not(let_guess in secret_word):
        help_list[1] = 2 # will decrease guess count by two
        print("Oops! That letter is not in my word:", str(guessed_word))
        print("-------------")
    # else statement to check if letter is in secret word
    else:
        help_list[2].append(let_guess)
        guessed_word = get_word_progress(secret_word, letters_guessed)
        print("Good guess:",guessed_word)
        print("-------------")
        
    # Return Section
    return help_list
    

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '$'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol $, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    #-------------------------
    # Initialization Section
    #-------------------------
    guess = 10
    letters_guessed = []
    score = 0
    guess_let = ""
    
    #Print the start of the Hangman game
    print("Welcome to Hangman!")
    print("I am thinking of a word that is", str(len(secret_word)),"letters long.")
    print("-------------")
   
    # while loop to simulate hangman game
    while guess > 0:
        avail_let = get_available_letters(letters_guessed)
        guessed_word = get_word_progress(secret_word, letters_guessed)

        # function to get a valid user input
        help_list = invalid_let(with_help, avail_let, secret_word, guessed_word, letters_guessed, guess)
        
        guess_let = help_list[0]
        letters_guessed.append(guess_let)
        guessed_word = get_word_progress(secret_word, letters_guessed)
        
        
        # if statement to check if the user guess the correct word
        if has_player_won(secret_word, letters_guessed):
            #print("Good guess:",guessed_word)
            uni_let = []
            
            # for loop to create a list of the unique letters in the secret word
            for ele in secret_word:
                if ele not in uni_let:
                    uni_let.append(ele)
            """
            string = "".join(uni_let)
            print("this is the uni_let", string)
            print("this is 4*len(secret word):",4*len(secret_word))
            print("this is 3*len(uni_let)",3*len(uni_let))
            print("this is guess", guess)
            """
            # calculates score
            guess = guess-help_list[1]
            score = guess + 3*len(uni_let) + 4*len(secret_word)
            
            # ending of the hangman
            print("Congratulations, you won!")
            print("Your total score for this game is:", str(score))
            break
        
        else:
            #print(guessed_word)
            guess= guess-help_list[1]
            if guess <= 0:
                print("Sorry, you ran out of guesses. The word was", secret_word)


def guess_help(secret_word, avail_let):
    """
    secret_word: string, the lowercase word the user is guessing
    avail_let: string, available letters that the user can guess from
        
    return: string, a letter to reveal in the secret word
        
    """
    #-------------------------
    # Initialization section
    #-------------------------
    choose_from = ""    
    
    # creates a string of unique of letters that is in both secret word and available letters string
    for ele in secret_word:
        if (ele in secret_word) and (ele in avail_let) and (ele not in choose_from):
            choose_from = choose_from + ele
    
    # selects a random letter to reveal
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    
    # Return section
    return revealed_letter
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    #secret_word = "wildcard"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "$" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.

