text_file = open('text.txt', 'r')

punctuations = ["-", "_", ":", ";", ",", "'", '"', ".", "!", "?"]
result_list = []

char_counter = 0
punctuation_counter = 0
line_counter = 1
output = open('output.txt', 'w')

for line in text_file:
    for char in line:
        if char.isalpha():
            char_counter += 1
        elif char in punctuations:
            punctuation_counter += 1
        elif char == "\n":
            line.replace("\n", "")

    output.write(f"Line {line_counter}: {line.strip()} ({char_counter})({punctuation_counter})\n")

    char_counter = 0
    punctuation_counter = 0
    line_counter += 1

text_file.close()
output.close()
