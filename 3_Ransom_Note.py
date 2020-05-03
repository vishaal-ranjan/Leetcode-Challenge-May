class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}
        
        for i in magazine:
            d1[i] = d1.get(i,0) + 1
        
        for i in ransomNote:
            d2[i] = d2.get(i,0) + 1
        
        for key in d2:
            print(key)
            if key not in d1 or d2[key] > d1[key]:
                return False
            
        return True