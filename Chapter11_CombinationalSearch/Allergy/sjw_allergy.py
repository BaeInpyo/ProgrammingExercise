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
FOOD_TO_PEOPLE = None       # key: food number, value: people


# return if further calculation needed or not
def parse_input():
    global N, M

    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    food_set = set(range(M))
    people_set = set(sys.stdin.readline().strip().split())

    people_to_number = { people: index for (index, people) in enumerate(list(people_set)) } # key: people name, value: number
    food_to_people = defaultdict(set) # key: food, value: set of people
    for idx in range(M):
        food_to_people[idx] = set(sys.stdin.readline().strip().split()[1:])

    global MINIMAL, FOOD_SET, PEOPLE_SET, FOOD_TO_PEOPLE
    MINIMAL = M
    FOOD_SET = food_set
    PEOPLE_SET = people_set
    FOOD_TO_PEOPLE = food_to_people

    return

def recur(food_set, people_check, start_idx):
    global MINIMAL
    # if all people are available, return
    if all(people_check.values()):
        MINIMAL = min(len(food_set), MINIMAL)
        return

    # add food
    for food_idx in FOOD_SET:
        if food_idx < start_idx:
            continue

        # if current food is useless, continue
        useful = [people for people in FOOD_TO_PEOPLE[food_idx] if people_check[people] == False]
        if not useful:
            continue

        # set parameters
        food_set.add(food_idx)
        for people in useful:
            people_check[people] = True

        # go deeper
        recur(food_set, people_check, food_idx + 1)

        # unset parameters
        food_set.remove(food_idx)
        for people in useful:
            people_check[people] = False

    return


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        parse_input()

        # start food_set with empty and add food (bottom up)
        food_set = set()

        # set boolean array for people check
        people_check = { people: False for people in PEOPLE_SET }

        recur(food_set, people_check, 0)
        print(MINIMAL)