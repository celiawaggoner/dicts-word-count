# put your code here.
def word_count(filename):

    """Check through a text file and print the word count"""

    #open the file
    the_file = open(filename)

    #create an empty dictionary 
    word_count_dict = {}

    #split words by space
    #loop over the_file for word
    #if word exists in dictionary, count + 1
    #else create new key for word and assign count to 1

    for line in the_file:
        line = line.rstrip()
        words = line.split()
        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    
    #loop over dictionary, print word and word count
    for word, count in word_count_dict.iteritems():
    #for word, count in word_count_dict.items():
        print "%s %d" % (word, count)

word_count("twain.txt")