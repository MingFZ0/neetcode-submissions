class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        allNums = set()
        record = 0

        for num in nums:
            allNums.add(num)

        for num in allNums:
            if (num-1) not in allNums:
                # print(f"{num} ->")
                cur = num
                highest = 0

                while (cur) in allNums:
                    # print(f"     {cur}")
                    cur += 1
                    highest += 1

                record = max(highest, record)
        

        return record

