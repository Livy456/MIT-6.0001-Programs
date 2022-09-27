import string
import math


# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    # print(f"this is input text-> a string: {input_text}")
    
    # iniitialization section
    #word = ""
    #update_list = []
    word_list = []
    space_word = None
    word = [""]
    #combine = ""
    #i = 0
    
    """
    # loops of input_text to 
    while i < len(input_text):
        char = input_text[i]
        if char == " ":
            while char == " ":
                i+=1
                char = input_text[i]
            word_list.append(word)
        # avoids getting a negative index
        if i !=0:    
            combine = char + input_text[i-1]
        # checks to make sure the character is in alphabet and is not \r or \n
        elif char.isalpha() and (combine != "\n") and (combine != "\r"): 
            word = word + char
        i+=1
    """    
    # splits the string into a list of individual words        
    word_list = input_text.split(" ")
    #print(word_list)
    #print(len(word_list))
    i = 0
    while i < len(word_list):
        #print(f"this is word_list: {word_list}")
        #print(f"I am i: {i}")
        ele = word_list[i]
        
        if ("\n" in ele):
            word_list[i] = word_list[i].replace("\n", " ")
            #print(f"No more \\n: {word_list[i]}")
        if ("\r" in ele):
            word_list[i] = word_list[i].replace("\r", " ")
            #print(f"No more \\r: {word_list[i]}") 
        elif ele == "":
            word_list.remove(ele)
        i+=1
        
    for i in range(len(word_list)):
        ele = word_list[i]
        if " " in ele: 
            space_word = word_list.pop(i)
    # takes the broken up word
    #print(type(space_word))
    
    # catches the attribute error that comes from
    try:
        if type(space_word) != None:
            word = space_word.split(" ")
    except AttributeError:
        pass
    
    if word != [""]:
        for ele in word:
            word_list.append(ele)
    """
    for ele in word_list:
        i+=1
        if ele == "":
            word_list.remove(ele)
        elif ele == "\\":
            word_list.remove(ele)
            word_list.remove(word_list[i])
    """        
    """
    for char in input_text:
        i +=1
        if char.isalpha():
            word = word + char
        elif char == " ":
            word_list.append(word)
    """
    # return section
    return word_list


### Problem 1: Get Frequency ###
def get_frequencies(word_list):
    """
    Args:
        word_list: list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in l and the corresponding int
        is the frequency of the letter or word in l
    """
    # initialization section
    uni_list = []
    uni_dict ={}
    
    # creates a list of the unique letters or words in list
    for ele in word_list:
        if ele not in uni_list:
            uni_list.append(ele)
    
    # finds the frequency of the unique words or text
    for ele1 in uni_list:
        count = 0
        for ele2 in word_list:
            if ele1 == ele2:
                count+=1
        uni_dict[ele1] = count
   
    
    # return section
    return uni_dict

### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    word_list = []
    
    for let in word:
        word_list.append(let)
    
    # return section
    # returns a dictionary of the frequency of the letters
    # by using the get_frequency function
    return get_frequencies(word_list)

