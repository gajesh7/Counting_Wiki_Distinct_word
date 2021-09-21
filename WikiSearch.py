import re
import urllib.request
from collections import Counter

URL = 'https://en.wikipedia.org/wiki/Engineering'

counter = Counter()

with urllib.request.urlopen(URL) as source:
    for line in source:
        words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
        counter.update(words)

#word=input("Enter your word:")#the word you wanna search in that Engineers page"""
#print('{}:{}'.format(word, counter[word]))


#this code also works
for word in ['Engineering', 'Engineers', 'Engineer','engineers']:
  print('{}: {}'.format(word, counter[word]))
