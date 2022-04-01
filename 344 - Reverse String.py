
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
Problem : https://leetcode.com/problems/reverse-string/
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(s)-1
        for i in range(len(s)//2):
            s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
            ptr1 += 1
            ptr2 -= 1
        
        
