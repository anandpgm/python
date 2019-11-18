# Write a Python program to count the occurrences of each word in a given sentence.
import collections
def word_count(s1):
    words = s1.split()
    print(words)
    ctr = collections.Counter(words)
    print(dict(ctr))


word_count("hi this is the input hi")