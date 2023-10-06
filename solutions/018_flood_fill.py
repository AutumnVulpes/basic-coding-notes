# https://leetcode.com/problems/flood-fill/description/

# Edge Case: If color is same as starting point, return current image (eg 2)
# Remember to store start color since it will change
# But other tiles only change if they match starting color
# Depth first search(?), start then just go all the way out in cardinals until stop
# Repeat et al?
# Additional recursive fn
# Edge Case: Border of image

# Solution 1: Iterative DFS
# Better than recursive due to max recusrion limit and less space used on python call stack
class Solution:
    def within_bounds(self, target, min, max):
        return target >= min and target <= max

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        
        hori_bound = len(image) - 1
        vert_bound = len(image[0]) - 1

        stack = [(sr, sc)]
        while stack:
            (r, c) = stack.pop()
            image[r][c] = color
            for (row, col) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (not self.within_bounds(row, 0, hori_bound)
                    or not self.within_bounds(col, 0, vert_bound)):
                    continue
                if image[row][col] == start_color:
                    stack.append((row, col))
        return image


# Solution 2: Recursive DBS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        
        hori = len(image)
        vert = len(image[0])
        
        # New recursive function
        # Set target spot to new color, look at adjacents
        # If in bounds and same as saved starting color, repeat
        
        def splash(r, c):
            image[r][c] = color
            for (row, col) in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= row < hori and 0 <= col < vert and image[row][col] == start_color:
                    splash(row, col)

        splash(sr, sc)
        return image
