# class Solution:
from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums)-1

    result = nums[left]
    while left <= right:
        if nums[right] > nums[left]:
            result = min(result, nums[left])
            break
        mid = (left + right) // 2
        result = min(result, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))