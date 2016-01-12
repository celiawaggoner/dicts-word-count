# put your code here.
def word_count(filename):

    """Check through a text file and print the word count"""
    
    #import Counter
    from collections import Counter

    #open the file
    the_file = open(filename)

    #create an empty dictionary 
    word_count_dict = {}
    all_words = []

    #split words by space
    #loop over the_file for word
    #if word exists in dictionary, count + 1
    #else create new key for word and assign count to 1

    for line in the_file:
        line = line.rstrip()
        words = line.split()
        all_words.extend(words)

    all_words = [word.lower() for word in all_words]

    new_all_words = []

    for word in all_words:
        if word[-1].isalpha() is False:
            new_all_words.append(word[:-1])
        else:
            new_all_words.append(word)
        
    word_count_dict = Counter(new_all_words)

            # if word in word_count_dict:
            #     word_count_dict[word] += 1
            # else:
            #     word_count_dict[word] = 1

    #loop over dictionary, print word and word count
    # for word, count in word_count_dict.iteritems():
    for word, count in word_count_dict.items():
        print "%s %d" % (word, count)

    #close the file
    the_file.close()

#pass name of input file
import sys

filename = sys.argv[1]

word_count(filename)