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

def write_summary(x, y):
    """
    Reads input_file, counts words per line,
    and writes a summary to output_file.
    """
    lines = read_file(x)
    
    with open(y, 'w') as f_out:
        for i, line in enumerate(lines, start=1):
            word_count = len(line.split())
            f_out.write(f"Line {i}: {word_count} words\n")
    
    print(f"Summary written to '{y}'")


print(read_file('input.txt'))
count_words_per_line('input.txt')
write_summary('input.txt', 'summary.txt')
