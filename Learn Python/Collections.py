import collections
from collections import defaultdict
#print(collections.__doc__)

fruits = ["apple","banana","apple","orange"]

print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common)
word_dict = collections.defaultdict(list)
word_dict["python"].append("Programming Language")
print(word_dict)