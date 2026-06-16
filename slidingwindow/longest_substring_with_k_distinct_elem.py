# Given a string, find the length of the longest substring T that contains at most k distinct characters.-> leetcode 340
s = 'aaabbcdd'
seen = {}
k = 2
l = 0 
max_len = 0 

for r in range(len(s)):
    seen[s[r]] = seen.get(s[r], 0) + 1

    if len(seen) > k:
      seen[s[l]]-= 1
      if seen[s[l]] == 0:
          del seen[s[l]]
      l+=1

    if len(seen) <= k:
      max_len = max(max_len, r - l + 1)


print(max_len)