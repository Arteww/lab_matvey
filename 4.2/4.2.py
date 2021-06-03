with open('infile.txt', 'r', encoding='utf-8') as infile:
    # 4.2.1
    with open('f1.txt', 'w', encoding='utf-8') as f1:
        for num in infile:
            f1.write(str(num))
    # 4.2.2
    with open('f1.txt', 'r', encoding='utf-8') as f1:
        with open('outfile.txt', 'w', encoding='utf-8') as outfile:
            nums = []
            for num in f1:
                nums.append(num)
            outfile.writelines(nums)
