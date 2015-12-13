from mapreduce import MapReduce
import re
#-----------------------------------

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            yield (char,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

#-----------------------------------
string = open('alice.txt').read()
new_str = re.sub('[^a-zA-Z]', '', string)
x = new_str.replace(' ', '')

x = new_str.strip().split('\n')

output = CharCount.run(x)
for item in output:
    print item
