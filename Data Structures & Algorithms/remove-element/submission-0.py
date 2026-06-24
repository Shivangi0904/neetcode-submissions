class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       k = 0
       tmp = []
       for num in nums:
        if num == val:
            continue
       for i in range (len(nums)):
            if nums[i] != val:
                k +=1
    
    