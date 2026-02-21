class Solution:
    
    prime_numbers = {1:False}

    def is_prime_number(self, num : int) -> bool:
        if num in self.prime_numbers:
            return Solution.prime_numbers[num]
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0 and i != num:
                Solution.prime_numbers[num] = False
                return False

        Solution.prime_numbers[num] = True
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            bin_nb = bin(i)[2:]
            nb_bit_sets = bin_nb.count("1")
            if self.is_prime_number(nb_bit_sets):
                count += 1

        return count
    
