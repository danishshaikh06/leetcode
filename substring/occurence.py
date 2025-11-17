'''Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"'''

class Solution:
    def occurrence(self, s: str, part: str) -> str:
        index = s.find(part)
        while index!= -1:
            s = s[:index] + s[index + len(part) : ]
            index = s.find(part)
        return s

            
        

sol = Solution()
s = "daabcbaabcbc"
part = "abc"
result = sol.occurrence(s, part)
print(result)