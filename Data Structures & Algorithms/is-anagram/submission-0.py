class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): 
            return False
        myDict = {}
        for c in s:
            if c in myDict:
                myDict[c] += 1
            else:
                myDict[c] = 1
        
        for c in t:
            if (myDict.get(c, 0) == 0):
                return False
            myDict[c] -= 1

        return True
        