class Solution:
    def reverse(self, s : str):
        return s[::-1]
    def invert(self, s : str):
        s_ = ""
        for c in s:
            if c == "1":
                s_ += "0"
            else:
                s_ += "1"

        return s_
    
    def create_string(self, n: int):
        if n == 1:
            return "0"

        str_ = self.create_string(n-1)
        return str_ + "1" + self.reverse(self.invert(str_))

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        return self.create_string(n)[k-1]
