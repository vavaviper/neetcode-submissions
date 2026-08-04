class Solution:
    def climbStairs(self, n: int) -> int:
        #define dp[i]
        stairs = [0,1]
        #base case ^
        #build answer
        for i in range(1,n+1):
            stairs.append((stairs[-1] + stairs[-2]))
            print(i,stairs)
        #return answer
        return stairs[-1]
        
            