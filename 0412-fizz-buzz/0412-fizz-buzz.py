class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_r = []

        for i in range(1, n+1):
            
            if i % 5 == 0 and i % 3 == 0:
                list_r.append('FizzBuzz')
            elif i % 3 == 0:
                list_r.append("Fizz")
            elif i % 5 == 0:
                list_r.append("Buzz")
            else:
                list_r.append(str(i))
        return list_r