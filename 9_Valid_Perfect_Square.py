class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq = 1
        
        while sq*sq <= num:
            if sq*sq == num:
                return True
            sq += 1
            
        return False