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
    #loop through each line in file, and each word in line
    #if work exists in dictionary, value + 1
    #else create new key for word and assign value to 1
    #print word and word count

word_count("test.txt")