from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.b_search(nums, 0, len(nums)-1, target)

    def b_search(self, nums, left, right, target):
        if right >= left:
            mid = int((right + left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.b_search(nums, left, mid-1, target)
            else:
                return self.b_search(nums, mid+1, right, target)
        else:
            return -1