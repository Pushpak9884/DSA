class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            value=target-num
            if value in seen:
                return [seen[value],i]
            seen[num]=i
             