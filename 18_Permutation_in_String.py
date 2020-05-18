class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        
        if n < m:
            return False
        
        sorted_s1 = sorted(s1)
        
        for i in range(n-m+1):
            temp = sorted(s2[i:i+m])
            if temp == sorted_s1:
                return True
        
        return False