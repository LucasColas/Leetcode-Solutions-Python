"""

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
From Leetcode : https://leetcode.com/problems/backspace-string-compare/

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(string):
            res = []
            for c in string:
                if c != '#':
                    res.append(c)
                elif c == '#' and len(res) > 0:
                    res.pop()
            return "".join(res)
        
        return check(s) == check(t)
        
