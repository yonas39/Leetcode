class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ######### Iterative Solution ###############
        # if not grid:
        #     return 0

        # agenda = []
        # count = 0

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]=='1':
        #             agenda.append((i,j))
        #             count += 1
        #             grid[i][j] = "0"   

        #             while agenda:
        #                 row, col = agenda.pop()
        #                 if row > 0 and grid[row-1][col] == "1":
        #                     agenda.append((row-1,col))
        #                     grid[row-1][col]="0"
        #                 if col > 0 and grid[row][col-1] == "1":
        #                     agenda.append((row,col-1))
        #                     grid[row][col-1]="0"
        #                 if row < len(grid)-1 and grid[row+1][col] == "1":
        #                     agenda.append((row+1,col))
        #                     grid[row+1][col]="0"
        #                 if col<len(grid[0])-1 and grid[row][col+1] == "1":
        #                     agenda.append((row,col+1))
        #                     grid[row][col+1]="0"
        # return count

        ############ Recursive Solution ###################
        def DFS(grid,row, col):
            if row < 0 or col < 0 or row >len(grid)-1 or col >len(grid[0])-1 or grid[row][col]=="0":
                return 
            grid[row][col]="0"
            DFS(grid,row-1,col)
            DFS(grid,row+1,col)
            DFS(grid,row,col-1)
            DFS(grid,row,col+1)

        count=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    count+=1
                    DFS(grid,r,c)
        return count

