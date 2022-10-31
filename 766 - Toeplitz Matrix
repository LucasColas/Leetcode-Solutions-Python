"""

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
Toeplitz Matrix : https://leetcode.com/problems/toeplitz-matrix/

"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if (matrix[i-1][j-1] != matrix[i][j]):
                    return False
        return True
        
