"""
Problem URL: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3404/

This is quite tricky problem.
You can draw 2d matrix and think about the solution.
"""

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        counts = sorted(count.values(), reverse=True)
        max_count = counts[0] - 1   # we can ignore last occurence
        idle_slots = max_count * n
        for idx in range(1, len(counts)):
            # there can be multiple max_count, e.g) ["A", "A", "B", "B"]
            # therefore we use min() here
            idle_slots -= min(max_count, counts[idx])

        # count idle_slot only if it exists
        return max(len(tasks), len(tasks) + idle_slots)