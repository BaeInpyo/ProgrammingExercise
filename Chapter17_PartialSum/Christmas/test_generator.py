import random

input_filename = './input.txt'

T = 60
MAX = 100000

candidate = [i+1 for i in range(0, MAX)]
input_file = open(input_filename, 'w')
input_file.write(str(T) + '\n')
for _ in range(0, T):
    N = random.randint(0, MAX)
    K = random.randint(0, MAX)
    input_file.write(str(N) + ' ' + str(K) + '\n');
    for _ in range(0, N):
        D_i = random.choice(candidate)
        input_file.write(str(D_i) + ' ')
    input_file.write('\n')

input_file.close()
