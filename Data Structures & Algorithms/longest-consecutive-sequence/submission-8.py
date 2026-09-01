class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        sortedLs = sorted(nums)
        highest = 0
        current = sortedLs[0]
        currentConsecutive = 0
        # print(sortedLs)

        for i in range(len(nums)):
            val = sortedLs[i]
            # print(f"Current: {current} | Val: {val}")
            if current == val:
                if (currentConsecutive == 0):
                    currentConsecutive = 1
                continue
            elif val < (current + 2):
                currentConsecutive += 1
                current = val
            else:
                # print("reset")
                highest = max(currentConsecutive, highest)
                currentConsecutive = 1
                current = val

        highest = max(currentConsecutive, highest)

        return highest

