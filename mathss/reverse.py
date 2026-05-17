class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        INT_MAX = 2**31 - 1 
        INT_MIN = -2**31
        reversed_num = 0
        while x > 0:
            dig = x % 10
            x = x // 10

            if reversed_num > (INT_MAX - dig) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + dig
            
        reversed_num *= sign
        return reversed_num
