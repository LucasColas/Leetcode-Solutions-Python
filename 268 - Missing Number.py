"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

From leetcode : https://leetcode.com/problems/missing-number/

"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n
