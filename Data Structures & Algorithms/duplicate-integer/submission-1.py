class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if(dict.get(num, False) == False):
                dict[num] = 1
            else:
                return True
        return False
        