with open('infile.txt', 'r', encoding='utf-8') as infile:
    with open('outfile.txt', 'w', encoding='utf-8') as outfile:
        text = infile.read()
        text = text.split()
        for word in text:
            if 21 > len(word) > 1:
                outfile.write(word + "\n")
