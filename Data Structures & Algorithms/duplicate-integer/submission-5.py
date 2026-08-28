class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            numSet.add(num)

        # print(f"nums: {nums}")
        # print(f"numSet: {numSet}")
        return len(numSet) != len(nums)