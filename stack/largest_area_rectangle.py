class Solution(object):

        def largestRectangleArea(self,arr):
            stack = []
            max_area = 0

            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    element = arr[stack.pop()]
                    nse = i

                    if stack: # if len(stack) > 0:
                        pse = stack[-1]
                    else:
                        pse = -1

                    width = nse - pse - 1
                    max_area = max(max_area, element * width)

                stack.append(i)

            while stack:
                element = arr[stack.pop()]
                nse = len(arr)

                if stack: # if len(stack) > 0:
                    pse = stack[-1]
                else:
                    pse = -1

                width = nse - pse - 1
                max_area = max(max_area, element * width)

            return max_area


    