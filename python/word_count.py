#Will Hickey
#word_count.py

import sys

#initalize a empty dictionary of words
words = {}


if len(sys.argv) < 2:
        print "no file given"
        sys.exit()

#opens the file that is given in command
fn = str(sys.argv[1])

#try to open file and excute rest of program
try:
    with open(fn) as f:
        for line in f:
                word = line.split()
                n = len(word)
                for i in range(n):
                        if word[i] in words:
                                words[word[i]] = words[word[i]] + 1
                        else:
                                words[word[i]] = 1
                        
    temp = words.keys()
    buff = sorted(temp, key=str.lower)
    llen = len(buff)

    for i in range(llen):
        print buff[i] + " " + str(words[buff[i]])
 
    print "There are " + str(llen) + " words in this file."
#except if file does not exist. 
except IOError:
   print 'Bad File'                
        
       







