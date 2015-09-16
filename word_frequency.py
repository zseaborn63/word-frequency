# Simpler form

with open("sample.txt") as infile:
    book = infile.read()
    
import string
    
def word_frequency(file):
    file = file.lower()
    for c in string.punctuation:
        file = file.replace(c, "")
    for c in string.whitespace:
        file = file.replace(c, " ")
    word = file.split()
    word_dict = {}
    for word in word:
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

unsorted_mess = word_frequency(book)
word_list = word_list(unsorted_mess)
sort_list(word_list, 20)


