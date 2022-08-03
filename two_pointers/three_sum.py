from typing import List


# class Solution:
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for index, num in enumerate(nums):
        if index > 0 and num == nums[index-1]:
            continue
        i, j = index+1, len(nums)-1
        while i < j:
            if nums[index] + nums[i] + nums[j] == 0:
                result.append([nums[index], nums[i], nums[j]])
                i += 1
                while nums[i] == nums[i-1] and i < j:
                    i += 1
            elif nums[index] + nums[i] + nums[j] > 0:
                j -= 1
            else:
                i += 1
    return result