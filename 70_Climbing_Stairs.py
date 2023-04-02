class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        # memo={}
        if n<=2:
            return n
        if n in memo:
            return memo[n]
        else:
            output = self.climbStairs(n-1, memo) + self.climbStairs(n-2,memo)
            memo[n]= output
            return output


        ########### Iterative ###################
        # if n<=2:
        #     return n
        # prev_1=1
        # prev_2=2
        # total=0
        # for i in range(3,n+1):
        #     total=prev_1 + prev_2
        #     prev_1 = prev_2
        #     prev_2 = total
        # return total
