# Question : Longest Substring Without Repeating Characters -> leetcode 3
#example -> abcabcbb , output -> 3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        seen = {}
        max_len = 0 
        l = 0 

        for i ,r in enumerate(s):
            if r in seen and seen[r]>=l :
                l = seen[r] + 1
            seen[r] = i
            sub = s[l:i+1]
            max_len = max(max_len, i-l+1)
        
        return max_len, sub