class Solution:
    def twoSum(self, nums, target):
        numtoindex = {}
        for i in range(len(nums)):
            if target - nums[i] in numtoindex:
                return [numtoindex[target - nums[i]], i]
            numtoindex[nums[i]] = i  
