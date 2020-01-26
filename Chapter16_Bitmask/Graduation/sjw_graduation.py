import sys
import os

abs_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(abs_dir, "input.txt"), "r")

# read line and return list of integer
def read_line():
    return [int(x) for x in sys.stdin.readline().strip().split()]

def solution(N, K, M, L, requisite, semester):

    def count_bits(bitmask):
        """
        return number of bits in bitmask
        """
        return bin(bitmask)[2:].count("1")

    def recur(taken_subjects, curr_semester, num_taken_semester):
        """
        return minimun number of semester which can cover K subjects
        int taken_subjects:
            bitmask which represents set of taken subjects
        int curr_semester:
            index of semester
        int num_taken_semester:
            number of taken semesters
        """

        # taken more than K subjects
        if count_bits(taken_subjects) >= K:
            return num_taken_semester

        # reach end of semester
        if curr_semester == M:
            return M

        # return minumum of cases
        cases = []

        # case: skip current semester
        cases.append(recur(
            taken_subjects, curr_semester + 1, num_taken_semester
        ))

        # remove already taken subjects
        # set difference
        available_subjects = semester[curr_semester] & (~taken_subjects)

        # remove unsatisfied subject
        for digit, enabled in enumerate(reversed(bin(available_subjects)[2:])):
            if requisite[digit] & taken_subjects != requisite[digit]:
                available_subjects = available_subjects & (~(1 << digit))

        if count_bits(available_subjects) <= L:
            # case: take as many subjects as possible
            cases.append(recur(
                taken_subjects | available_subjects, curr_semester + 1,
                num_taken_semester + 1
            ))
        else:
            # case: consider all subsets of subjects available on current
            # semester whose length is L
            subset = available_subjects
            while subset > 0:
                subset = (subset - 1) & available_subjects
                if count_bits(subset) == L:
                    cases.append(recur(
                        taken_subjects | subset, curr_semester + 1,
                        num_taken_semester + 1
                    ))

        # return minimum
        return min(cases)

    # starts from empty set
    answer = recur(taken_subjects=0, curr_semester=0, num_taken_semester=0)
    answer = "IMPOSSIBLE" if answer == M else answer

    # return string instead of integer to use join()
    return str(answer)


if __name__ == "__main__":
    C = int(sys.stdin.readline().strip())
    answers = []
    for _ in range(C):
        N, K, M, L = read_line()
        requisite = []
        for _ in range(N):
            bitmask = 0
            for subject in read_line()[1:]:
                bitmask |= 1 << subject # bitwise union
            requisite.append(bitmask)
        semester = []
        for _ in range(M):
            bitmask = 0
            for subject in read_line()[1:]:
                bitmask |= 1 << subject # bitwise union
            semester.append(bitmask)

        answers.append(solution(N, K, M, L, requisite, semester))

    sys.stdout.write("\n".join(answers))