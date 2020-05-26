class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0
        d = {0: -1}
        count = 0
        
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in d:
                maxlen = max(maxlen, i - d[count])
            else:
                d[count] = i
        
        return maxlen