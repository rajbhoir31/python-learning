"""
List unique words in lowercase
"""

def unique_words(x):
    sentence = sentence.lower()
    words = sentence.split()
    unique = set(words)
    return list(unique)

sentence = input("Enter words : ")
print(unique_words(sentence))
