with open('infile.txt', 'r', encoding='utf-8') as file:
    with open('f1.txt', 'w', encoding='utf-8') as f1:
        for b in file:
            f1.write(str(b))
    with open('f1.txt', 'r', encoding='utf-8') as f1:
        with open('outfile.txt', 'w', encoding='utf-8') as outfile:
            a = []
            for b in f1:
                a.append(b)
            outfile.writelines(a)
