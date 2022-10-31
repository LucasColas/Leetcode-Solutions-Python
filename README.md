# Leetcode-Solutions-Python


| Problem  | Topics Covered | solution (idea) |
| ------------- | ------------- | ------------- | 
| 344 - Reverse String | string, 2 pointers | [Use 2 pointers and swap the values.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/344%20-%20Reverse%20String.py) |
| 1721 - Swapping Nodes in a Linked List | 2 pointers | [Use 3 pointers. Find kth node from right using pointer that points to the kth node from left and use a pointer which points to the head. Iterate until tail.next == None.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/1721%20-%20Swapping%20Nodes%20in%20a%20Linked%20List.py) |
| 703 - Kth Largest Element in a Stream | heap, loop | [Convert list to heap, delete every largest element to get an heap of length k. Every time we add values, we delete the larget element and return the smallest element.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/703%20-%20Kth%20Largest%20Element%20in%20a%20Stream.py) |
| 682 - Baseball Game | array | [Iterate through ops, check different cases. Return the sum of all the scores.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/682%20-%20Baseball%20Game.py) | 
| 100 - Same Tree | Tree | [Check if the two values are the same or not.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/100%20-%20Same%20Tree.py) |
| 705 - Design HashSet | HashSet, Set | [Use set ; add, discard and search elements in the set.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/705%20-%20Design%20HashSet.py) |
| 706 - Design HashMap | array, index | [Use an array, the key serves as an index in the array.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/706%20-%20Design%20HashMap.py) | 
| 844 - Backspace String Compare | string, array, join | [Append to a list every char different from #, use join to build the new string.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/844%20-%20Backspace%20string%20compare.py) |
| 1679 - Max Number of K-Sum Pairs | Two pointers | [Sort the array.Two pointers. One starts from very begining & another from the end of the array.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/1679%20-%20Max%20Number%20of%20K-Sum%20Pairs.py) |
| 191 - Number of 1 Bits | loop | [Iterate until n = 0. Divide by 2 and use modulo 2.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/191%20-%20Number%20of%201%20Bits.py) |
| 703 - Kth Largest Element in a Stream | Heap | [Use heap. Pop until the length of the heap is equal to k.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/703%20-%20Kth%20Largest%20Element%20in%20a%20Stream.py) |
| 318 - Maximum Product of Word Lengths | string, loop | [Compare each string with every other string of the list.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/318%20-%20Maximum%20Product%20of%20Word%20Lengths.py) |
| 1480 - Running Sum of 1d Array | for loop | [To alculate the i-th number : i-th value of nums + i-1-th value.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/1480%20-%20Running%20Sum%20of%201d%20Array.py) |
| 867 - Transpose Matrix | loop, array | [New 2D array to contain the transpose of a Matrix. new_matrix(j)(i) = matrix(i)(j).](https://leetcode.com/problems/transpose-matrix/) |
| 167 - Two Sum II - Input array is sorted | Two pointers | [Pointer1 starts at 0, Pointer2 starts at the end of the array. If the sum is greater than target, we move Pointer2 to the left, otherwise we move Pointer1 to the right until the sum is equal to target.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/167%20-%20Two%20Sum%20II%20-%20Input%20Array%20is%20sorted.py) |
| 1662 - Check If Two String Arrays are Equivalent | strings | [Use join to concatenate every string of an array.](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/1662%20-%20Check%20If%20Two%20String%20Arrays%20are%20Equivalent) |
| 766 - Toeplitz Matrix | Array | [Iterate through the 2D array. Check if matrix[i-1][j-1] != matrix[i][j].](https://github.com/LucasColas/Leetcode-Solutions-Python/blob/main/766%20-%20Toeplitz%20Matrix) |
