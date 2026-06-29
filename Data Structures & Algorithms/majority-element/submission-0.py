class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}

        for num in nums:
            if num not in myDict:
                myDict[num] = 0
            myDict[num] += 1

        i = 0
        j = 0
        for key, value in myDict.items():
            if i < value:
                j = key
                i = value

        return j