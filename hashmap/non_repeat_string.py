'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.'''


def unique(s):
    
    freq = {}

    for ch in s:
      freq[ch] =freq.get(ch,0) + 1

    for i, ch in enumerate(freq):
      if freq[ch] == 1:
        return (i,ch)

    return -1

unique('leetcode')



