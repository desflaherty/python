import re
import collections

text = open('book.txt').read().lower()
words = re.findall('\w+',text) # any occurance that is not a whitespace (w)
print(collections.Counter(words).most_common(10)) # top 10 words

