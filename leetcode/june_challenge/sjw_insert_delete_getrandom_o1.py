"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3358/
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._set:
            return False
        else:
            self._set.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self._set:
            self._set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_index = random.randint(0, len(self._set)-1)
        return tuple(self._set)[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()