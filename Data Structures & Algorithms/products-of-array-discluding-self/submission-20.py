class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = None
        zeros = 0
        for num in nums:
            if (num == 0):
                zeros += 1
            else:
                if (total is None):
                    total = num
                else:
                    total *= num
        print(total)
        
        result = [0] * len(nums)
        if total == None or zeros > 1:
            return result

        
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = total
            else:
                if (zeros >= 1):
                    result[i] = 0
                else:
                    result[i] = total // nums[i]
        return result