def compute(n):
    return n

def solution(string):
    numbers = [int(x) for x in string.split(" ")]
    cache = dict()

    for number in numbers:
        if number in cache:
            continue
        else:
            cache[number] = compute(number)

    answer = [str(cache[number]) for number in numbers]
    print(" ".join(answer))

solution("1 1 3 4 3 6 3")