"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

From Leetcode : https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        while n > 0:
            if n%2 == 1:
                count += 1
                
            n = n//2
            
        return count
        
