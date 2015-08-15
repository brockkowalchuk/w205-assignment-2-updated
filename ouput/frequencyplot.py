# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:13:28 2015
@author: brockkowalchuk
"""

import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
import codecs
from matplotlib import pylab as pl
import numpy as np
import re #reg expression

#Open  file with desired tweets, read in as utf-8 for NLTK to process
file = codecs.open("q2_master.txt", "r", "utf-8")
text = file.read()
tokens = nltk.word_tokenize(text) #break down text into words (tokenize)
words = [w.lower() for w in tokens]
words_FreqDist = FreqDist(words) #encode frequency distributions
common = words_FreqDist.most_common(500) #NLTK function to gather most common word occurrences
stopwords = stopwords.words('english') # I added RT, HTTP, HTTPS to my english stopwords file
top_words_dict = {} #create empty dictionary for results

#fill dictionary with top 50 words
i = 0
while len(top_words_dict) <= 50:
    top_word = common[i]
    #regex allows us to remove erroneous characters. in the below we watch for a-z, A-Z, 0-9
    if top_word[0] not in stopwords and re.match('^[a-zA-Z0-9]*$',top_word[0]): 
        top_words_dict[top_word[0].encode('ascii')] = top_word[1] #encode word into ascii, and add to dict
    i += 1

#create a plot of the frequency distribution
X = np.arange(len(top_words_dict))
pl.bar(X, top_words_dict.values(), align = 'center', width = 0.6)
pl.xticks(X, top_words_dict.keys(), fontsize = 6.5)
locs, labels = pl.xticks()
pl.setp(labels, rotation = 90)
ymax = max(top_words_dict.values()) + 100
pl.xlim([-1,51])
pl.ylim(0, ymax)
pl.suptitle("Most Frequently Occurring Words")
pl.show()