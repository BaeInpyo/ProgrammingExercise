import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        weights = [0]
        # calculate accumulative sum
        for weight in w:
            weights.append(weights[-1] + weight)

        # divide by sum(self.w) which leads to probability
        weights = [weight / sum(w) for weight in weights]
        self.weights = weights

    def pickIndex(self) -> int:
        # pick random value in [0, 1)
        random_value = random.random()

        # find random value's index
        index = bisect.bisect_right(self.weights, random_value) - 1

        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()