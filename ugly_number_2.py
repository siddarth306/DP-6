# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Keep multiplying the 2,3,5 with the past values in the ugly number sequence and always take the minimum from it.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        multiplier = [0]*3
        factors = [2,3,5]
        
        nextVal = 9999999999
        idx = -1
        past_values = [1]
        for _ in range(n-1):
            nextVal = 9999999999
            idx = []
            nextVal = min([past_values[multiplier[i]]*factors[i] for i in range(3) if past_values[multiplier[i]]*factors[i]  not in past_values])
        
            for i in range(3):
                possibleVal = past_values[multiplier[i]]*factors[i]
                if nextVal == possibleVal:
                    idx.append(i)
                    
            for i in idx:
                multiplier[i] += 1
            past_values.append(nextVal)

        return nextVal
        