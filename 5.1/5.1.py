with open('infile.txt', 'r', encoding='utf-8') as infile:
    with open('outfile.txt', 'w', encoding='utf-8') as outfile:
        text = infile.read()
        while "  " in text:
            text = text.replace("  ", " ")
        outfile.write(text)
