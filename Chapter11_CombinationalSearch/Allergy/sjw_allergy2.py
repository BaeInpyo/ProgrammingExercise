import sys, os
from collections import defaultdict

# freopen equivalent
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.stdin = open(os.path.join(abs_path, 'input.txt'), 'r')

def recur(num_selected_food):
    global SATISFIED, MINIMAL

    if num_selected_food >= MINIMAL:
        return

    # find person that cannot eat any food
    is_all_satisfied = False
    not_satisfied = None
    for person in SATISFIED:
        if SATISFIED[person] == 0:
            not_satisfied = person
            break

    # if all person are edible, return
    if not_satisfied is None:
        MINIMAL = num_selected_food
        return

    # select food to make person edible
    edible = PEOPLE_TO_FOOD[not_satisfied]
    for food in edible:
        # set SATISFIED
        for people in FOOD_TO_PEOPLE[food]:
            SATISFIED[people] += 1

        recur(num_selected_food + 1)

        # unset SATISFIED
        for people in FOOD_TO_PEOPLE[food]:
            SATISFIED[people] -= 1


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N, M = [int(x) for x in sys.stdin.readline().strip().split()]
        PEOPLE = sys.stdin.readline().strip().split()
        FOOD_TO_PEOPLE = dict()             # key: food, value: list of people that can eat this food
        PEOPLE_TO_FOOD = defaultdict(list)  # key: people, value: list of edible food
        for food in range(M):
            _, *people = sys.stdin.readline().strip().split()
            FOOD_TO_PEOPLE[food] = people
            for p in people:
                PEOPLE_TO_FOOD[p].append(food)

        # we will search food first that can server many people
        for people in PEOPLE_TO_FOOD:
            PEOPLE_TO_FOOD[people].sort(key = lambda x: len(FOOD_TO_PEOPLE[food]))

        SATISFIED = { p: 0 for p in PEOPLE }   # check if each person can eat food
        MINIMAL = M
        recur(0)
        print(MINIMAL)