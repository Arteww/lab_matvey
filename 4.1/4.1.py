import numpy as np

with open('outfile.txt', 'w', encoding='utf-8') as outfile:
    N = 5
    float_list = list(np.random.rand(N))
    outfile.write(str(float_list) + '\n')

    max_ind = float_list.index(max(float_list))
    min_ind = float_list.index(min(float_list))
    float_list[max_ind], float_list[min_ind] = float_list[min_ind], float_list[max_ind]
    outfile.write(str(float_list))
