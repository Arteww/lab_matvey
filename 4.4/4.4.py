import random
N = 20
diapason = (0, 500)
random_list = [random.randint(*diapason) for i in range(N)]
print(random_list)
for i in range(N):
    value = random_list[i]
    index = i
    while (index > 0) and (random_list[index - 1] > value):
        random_list[index] = random_list[index - 1]
        index -= 1
    random_list[index] = value
print(random_list)
