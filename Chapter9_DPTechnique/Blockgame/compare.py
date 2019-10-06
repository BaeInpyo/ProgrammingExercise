import random
import os
import subprocess

def int_to_board(num):
    binary = str(bin(num))[2:]
    binary = [int(x) for x in binary]
    binary = [0] * (25 - len(binary)) + binary
    board = [['.', '#'][x] for x in binary]

    _board = []
    # convert 1d to 2d
    for i in range(0, 25, 5):
        _board.append(''.join(board[i:i+5]))

    return _board

random.seed(0)
C = 20

# generate random input
nums = []
for _ in range(C):
    nums.append(random.randint(0, 1<<24))

# make input.txt
input_text = ''
input_text += '{}\n'.format(C)
for num in nums:
    board = int_to_board(num)
    for row in board:
        input_text += '{}\n'.format(row)

abs_dir = os.path.dirname(os.path.abspath(__file__))
# write board to input.txt
with open(os.path.join(abs_dir, 'input.txt'), 'w') as f:
    f.write(input_text)

os.system('g++ {} -o {}'.format(
    os.path.join(abs_dir, 'vip_blockgame.cpp'),
    os.path.join(abs_dir, 'vip_blockgame')
))
print('vip_blockgame.cpp is compiled\n')

cmd = '{} < {}'.format(os.path.join(abs_dir, 'vip_blockgame'), os.path.join(abs_dir, 'input.txt'))
print(cmd, '\n')
vip_result = subprocess.check_output(cmd, shell=True)   # bytes
vip_result = vip_result.decode('utf-8')                 # bytes to string
vip_result = vip_result.split('\n')

cmd = 'python {} < {}'.format( os.path.join(abs_dir, 'sjw_blockgame.py'), os.path.join(abs_dir, 'input.txt'))
print(cmd, '\n')
sjw_result = subprocess.check_output(cmd, shell=True)   # bytes
sjw_result = sjw_result.decode('utf-8')                 # bytes to string
sjw_result = sjw_result.split('\n')

# print board and results when vip and sjw are different
for i, (vip, sjw) in enumerate(zip(vip_result, sjw_result)):
    if vip != sjw:
        int_to_board(nums[i])
        print('vip: {}, sjwL {}'.format(vip, sjw))

print('Finished')