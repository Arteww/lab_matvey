import random
N = 5
random_list = []
with open('outfile.txt', 'w', encoding='utf-8') as file:
    for i in range(N):
        random_list.append(random.random())
    file.write(str(random_list) + '\n')
    max = random_list.index(max(random_list))
    min = random_list.index(min(random_list))
    random_list[max], random_list[min] = random_list[min], random_list[max]
    file.write(str(random_list))
