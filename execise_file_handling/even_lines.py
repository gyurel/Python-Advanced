text_file = open('text.txt', 'r')

to_replace = ["-", ",", ".", "!", "?"]

counter = 0
for line in text_file:
    if counter % 2 == 0:
        for _ in range(len(line)):
            char = line[_]
            if char in to_replace:
                line = line.replace(char, "@")
        line = line.split()
        line = line[::-1]
        print(' '.join([x for x in line]))
        counter += 1
    else:
        counter += 1
        continue
text_file.close()
