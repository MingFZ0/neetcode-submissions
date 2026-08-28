class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict()
        for num in nums:
            numsDict.setdefault(num, 0)
            numsDict[num] += 1
        
        frequency = []
        for num in numsDict:
            frequency.append((numsDict[num], num))
        frequency.sort()
        
        result = []
        index = len(frequency) -1
        for _ in range(k):
            result.append(frequency[index][1])
            index -= 1
        return result