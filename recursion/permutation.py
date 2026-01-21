'''arr = [1, 2, 3]

idx = 0

Loop execution:

🔹 Iteration 1: i = 0

arr[0], arr[0] = arr[0], arr[0]

Array:

[1, 2, 3]

Meaning:

“Place 1 at position 0”

Then recurse to fix next position.

🔹 Iteration 2: i = 1

arr[0], arr[1] = arr[1], arr[0]

Array:

[2, 1, 3]

Meaning:

“Place 2 at position 0”

Then recurse.

🔹 Iteration 3: i = 2

arr[0], arr[2] = arr[2], arr[0]

Array:

[3, 2, 1]

Meaning:

“Place 3 at position 0”

Then recurse.

Why do we swap back?

arr[idx], arr[i] = arr[i], arr[idx]   # backtrack

Reason:

After recursion finishes, we must:

Undo the choice

Restore the array for the next iteration

Without backtracking:

The next i would start with a corrupted array

Permutations would be wrong'''


class Solution(object):
    def perms(self, arr, idx, ans):
        if idx == len(arr):
            ans.append(arr[:])
            return

        for i in range(idx, len(arr)):
            # choose
            arr[idx], arr[i] = arr[i], arr[idx]

            # explore
            self.perms(arr, idx + 1, ans)

            # backtrack
            arr[idx], arr[i] = arr[i], arr[idx]

    def permute(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.perms(arr, 0, ans)
        return ans