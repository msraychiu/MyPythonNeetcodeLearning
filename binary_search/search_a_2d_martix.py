from itertools import chain
from typing import List


class Solution:
    # flatten array approach
    def searchMatrixFlatten(self, matrix: List[List[int]], target: int) -> bool:
        flatten = list(chain.from_iterable(matrix))
        return self.b_search(flatten, 0, len(flatten) - 1, target)

    def b_search(self, nums, left, right, target):
        if right >= left:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.b_search(nums, left, mid - 1, target)
            else:
                return self.b_search(nums, mid + 1, right, target)
        else:
            return False
