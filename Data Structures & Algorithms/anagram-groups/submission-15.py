class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = dict()
        for string in strs:
            sortedS = "".join(sorted(string))
            if sortedS in sortedStrs:
                sortedStrs[sortedS].append(string)
            else:
                sortedStrs[sortedS] = [string]
        
        result = []
        for key in sortedStrs:
            result.append(sortedStrs[key])
        return result