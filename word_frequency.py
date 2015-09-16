# Normal Mode Complete

with open("sample.txt") as infile:
    book = infile.read()
    
import string
    
def remove_punctuation_and_lines(x):
    x = x.lower()
    for c in string.punctuation:
        x = x.replace(c, "")
    for c in string.whitespace:
        x = x.replace(c, " ")
    return x

def word_dictionary(x):
    word_dict = {}
    for word in x:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def word_list(dictionary):
    word_list = list(dictionary.items())
    return word_list

def sort_list(a_list, how_many):
    sorted_list = sorted(a_list, reverse = True, key= lambda x: x[1])[:how_many]
    for word, appears in sorted_list:
        print("{} {}".format(word, appears))

only_words = remove_punctuation_and_lines(book)
listed_words = only_words.split()
unsorted_mess = word_dictionary(listed_words)
word_list = word_list(unsorted_mess)
sort_list(word_list, 5)


