'''Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.'''

class Solution:
    def longsubString(self, s: str) -> str:
        longest = ""

        n = len(s)

        for i in range(n):
            l, r = i, i  # odd-length palindrome
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
                '''Example: For "ababd" with i=1 (center "b"):

                    l=1, r=1 → "b"   (palindrome)
                    l=0, r=2 → "aba" (palindrome, longest so far)
                    l=-1, r=3 → stop (out of bounds)'''

            l, r = i, i + 1  # even-length palindrome
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1

        return longest


# Example
sol = Solution()
s = "ababd"
print(sol.longsubString(s))  # Output: "bab" or "aba"

        




