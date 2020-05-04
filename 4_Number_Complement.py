class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        result = 1
        
        while n != 0:
            num ^= result
            result = result << 1
            n = n >> 1
        
        return num