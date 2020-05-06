class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        target = len(nums)//2
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] > target:
                    return i