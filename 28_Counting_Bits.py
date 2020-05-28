class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num + 1)
        
        for i in range(1, num+1):
            n = i
            cnt = 0
            for _ in range(32):
                if n&1 == 1:
                    cnt += 1
                n = n>>1
            res[i] = cnt
        return res