class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []
        sol = []
        
        p_count = collections.Counter(p)
        s_count = collections.Counter()
        
        for i in range(m):
            s_count[s[i]] += 1
            if i >= n:
                if s_count[s[i-n]] == 1:
                    del s_count[s[i-n]]
                else:
                    s_count[s[i-n]] -= 1
                
            if p_count == s_count:
                sol.append(i-n+1)
        
        return sol