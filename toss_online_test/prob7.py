def solution(string):
    startingPointer = int(string[0])
    src_space = [int(x) for x in string[3:].split()]
    dst_space = [0] * 8

    assert(len(src_space) == 8)

    dst_index = 0   # first valid index of dst_space
    while True:
        num1, num2 = src_space[startingPointer], src_space[startingPointer+1]
        if num1 == 0:
            dst_space[dst_index] = 0
            dst_space[dst_index+1] = dst_index + 2
            dst_index += 2
            startingPointer = num2

        elif num1 == 1:
            dst_space[dst_index] = 1
            dst_space[dst_index+1] = num2
            break

    answer = "0; " + " ".join([str(x) for x in dst_space])
    print(answer)

solution("4; 1 30 0 6 0 2 1 3")
