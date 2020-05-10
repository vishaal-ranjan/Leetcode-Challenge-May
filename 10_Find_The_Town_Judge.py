class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return N
        judge = -1
        d1 = {}
        d2 = {}
        
        for i in range(len(trust)):
            if trust[i][1] in d1:
                d1[trust[i][1]] += 1
            else:
                d1[trust[i][1]] = 1
            if trust[i][0] not in d2:
                d2[trust[i][0]] = 1
             
        for i in d1:
            if d1[i] == N-1:
                judge = i
        
        return judge if judge not in d2 else -1