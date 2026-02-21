class Solution:
    
    

    def is_prime_number(self, num : int) -> bool:
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0 and i != num:
                return False

        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            bin_nb = bin(i)[2:]
            nb_bit_sets = bin_nb.count("1")
            if self.is_prime_number(nb_bit_sets):
                count += 1

        return count
    
