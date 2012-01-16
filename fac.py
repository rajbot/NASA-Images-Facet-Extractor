#!/usr/bin/env python
import string

def build_dict():
    facet_file = 'facets.txt'
    facet_list = open(facet_file,'rb').read().split('\n')
    dictionary = {}
    max_words_in_key = 0
    for facet in facet_list:
        k,v = facet.split(',')[0], facet.split(',')[-1]
        k = k.strip().lower()
        if not k:
            continue
        words_in_key = len(k.split(' '))
        if words_in_key > max_words_in_key:
            max_words_in_key = words_in_key
        dictionary[k] = v.strip()

    return dictionary, max_words_in_key


def get_phrase(words, phrase_length, start_pos):
    """
    >>> words = "this is a five word sentence".split(' ')
    >>> get_phrase(words, 1, 3)
    'five'
    >>> get_phrase(words, 2, 3)
    'five word'
    """
    s = ''
    for i in range(phrase_length):
        s += words[start_pos+i] + ' '
        exclude =set(['!', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', ',',
                      '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']', '\\',
                      '^', '`', '{', '}', '|', '~'])
        s = ''.join(ch for ch in s if ch not in exclude)
    return s[:-1]

def get_facets(string, dictionary, longest_key):
    """extract facets from string
    >>> d, longest_key = build_dict()
    >>> get_facets(' STS-1 STS-123 ', d, longest_key)
    {'STS-123': 'What --', 'STS-1': 'What --'}

    >>> get_facets('STS-1', d, longest_key)
    {'STS-1': 'What --'}
    >>> get_facets('STS-123', d, longest_key)
    {'STS-123': 'What --'}

    >>> get_facets('Ain', d, longest_key)
    {'Ain': 'What --'}
    >>> get_facets('Ain al Rami', d, longest_key)
    {'Ain al Rami': 'What --'}
    >>> get_facets('Ain Ain al Rami', d, longest_key)
    {'Ain': 'What --', 'Ain al Rami': 'What --'}

    >>> get_facets('Venus', d, longest_key)
    {'Venus': 'Where --'}
    >>> get_facets('Venus Express', d, longest_key)
    {'Venus Express': 'What --'}

    >>> get_facets('Virgo', d, longest_key)
    {'Virgo': 'What --'}
    >>> get_facets('Virgo Stellar Stream', d, longest_key)
    {'Virgo Stellar Stream': 'Where --'}

    >>> get_facets('Virgo. STS-123, STS-1!', d, longest_key)
    {'Virgo': 'What --', 'STS-123': 'What --', 'STS-1': 'What --'}
    """
    faceted = {}
    words = string.split()
    num_words = len(words)
    pos = 0

    #print 'num_words = ' + str(num_words)
    #print 'longest_key = ' + str(longest_key)
    while pos < num_words:
        #print 'checking pos ' + str(pos)
        phrase_length = min(longest_key, num_words-pos)
        found_phrase = False
        while phrase_length > 0:
            #print ' checking phrase length ' + str(phrase_length)

            phrase = get_phrase(words, phrase_length, pos)
            print ' got phrase ' + phrase
            if phrase.lower() in dictionary:
                #print '  phrase matched!'
                found_phrase = phrase.lower()
                break
            phrase_length -= 1

        if False != found_phrase:
            faceted[found_phrase] = dictionary[found_phrase]
            pos += phrase_length
        else:
            pos += 1

        #print 'end of outer while'

    return faceted

def main():
    #t = open('text','rb').read()
    facet_dict, longest_key = build_dict()
    facets = get_facets('Virgo. sts-123, STS-1!', facet_dict, longest_key)
    print facets

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
