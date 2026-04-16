class Solution:
    def binarySearch(self, array, element):
        low = 0
        high = len(array) - 1

        while low <= high:
            
            mid = (low + high) // 2
            
            if array[mid] == element:
                return mid

            elif array[mid] < element:
                low = mid + 1
                
            else:
                high = mid - 1

        return -1
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        answer  = []
        numbers = {}
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = []

            numbers[nums[i]].append(i)
        n =len(nums)
        for q_idx in queries:
            target_val = nums[q_idx]
            indices = numbers[target_val]
        
            if len(indices) <= 1:
                answer.append(-1)
                continue

            pos = self.binarySearch(indices, q_idx)
            
            prev_idx = indices[(pos - 1) % len(indices)]

            next_idx = indices[(pos + 1) % len(indices)]
            
            def get_circ_dist(i, j, n):
                diff = abs(i - j)
                return min(diff, n - diff)
            
            dist1 = get_circ_dist(q_idx, prev_idx, n)
            dist2 = get_circ_dist(q_idx, next_idx, n)
            
            answer.append(min(dist1, dist2))

        return answer

