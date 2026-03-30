# problem number 84 

'''# 📌 Largest Rectangle in Histogram

# 🧠 Problem Statement:
# Given an array of integers 'heights' representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle
# in the histogram.

# ------------------------------------------------------------
# 📊 Example:
# Input: heights = [2, 1, 5, 6, 2, 3]
# Output: 10

# Explanation:
# The largest rectangle is formed using heights[2] = 5 and heights[3] = 6
# Width = 2 → Area = 5 * 2 = 10

# ------------------------------------------------------------
# 🔍 Dry Run:
# heights = [2, 1, 5, 6, 2, 3]

# Step-by-step using stack:
# We maintain a stack of indices with increasing heights.

# i=0 → push(0) → stack = [0]
# i=1 → height[1] < height[0]
#        pop(0), area = 2 * 1 = 2
#        push(1)
#        stack = [1]

# i=2 → push(2) → stack = [1,2]
# i=3 → push(3) → stack = [1,2,3]

# i=4 → height[4] < height[3]
#        pop(3), area = 6 * 1 = 6
#        pop(2), area = 5 * 2 = 10  ← max area
#        push(4)
#        stack = [1,4]

# i=5 → push(5) → stack = [1,4,5]

# End → process remaining stack:
# pop(5) → area = 3 * 1 = 3
# pop(4) → area = 2 * 4 = 8
# pop(1) → area = 1 * 6 = 6

# Maximum Area = 10

# ------------------------------------------------------------
# 💡 Approach (Monotonic Stack):
# - Use a stack to store indices
# - Ensure heights are in increasing order
# - When a smaller bar appears, calculate area'''


class Area:

    def right_smaller_element(self, heights):
        stack = []
        n = len(heights)
        right = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1]

            stack.append(i)

        return right


    def left_smaller_element(self, heights):
        stack = []
        n = len(heights)
        left = [0] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]

            stack.append(i)

        return left


    def largestRectangleArea(self, heights):
        left = self.left_smaller_element(heights)
        right = self.right_smaller_element(heights)

        max_area = 0

        for i in range(len(heights)):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area

if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    obj = Area()
    print(obj.largestRectangleArea(heights)) 
