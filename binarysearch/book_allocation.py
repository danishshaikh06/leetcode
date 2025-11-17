'''Book Allocation Problem
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.

Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.

Examples:
Input: nums = [12, 34, 67, 90], m=2
Output: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.'''

from typing import List

class Solution:
    @staticmethod
    def number_students(arr: List[int], pages: int,):
        student = 1
        num_pages = 0 
        for i in range (len(arr)):
            if (num_pages + arr[i] <= pages):
                num_pages += arr[i]
            else:
                student+=1
                num_pages = arr[i]

        return student
    
    def book_allocation(self, m: int, nums: List[int]):
        low = max(nums)
        high = sum(nums)
        while (low <= high):
            mid = (low + high) // 2
            max_student = Solution.number_students(nums, mid)
            if (max_student > m):
                low = mid + 1
            else: 
                high = mid -1
        return low
    
sol = Solution()
nums = [12, 34, 67, 90]
m = 2
result = sol.book_allocation(m,nums)
print(result)


    
