def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charsToLastIndex = {}
        longest = 0
        for end in range(len(s)):
            if s[end] in charsToLastIndex and charsToLastIndex[s[end]] >= start:
                start = charsToLastIndex[s[end]] + 1
            charsToLastIndex[s[end]] = end
            longest = max(longest,end-start+1)
        return longest