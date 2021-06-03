alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
symbol_c = 0
letter_c = 0
notletter_c = 0
with open('infile.txt', 'r', encoding='utf-8') as infile:
    with open('outfile.txt', 'w', encoding='utf-8') as outfile:
        text = infile.read()
        for symbol in text.lower():
            if symbol in alphabet:
                alphabet[symbol] += 1
                letter_c += 1
            else:
                notletter_c += 1
            symbol_c += 1
        outfile.write(f"symbols: {symbol_c}\n"
                      f"letters: {letter_c}\n"
                      f"other symbols (not letters): {notletter_c}\n\n")
        for i in alphabet:
            outfile.write(f"{i}: {alphabet[i]}\n")
