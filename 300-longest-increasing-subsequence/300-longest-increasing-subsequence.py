import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        for i in range(len(nums)):
            idx=bisect.bisect_left(dp,nums[i])
            if idx==len(dp): dp.append(nums[i])
            else: dp[idx]=nums[i]
        return len(dp)
        