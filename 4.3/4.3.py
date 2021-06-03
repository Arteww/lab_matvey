import numpy as np

with open('outfile.txt', 'w', encoding='utf-8') as outfile:
    N = 5
    float_list = list(np.random.rand(N))
    outfile.write(str(float_list) + '\n')

    for i in range(5):
        min_index = float_list.index(min(float_list[i:]))
        float_list[i], float_list[min_index] = float_list[min_index], float_list[i]
    outfile.write(str(float_list))
