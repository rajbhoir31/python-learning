# f = open("myfile.txt", "r")

# content = f.read()      # Reads entire file as a single string
# print(content)

# f.close()

# with open("myfile.txt", "r") as f:
#     for line in f:
#         print(line.strip())   # remove \n

# with open("myfile.txt", "w") as f:
#     f.write("This is the first line.\n")
#     f.write("This is the second line.\n")

def read_file(x):
    """
    Reads the entire file and returns all lines as a list (without newline characters).
    """
    with open(x, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def count_words_per_line(x):
    """
    Prints each line's number and how many words it contains.
    """
    lines = read_file(x)
    for i, line in enumerate(lines, start=1):
        word_count = len(line.split())
        print(f"Line {i}: {word_count} words")

filename = input("Enter filename : ")
print(read_file(filename))
print(count_words_per_line(filename))