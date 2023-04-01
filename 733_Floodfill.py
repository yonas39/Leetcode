class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        In this implementation, I use agenda to keep track of the pixels to be filled. I started with the given starting pixel, push it onto the agenda, 
        and then continue looping until the agenda is empty. During each iteration of the loop, we pop a pixel from the agenda and check if it has the 
        original color. If it does, I change its color to the new color and add its adjacent pixels (up, down, left, right) to the agenda, if they have 
        the original color. This process continues until all pixels with the original color have been visited and colored with the new color. Finally, 
        I return the filled image array.
        
          Note: that the iterative approach can be more efficient than the recursive approach, as it avoids the overhead of function calls and recursion 
          stack.
        """
        ############## Iterative method #################
        # if image[sr][sc] == color:
        #     return image

        # original_color = image[sr][sc]
        # agenda = [(sr,sc)]
        # # visited = set()
        # while agenda:
        #     r,c = agenda.pop()
        #     if image[r][c] == original_color:
        #         image[r][c] = color
        #         if r>0:
        #             agenda.append((r-1,c))
        #         if r<len(image)-1:
        #             agenda.append((r+1,c))
        #         if c>0:
        #             agenda.append((r,c-1))
        #         if c<len(image[0])-1:
        #             agenda.append((r,c+1))
        # return image

        ################ recursive method ############
        org_color = image[sr][sc]
        if org_color == color:
            return image
        
        def  flooded(image, r, c, org_color, color):
            if r< 0 or r>=len(image) or c<0 or c>=len(image[0]):
                return 
            if image[r][c]!=org_color:
                return 

            image[r][c]=color
            flooded(image, r-1,c,org_color,color)
            flooded(image, r+1,c,org_color,color)
            flooded(image, r,c-1,org_color,color)
            flooded(image, r,c+1,org_color,color)
     
        flooded(image, sr, sc, org_color, color)
        return image

