class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        negative = True
        for i in A:
            if i > 0:
                negative = False
        if negative:
            return max(A)
        
        total_sum = sum(A)
        max_dp = [0]*len(A)
        min_dp = [0]*len(A)
        max_dp[0] = A[0]
        min_dp[0] = A[0]
        maxsum = A[0]
        minsum = A[0]
        
        for i in range(1, len(A)):
            max_dp[i] = max(max_dp[i-1] + A[i], A[i])
            maxsum = max(max_dp[i], maxsum)
            min_dp[i] = min(min_dp[i-1] + A[i], A[i])
            minsum = min(minsum, min_dp[i])
         
        return max(maxsum, total_sum - minsum)