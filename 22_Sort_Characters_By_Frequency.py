class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        output = ''
        
        a = sorted(d.items(), key = lambda x: x[1], reverse = True)
        
        for i in range(len(a)):
            k, v = a[i][0], a[i][1]
            output += k*v
                
        return output