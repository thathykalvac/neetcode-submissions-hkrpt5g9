class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for n in range(len(nums)):
            if target-nums[n] not in d:
                d[nums[n]]=n
            else:
                return [d[target-nums[n]],n]
