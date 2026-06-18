class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       n = len(nums)
       x = 0
       for i in range(n):
        cnt = 0
        for j in range(i, n):
            if nums[j] == 0: break
            cnt += 1
        x = max(x,cnt)

       return x