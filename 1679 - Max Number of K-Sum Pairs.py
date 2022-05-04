"""

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

From Leetcode : https://leetcode.com/problems/max-number-of-k-sum-pairs/

"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        op,i = 0, 0
        j = len(nums)-1
        
        while i < j:
            sum = nums[i]+nums[j]
            if sum == k:
                i += 1
                j -= 1
                op += 1
            
            elif sum > k:
                j -= 1
            
            else:
                i += 1
        
                
        return op
                        
        
