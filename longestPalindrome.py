# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Approach: Create a 2D dp array. Make the left-right diagonal elements as True. Fill the upper right half of the triangle.
#			The dp operation will be if first and last character match, dp[i][j] = dp[i+1][j-1]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        
        dp = [[False]* len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            
        result = 1
        result_str = s[0]
        for i in range(1,len(s)):
            for j in range(len(s)-i):
                if i+j < len(s):
                    #print(s[j],s[i+j])
                    if s[j] == s[i+j] and (dp[j+1][i+j-1] or  i == 1):
                        dp[j][i+j] = True
                        result = i+1
                        result_str = s[j:i+j+1]
                        
        #print(dp)
        return result_str