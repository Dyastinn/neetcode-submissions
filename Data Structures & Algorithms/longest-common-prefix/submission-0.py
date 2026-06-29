class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestWord = min(strs, key=len)
        for i, ch in enumerate(shortestWord):
            for str in strs:
                print(ch)
                if ch != str[i]:
                    return shortestWord[0:i:]

        return shortestWord