### Problem 3: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of letters of word1 or words of text1
        dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    # initialization section
    sim_score = 1
    score = 0
    total = 0
    diff = 0
    diff_freq1 = 0
    diff_freq2 = 0
    
    # gets the keys from the two dictionaries
    key1 = list (dict1.keys())
    key2 = list (dict2.keys())
        
    # iterates through all the keys in dict1
    for ele in key1:
        # checks to see if there are similar keys in dict1 and dict2
        if ele in key2:
        # finds the difference in frequency of similar key elements
            #if dict1[ele] == dict2[ele]:
            #    diff+= dict1[ele] + dict2[ele]
            #else:    
            diff += abs(dict1[ele] - dict2[ele])
        # checks to see if there are unique keys only to dict1
        elif ele not in key2:
            diff_freq1 += dict1[ele]
        # finds total frequency of all elements of dict1 
        total+=dict1[ele]
    
    # iterates through all the keys from dict2
    for ele in key2:
        # checks to see if there are unique keys only to dict2
        if ele not in key1:
            diff_freq2 += dict2[ele]
        # adds the total frequency of all elements dict2 to total frequency of dict1
        total+=dict2[ele]
    """
    print()
    print(dict1)
    print(dict2)
    print(f"this is diff: {diff}")
    print(f"this is diff_freq1: {diff_freq1}")
    print(f"this is diff_freq2: {diff_freq2}")
    """
    # calculates the score based on the sum of frequency of unique words in both dicts
    # and the difference in frequency of words in both dicts
    score = 1-((diff_freq1+diff_freq2+diff)/total)  
    #print(score)            
    sim_score = float("{:.2f}".format(score))
    
    # checks to see whether the two dictionaries inputted are the same
    if key1 == key2:
        sim_score = 1
    # checks to see if all the items in dictionary are different
    
    #elif diff == 0:
    #    sim_score = 0
    
    return sim_score

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """    
    # initialization section
    maxf = 0
    val1 = dict1.values()
    val2 = dict2.values()
    maxf1 = max(val1)
    maxf2 = max(val2)
    max_list = []
    
    # checks to see if dict2 has the max frequency
    if maxf1 < maxf2:
        maxf = maxf2    
    # checks to see if dict1 has the max frequnecy, or if the frequencies are equivalent
    else:
        maxf = maxf1
    
    # for loop to find if dict1 has the most frequent word
    for key, value in dict1.items():
        if value == maxf:
            max_list.append(key)
    
    # for loop to find if dict2 has the most frequenct word
    for key, value in dict2.items():
        if value == maxf:
            max_list.append(key)
    
    # return section
    return max_list

### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    # initialization section
    dict_tf = {}
    word_list = prep_data((load_file(text_file)))   # load file puts the content of text file into string 
                                                    # format then prep data makes string into a list
    tot_word = len(word_list)                       # total number of words in the document
    word_dict = get_frequencies(word_list)          # frequency of the words in the document
    tf = 0.0
    
    # finds the tf for each word
    for key, value in word_dict.items():
        tf = value/tot_word
        dict_tf[key] = tf # adds a new item to the dict of word assigned to tf value
    
    # return section
    return dict_tf

def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    # initialization section
    dict_idf = {}
    tot_doc = len(text_files) # total number of documents
    idf = 0
    word_list = []
    all_word_list = [] # a list of a list of all the words in each document
    uni_word = []      # frequency of each word
    
    # for loop to iterate through each document
    for text in text_files:
        # check to see element in list is in document
        word_list = prep_data(load_file(text)) # creates a list of words from document
        all_word_list.append(word_list)
        
        # get all the words into a dictionary
        for word in word_list:
            # only adds unique elements to dictionary
            if word not in all_word_list:
                uni_word.append(word)
    
    # calculates the idf for each word
    for word in uni_word:
        # resets values
        idf = 0
        cnt = 0
        # iterates through each document
        for doc in all_word_list:
            # checks if word is in document
            if word in doc:
                cnt +=1 # increases frequency
        if cnt == 0:
            idf = 0
        else:
            idf = math.log10(tot_doc/cnt)
        # adds dictionary entry with word assigned to its corresponding idf value
        dict_idf[word] = idf
        
    
    """try making coding have less big o complexity"""
    """
    # try to not use a triple for loop
    # put the words in a dictionary
    # iterate over every word
    # add the word to a dictionary
    # count the number of words in each dictionary
    
    # loops to iterate throguh each document
    for document in all_word_list:
        # iterates through each word in the document
        for word in document:
            idf = 0
            word_cnt = 0  # number of documents word is in
            
            # checks to see if the idf was already calculated for word
            if word not in dict_idf:
                # iterates through each document to find if word is inside
                for doc in all_word_list:
                    if word in doc:
                        word_cnt+=1
                if word_cnt == 0:
                    idf = 0
                else:
                    idf = math.log10(tot_doc/word_cnt)
                dict_idf[word] = idf
     """       
    # return section
    return dict_idf

def get_tfidf(text_file, text_files):
    """
        Args:
            text_file: name of file in the form of a string (used to calculate TF)
            text_files: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
    """
    # initialization section
    word_list = prep_data(load_file(text_file))
    #print(f"this is the prep data output:{prep_data(load_file(text_file))}")
    dict_tf = get_tf(text_file)
    dict_idf = get_idf(text_files)
    tf_idf = 0
    list_tf_idf = []    # a list of a list of the word and its corresponding tf-idf value
    #sort_list = []
    
    #dict_tf_idf = {}
    #print(f"this is word_list {word_list}")
    for ele in word_list:
        # calculates the tf, idf, and the tf-idf of a word
        tf = dict_tf[ele]
        idf = dict_idf[ele]
        tf_idf = tf*idf
        # adds the word and its corresponding tf-idf to a tuple
        list_calc = (tf_idf, ele)
        #list_calc = (ele, tf_idf)
        #dict_tf_idf[ele] = tf_idf
        # checks to make sure only unique word, tf-idf pairs are added to list 
        if list_calc not in list_tf_idf:
            list_tf_idf.append(list_calc)
        #print(f"end of the loop this is what list_tf_idf is: {list_tf_idf}")
    
    list_tf_idf.sort()
    for i in range(len(list_tf_idf)):
        list_tf_idf[i] = (list_tf_idf[i][1], list_tf_idf[i][0])
    
    """
    print()
    print("this is list_tf_idf")
    print(list_tf_idf)
    print("first item1")
    print(list_tf_idf[0])
    print("second item2")
    print(list_tf_idf[1])
    print("we're all done")
    
    for item in list_tf_idf:
        tf_idf = item[1]
        
        # checks to make sure that item is a unique pair of word and tf-idf value
        if item not in sort_list:
        
    """
    """
    i = 0
    # bubble sort algorithm
    for i in range(len(list_tf_idf)):
        
        for index in range(len(list_tf_idf)-i - 1):
            item1 = list_tf_idf[index]
            item2 = list_tf_idf[index+1]
            
            if item1[1] > item2[1]:
                item = item2
                list_tf_idf[index] = item1
                list_tf_idf[index-1] = item
            elif item1[1] == item2[1]:
                if item1[0] > item2[0]:
                    item = item2
                    list_tf_idf[index] = item1
                    list_tf_idf[index-1] = item
                
    """
    """
    while i < len(list_tf_idf)-1:
        item1 = list_tf_idf[i] # tf_idf tuple
        index = i+1
        #print("this is i")
        #print(i)
        #print("inside first while loop")
        #print("this is item1")
        #print(item1)
        #print("this is index")
        #print(index)
            # loop to swap indexes
        while index < len(list_tf_idf):
            item2 = list_tf_idf[index]
                
            if item1[1] > item2[1]:
                # swap tuples
                item = item2
                list_tf_idf[index] = item1
                list_tf_idf[index-1] = item
                #print(f"this is the list_tf_idf[index]: {list_tf_idf[index]}")
                #print(f"this is the list_tf_idf[index-1]: {list_tf_idf[index-1]}")
            elif item1[1] == item2[1]:
            # checks to see if item2 is alphabetically less than item 1
                #print(f"this is the item1[1]: {item1[1]}")
                #print(f"this is the item1: {item1}")
                #print(f"this is the item2[1]: {item2[1]}")
                #print(f"this is the item2: {item2}")
                #print("we're equals!")
                if item1[0] > item2[0]:
                    #print("I'm in the loop!")
                    item = item2
                    list_tf_idf[index] = item1
                    list_tf_idf[index-1]= item
            index+=1
        i+=1
    """
           
    """
    for i in range(len(list_tf_idf)):
        value = list_tf_idf[i][1]   # gets the tf-idf value
        
        for j in range(i+1, len(list_tf_idf)):
            compare = list_tf_idf[j][1]
            # checks for the smallest element in the list
            if value > compare and (compare not in ):
                value = compare
        
     """       
        # check the ascii value of the value[0][0] and compare with the word to the right
    
    return list_tf_idf


if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    ## Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    #hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #world, friend = prep_data(hello_world), prep_data(hello_friend)
    #print(world) ## should print ['hello', 'world', 'hello']
    #print(friend) ## should print ['hello', 'friends']
    list_word = prep_data("hello  it is\nme\rmario")
    print(list_word)
    
    ## Tests Problem 1: Get Frequencies
    #world_word_freq = get_frequencies(world)
    #friend_word_freq = get_frequencies(friend)
    #print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    #print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    #freq1 = get_letter_frequencies('hello')
    #freq2 = get_letter_frequencies('that')
    #print(freq1) ##  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    #print(freq2) ##  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    #word1_freq = get_letter_frequencies('toes')
    #word2_freq = get_letter_frequencies('that')
    # 1, 1, 1, 1
    # 2, 1, 1
    #word3_freq = get_frequencies('nah')
    #word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    #word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    #word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    #word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    #print(word_similarity1) ## should print 1.0
    #print(word_similarity2) ## should print 0.25
    #print(word_similarity3) ## should print 0.0
    #print(word_similarity4) ## should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    #freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    #most_frequent = get_most_frequent_words(freq1, freq2)
    #print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    #text_file = 'tests/student_tests/hello_world.txt'
    #text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    #tf = get_tf(text_file)
    #idf = get_idf(text_files)
    #tf_idf = get_tfidf(text_file, text_files)
    #print(tf) ## should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    #print(idf) ## should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    #print(tf_idf) ## should print [('hello', 0.0), ('world', 0.10034333188799373)]



