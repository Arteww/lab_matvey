import random
N = 10
random_list = []
with open('outfile.txt', 'w', encoding='utf-8') as file:
    for i in range(N):
        random_list.append(random.random())
    file.write(str(random_list) + '\n')
    for i in range(N):
        min_index = random_list.index(min(random_list[i:]))
        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]
    file.write(str(random_list))
