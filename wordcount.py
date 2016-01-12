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
            word = word.lower()
            if word[-1].isalpha() is False:
                word = word[:-1]

            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    
    #loop over dictionary, print word and word count
    # for word, count in word_count_dict.iteritems():
    for word, count in word_count_dict.items():
        print "%s %d" % (word, count)

    the_file.close()



#pass name of input file
import sys

filename = sys.argv[1]

word_count(filename)