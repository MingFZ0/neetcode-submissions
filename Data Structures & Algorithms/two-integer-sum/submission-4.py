class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = dict()
        numSet[nums[0]] = 0

        for i in range(1, len(nums)):
            diff = target - nums[i]
            if (diff in numSet):
                return [numSet[diff], i]
            numSet[nums[i]] = i