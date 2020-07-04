"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/
"""

"""
Since each cell's next state is dependent on adjacent 2 cells, total row will
repeat in 8 steps. (2^3 = 8)
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        states = [cells]
        step = 1
        while True:
            prev = states[-1]
            curr = [None] * 8
            for idx in range(8):
                if idx == 0 or idx == 7:
                    curr[idx] = 0
                else:
                    curr[idx] = 1 if prev[idx-1]==prev[idx+1] else 0

            if curr in states:
                # print("haha")
                # print(states)
                # print(curr)
                idx = states.index(curr)
                start, end = idx, step-1
                break
            else:
                states.append(curr)
                step += 1

        # print("start, end:", start, end)
        # for idx, row in enumerate(states):
        #     print(idx, row)
        # cycle from start ~ end
        if N <= end:
            return states[N]
        else:
            return states[(N-start)%(end-start+1) + (start)]
