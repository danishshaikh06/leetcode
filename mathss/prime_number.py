class Solution:
    def countprime(self, x):
        if x <= 2:
            return 0
        
        prime = [True] * x 
        prime[0] = prime[1] = False
        
        count = 0
        
        for i in range(2, x):
            if prime[i]:          
                count += 1
                for j in range(i * 2, x, i):
                    prime[j] = False
            
        
        return count


sol = Solution()
x = 50 
result = sol.countprime(x)
print(result)