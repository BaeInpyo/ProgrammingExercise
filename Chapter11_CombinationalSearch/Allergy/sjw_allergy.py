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
'''

N, M = None, None
MINIMAL, NECESSARY, FOOD_SET, PEOPLE_SET = None, None, None, None
FOOD_TO_PEOPLE = None       # key: food number, value: set of people number
PEOPLE_TO_NUMBER = None     # key: people name, value: people number, this is for debug


# return if further calculation needed or not
def parse_input():
    global N, M

    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    food_set = set(range(M))
    people_set = set(sys.stdin.readline().strip().split())

    food_to_people = defaultdict(set) # key: food, value: set of people
    for idx in range(M):
        food_to_people[idx] = set(sys.stdin.readline().strip().split()[1:])

    # if some food cover all people, no need to go further
    for _people_set in food_to_people.values():
        if len(_people_set) == N:
            return False

    # if food A is subset of food B, remove food A
    for A in food_set.copy():
        for B in food_set.copy():
            if A <= B:
                continue

            if food_to_people[A].issubset(food_to_people[B]):
                food_set.discard(A)
                break

    for food in food_to_people.copy():
        if food not in food_set:
            food_to_people.pop(food, None)  # remove unnecessary food

    necessary = 0

    # if some people only eat 1 food, this food must is necessary
    people_to_food = defaultdict(set) # key: people, value: set of food
    for (food, people) in food_to_people.items():
        for p in people:
            curr = people_to_food.get(p, set())
            curr.add(food)

    for (people, food) in people_to_food.items():
        if len(food) == 1:
            necessary += 1
            food_set.discard(food)
            for _people in food_to_people[food]:
                people_set.discard(_people)

    # if some food cover only 1 people, this food is necessary
    for food in food_set.copy():
        curr = food_to_people[food]
        if len(curr) == 1:
            necessary += 1
            food_set.discard(food)
            people_set.discard(curr.pop())

    global NECESSARY, FOOD_SET, PEOPLE_SET, FOOD_TO_PEOPLE, PEOPLE_TO_NUMBER
    NECESSARY, FOOD_SET, PEOPLE_SET = necessary, food_set, people_set
    people_list = list(people_set)
    PEOPLE_TO_NUMBER = { name: number for (number, name) in enumerate(people_list) }
    FOOD_TO_PEOPLE = defaultdict(set)
    for food in food_set:
        set_people_number = set()
        for name in food_to_people[food]:
            set_people_number.add(PEOPLE_TO_NUMBER[name])

        FOOD_TO_PEOPLE[food] = set_people_number

    return True


def recur(food_set, eatable_food_for_people, start_idx):
    global MINIMAL
    # if food_set cannot serve all, return
    if not all(eatable_food_for_people.values()):
        return

    # if minimal food_set found, save it
    if len(food_set) < MINIMAL:
        MINIMAL = len(food_set)

    # remove food
    for food_idx in food_set:
        if food_idx < start_idx:
            continue

        # set food_set and eatable_food_for_people
        food_set.discard(food_idx)
        for people in FOOD_TO_PEOPLE[food_idx]:
            eatable_food_for_people[people] -= 1

        recur(food_set, eatable_food_for_people, food_idx + 1)

        # recover food_set and eatable_food_for_people
        food_set.add(food_idx)
        for people in FOOD_TO_PEOPLE[food_idx]:
            eatable_food_for_people[people] += 1

    return


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        result = parse_input()

        # if some food cover all people, no need to go further
        if not result:
            print(1)
            continue

        # start food_set with all food (some food may be removed if subset of another food)
        food_set = FOOD_SET.copy()
        MINIMAL = len(food_set)

        # set number of eatable food for every people
        eatable_food_for_people = defaultdict(int)
        for (food, people) in FOOD_TO_PEOPLE.items():
            for number in people:
                eatable_food_for_people[number] += 1

        recur(food_set, eatable_food_for_people, 0)
        print(MINIMAL + NECESSARY)