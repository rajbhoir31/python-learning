"""
Count vowels in a string
"""

def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    count = {}

    for char in text:
        if char in vowels:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count

user_input = input("Enter a sentence: ")

vowel_count = count_vowels(user_input)

print("Vowel counts:", vowel_count)
