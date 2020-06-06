"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (x[1], x[0]))
        result = []
        for (h, k) in people:
            if k == 0:
                result.append([h, k])

            else:
                count = 0
                for idx, (_h ,_k) in reversed(list(enumerate(result))):
                    if _h >= h:
                        count += 1

                    if count == k:
                        break

                result.insert(idx+1, [h, k])

            print(result)

        return result
