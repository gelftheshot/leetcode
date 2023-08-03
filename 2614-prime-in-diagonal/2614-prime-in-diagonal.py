class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def isprime(n):
            if n == 2:
                return 1
            if n % 2 == 0 or n == 1:
                return 0
            m = 1
            for i in range(3,int(n**0.5)+1,2):
                if n % i == 0:
                    m = 0
            return m
                
            
        max_prime = 0
        for i in range(len(nums)):
                    if isprime(nums[i][i]) and nums[i][i] > max_prime:
                        max_prime = nums[i][i]
                    if nums[i][len(nums) - i - 1] > max_prime and isprime(nums[i][len(nums) - i - 1]):
                        max_prime = nums[i][len(nums) - i - 1]
        return max_prime
                    
                
                
                
                
                
                
                
                