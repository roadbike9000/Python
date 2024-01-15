# Write a function that accepts a string and an integer as an arguments and returns a list
# The string is the text to search. The integer is the length of the words to search for
# in the string. For example,
# assume you have a string with the following text:

# "This is a text file with some words I wrote. One thing is certain: this prose will not win any literary prizes."
# Your function should return the list:

# ['words', 'wrote', 'thing', 'prose']
# Remember the punctuation marks!
import string
text = "This is a text file with some words I wrote. One thing is certain: this prose will not win any literary prizes."
word_length = 10



def look_for_punctuation(word):
    # Check if last letter of word is punctuation and remove it if it is
    if word[-1] in string.punctuation:
        word = word[0:-1]

    return word


def look_for_words(text, word_length):
    words_of_a_certain_length = []
    # Make list of words
    words = text.split()
    # Check words for punctuation
    for word in words:
        parsed_words = [look_for_punctuation(word) for word in words]

    # Check for words with five letters
    for word in parsed_words:
        if len(word) == word_length:
            words_of_a_certain_length.append(word)

    return words_of_a_certain_length


# five_letter_words = look_for_five_letter_words(text)
print(look_for_words(text, word_length))
