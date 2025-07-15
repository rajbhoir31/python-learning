import string

filename = input("Enter the filename to analyze: ")

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found.")
    exit()

clean_text = text.translate(str.maketrans("", "", string.punctuation))
words = clean_text.lower().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

max_count = max(word_count.values())
most_common = [word for word, count in word_count.items() if count == max_count]

with open("summary.txt", "w") as out:
    out.write(f"Total words: {len(words)}\n")
    out.write(f"Unique words: {len(word_count)}\n")
    out.write(f"Most frequent word(s): {most_common} ({max_count} times)\n\n")
    out.write("Word Frequencies:\n")
    for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
        out.write(f"{word}: {count}\n")

with open("summary.txt", "r") as result:
    print(result.read())
