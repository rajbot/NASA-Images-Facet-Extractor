#!/opt/local/bin/python

import re

def facet_dict(string):
    facet_file = 'facets.txt'
    facet_list = open(facet_file,'rb').read().split('\n')
    dictionary = {}
    for facet in facet_list:
        k,v = facet.split(',')[0], facet.split(',')[-1]
        dictionary[k] = v
    print len(dictionary)
    faceted = {}
    words = string.split()
    for word in words:
        print word
        if word in dictionary:
            faceted[word] = dictionary[word]

    #for k,v in dictionary.iteritems():
    #    if k in string:
    #        faceted[k] = v
    return faceted

def main():
    #t = open('text','rb').read()
    print facet_dict(' STS-1 STS-123 ')

if __name__ == "__main__":
    main()
