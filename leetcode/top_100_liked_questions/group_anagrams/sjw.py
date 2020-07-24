"""
Problem URL: https://leetcode.com/problems/group-anagrams/

1. Use union-find => cannot define parent
2. Use frozenset => Cannot handle "boo", "bob"
3. Counter => unhashable => make it hashable
"""

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = dict()
        for string in strs:
            count = Counter(string)
            count = tuple(sorted(count.items()))
            if count in answer:
                answer[count].append(string)
            else:
                answer[count] = [string]

        return answer.values()