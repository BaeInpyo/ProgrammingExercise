import sys, os
from collections import defaultdict

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')


'''
optimization
    - if some food covers all people, no need to further calculation (O)
    - remove food that is included by another food (O)
    - if some food cover only 1 people, it must be added (O)
    - if some people only eat 1 food, it's food must be added (O)

question
    - top down vs bottom up, which one is better?
        - top down => time exceed
'''

N, M = None, None
MINIMAL, FOOD_SET, PEOPLE_SET = None, None, None
FOOD_TO_PEOPLE = None       # key: food number, value: people number


# return if further calculation needed or not
def parse_input():
    global N, M

    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    food_set = set(range(M))
    people_set = set(sys.stdin.readline().strip().split())

    people_to_number = { people: index for (index, people) in enumerate(list(people_set)) } # key: people name, value: number
    food_to_people = defaultdict(set) # key: food, value: set of people
    for idx in range(M):
        curr = sys.stdin.readline().strip().split()[1:]
        curr = [people_to_number[people] for people in curr]
        food_to_people[idx] = curr

    global MINIMAL, FOOD_SET, PEOPLE_SET, FOOD_TO_PEOPLE
    MINIMAL = M
    FOOD_SET = food_set
    PEOPLE_SET = people_set
    FOOD_TO_PEOPLE = food_to_people

    return

def recur(food_count, people_check, start_idx):
    global MINIMAL

    # MINIMAL is already found
    if MINIMAL <= food_count:
        return

    # if all people are available, return
    if people_check == (1 << N) - 1:
        MINIMAL = min(food_count, MINIMAL)
        return

    # add food
    for food_idx in range(start_idx, M):
        # if current food is useless, continue
        useful = sum([pow(2, number) for number in FOOD_TO_PEOPLE[food_idx]])
        useful = useful & (people_check ^ ((1 << N) - 1))
        if useful == 0:
            continue

        # set parameters
        food_count += 1
        people_check = people_check | useful

        # go deeper
        recur(food_count, people_check, food_idx + 1)

        # unset parameters
        food_count -= 1
        people_check = people_check & (useful ^ ((1 << N) - 1))

    return


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        parse_input()

        # start food_set with empty and add food (bottom up)
        food_count = 0

        # use number as list of boolean
        people_check = 0

        start_idx = 0

        recur(food_count, people_check, start_idx)
        print(MINIMAL)