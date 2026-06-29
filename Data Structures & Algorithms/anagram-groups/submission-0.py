class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in myDict:
                myDict[s] = []
                myDict[s].append(strs[i])
            else:
                myDict[s].append(strs[i])
        return list(myDict.values())