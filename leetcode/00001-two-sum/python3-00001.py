class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [map[target - nums[i]], i]
            else:
                map[nums[i]] = i