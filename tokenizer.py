# -*- coding: utf-8 -*-

import re
import json
from collections import Counter

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
#import nltk
#nltk.download('all')
from nltk.corpus import stopwords
import string
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt','RT', 'via','ó','ल','ु','்','ज','I','ब','य','द','ै','ट','भ','ग','प','व','ி','श','amp','https','ू','।','ध','ு','च','1','ा','https://t.co/47peyx2jtb','https://t.co/nnhx44sp6h','https://t.co/sggd4y6jpt','https://t.co/poe'] 
fname = 'D:/Twitter_mining/bb2.json'

with open(fname, 'r',newline='\r\n') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Count terms only once, equivalent to Document Frequency
        terms_single = set(terms_stop)
        # Count hashtags only
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
              # Count terms only (no hashtags, no mentions)
        terms_only = [term for term in preprocess(tweet['text'].lower()) if term not in stop  and not term.startswith(( '@', '#')) ] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs
        
        terms_all = [term for term in preprocess(tweet['text'])]
        #print (terms_all)
        new_terms = []
        for term in terms_only:
            if len(term) > 3:
                new_terms.append(term)
                
            
        # Update the counter
        count_all.update(new_terms)
        #count_all.update(terms_only)
    # Print the first 5 most frequent words
    print(count_all.most_common(50))

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

data = count_all.most_common(50)
df = pd.DataFrame(data)
df.columns = ('terms','frec')
print(df.head())
#df.to_csv('word_freq.csv')
word_string = ''
for index, row in df.iterrows():
    #print ((row['terms'] + ' ')*row['frec'])
    word_string += (row['terms'] + ' ')*int(row['frec']/180)
    
#print (word_string)
   
wordcloud = WordCloud(font_path='D:/Twitter_mining/Aaargh.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(word_string)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()

#wordcloudtest = WordCloud(font_path='D:/Twitter_mining/Aaargh.ttf',
#                          stopwords=STOPWORDS,
#                          background_color='white',
#                          width=2000,
#                          height=1800
#                         ).generate('suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit suchit shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet shwet')
#
#plt.imshow(wordcloudtest)
#plt.axis('off')
#plt.show()
#df.plot(kind='bar')

#plt.show()