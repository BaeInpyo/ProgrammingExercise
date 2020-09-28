import sys

def read_input():
    """ Read input and return (age, heartrate) """
    nums = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        nums.append(int(line))

    return nums[0], nums[1:]    # age, 심박수

def solution(age, heartrates):
    """ Print answer with given (age, heartrates) """
    # 6 ranges of workout
    answer = [0] * 6

    max_rate = 220 - age
    for rate in heartrates:
        ratio = rate / max_rate
        if ratio < 0.6:
            answer[5] += 1
        elif 0.6 <= ratio < 0.68:
            answer[4] += 1
        elif 0.68 < ratio < 0.75:
            answer[3] += 1
        elif 0.75 <= ratio < 0.8:
            answer[2] += 1
        elif 0.8 <= ratio < 0.9:
            answer[1] += 1
        elif 0.9 <= ratio:
            answer[0] += 1

    answer_string = " ".join([str(x) for x in answer])
    print(answer_string)
    return

if __name__ == "__main__":
    age, heartrates = read_input()
    solution(age, heartrates)
