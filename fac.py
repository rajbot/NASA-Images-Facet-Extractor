#!/opt/local/bin/python

import re

def facet_dict(string):
    facet_file = 'facets.txt'
    facet_list = open(facet_file,'rb').read().split('\n')
    dictionary = {}
    for facet in facet_list:
        k,v = facet.split(',')[0], facet.split(',')[-1]
        dictionary[k] = v
    faceted = {}
    for k,v in dictionary.iteritems():
        if k in string:
            faceted[k] = v
    return faceted

def main():
    #t = open('text','rb').read()
    print facet_dict(' STS-135 ')

if __name__ == "__main__":
    main()
