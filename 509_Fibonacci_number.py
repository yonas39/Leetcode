class Solution:
    def fib(self, n: int) -> int:
        ######## Recursive solution ##########
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1)+ self.fib(n-2)
        
        ####### Iterative solution ##########
        total=0
        if n<2:
            total+=n
        #     return total
        prev_1=0
        prev_2=1
        for i in range(2,n+1):
            # total += (i-1)+(i-2)
            total = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = total


        return total
