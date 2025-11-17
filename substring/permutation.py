'''567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # Frequency arrays for s1 and the sliding window in s2
        freq1 = [0] * 26
        freq2 = [0] * 26

        # Count frequency of each character in s1
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1 # ord converts char to asci codes

        # Initialize the first window in s2
        for i in range(n):
            freq2[ord(s2[i]) - ord('a')] += 1

        # Check if the first window is already a permutation
        if freq1 == freq2:
            return True

        # Slide the window across s2
        for i in range(n, m):
            # Add new character entering the window
            freq2[ord(s2[i]) - ord('a')] += 1

            # Remove the old character leaving the window
            freq2[ord(s2[i - n]) - ord('a')] -= 1

            # Check if the updated window matches s1's frequency
            if freq1 == freq2:
                return True

        return False



"""
==========================
 COMPLETE LOGIC EXPLANATION
==========================

Goal:
-----
Check if s1's permutation (anagram) appears as a substring inside s2.
Example:
  s1 = "ab"
  s2 = "eidbaooo"
  "ba" appears in s2 → True


Why We Use Frequency Arrays:
----------------------------
A permutation of s1 has exactly the same character counts as s1.
We store:
  freq1 = counts of letters in s1
  freq2 = counts of letters in a sliding window of s2 (same length as s1)

If freq1 == freq2 → This window is a permutation.


Step 1 — Count Characters in s1:
--------------------------------
We build freq1, a 26-element array (one entry per lowercase letter).


Step 2 — Build the First Window of s2:
--------------------------------------
We create the first window of length n = len(s1) inside s2.

Example:
  s1 = "ab"  → window size = 2
  s2 = "eidbaooo"

First window = "ei"
We count its characters into freq2.


Step 3 — Compare First Window:
------------------------------
If freq1 == freq2 → we found a permutation inside s2.


Step 4 — Sliding Window Logic:
-------------------------------
We slide the window from left to right by 1 character.

For each step:
  Window moves from old to new:
  
    [old window]      →      [new window]
    "ei"              →      "id"
     ^ removed char          ^ added char

Every move has 2 operations:

(1) Add the character entering the window:
    freq2[ord(new_char) - ord('a')] += 1

(2) Remove the character leaving the window:
    freq2[ord(old_char) - ord('a')] -= 1

The old char is at index (i - n).


Why i - n?
----------
When i points to the new character entering the window,
the character leaving is exactly n positions behind.

Example:
  n = 2
  i = 3
  New char = s2[3]
  Old char = s2[3 - 2] = s2[1]

This keeps freq2 always representing EXACTLY the current window.


Step 5 — After Each Slide, Compare Again:
-----------------------------------------
If freq1 == freq2 at any point → found a permutation → return True.


Time Complexity:
----------------
O(m), where m = len(s2)
We only scan s2 once.

Space Complexity:
-----------------
O(1), because both arrays have fixed size = 26.


Result:
-------
This is the optimal solution both in time and memory.
"""
