"""
Reverse words in a sentence
Input: "Hello world" → Output: "olleH dlrow"
"""

def reverse (x):
  words = sentence.split()
  reverse = [word[::-1] for word in words]
  return " ".join(reverse)

sentence = input("Enter sentence : ")
print(reverse(sentence))