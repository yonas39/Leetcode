class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ############ O(n) time compxty and O(n) space complx #####
        # min_=[0]*len(cost)
        # min_[0],min_[1] = cost[0], cost[1]
        # for i in range(2, len(cost)):
        #     min_[i]= min(min_[i-1],min_[i-2]) + cost[i]
        # return min(min_[len(cost)-1],min_[len(cost)-2])

        ########## better space complexity #############

        p_1, p_2 = cost[0], cost[1]
        for i in range(2,len(cost)):
            curr = min(p_1,p_2) + cost[i]
            p_1, p_2 = p_2, curr
        return min(p_1, p_2)
      
      
      
      
      
      
      
      
