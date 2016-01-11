# put your code here.
def word_count(filename):

    """Check through a text file and print the word count"""

    #open the file
    the_file = open(filename)

    #split words by space

    all_words = []

    for line in the_file:
        line = line.rstrip()
        words = line.split(" ")
        all_words += words
    # print all_words

    #create an empty dictionary 
    word_count_dict = {}

    #loop over all_words
    #if work exists in dictionary, value + 1
    #else create new key for word and assign value to 1

    for word in all_words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    #print word and word count
    
    for word, count in word_count_dict.items():
        print "%s %d" % (word, count)

word_count("test.txt")