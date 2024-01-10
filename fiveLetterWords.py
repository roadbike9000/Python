# Write a function that accepts a string as an argument and returns a list
# with all the words that are five letters long in that text. For example,
# assume you have a string with the following text:

# "This is a text file with some words I wrote. One thing is certain: this prose will not win any literary prizes."
# Your function should return the list:

# ['words', 'wrote', 'thing', 'prose']
# Remember the punctuation marks!
import string
text = "This is a text file with some words I wrote. One thing is certain: this prose will not win any literary prizes."
five_letter_words = []


def look_for_punctuation(word):
    # Check if last letter of word is punctuation and remove it if it is
    if word[-1] in string.punctuation:
        word = word[0:-1]

    return word


def look_for_five_letter_words(text):
    five_letter_words = []
    # Make list of words
    words = text.split()
    # Check words for punctuation
    for word in words:
        parsed_words = [look_for_punctuation(word) for word in words]

    # Check for words with five letters
    for word in parsed_words:
        if len(word) == 5:
            five_letter_words.append(word)

    return five_letter_words


# five_letter_words = look_for_five_letter_words(text)
print(look_for_five_letter_words(text))
