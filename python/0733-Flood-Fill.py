class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        orig_color = image[sr][sc]

        def dfs(r: int, c: int) -> None:
            image[r][c] = color
            directions = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            for dr, dc in directions:
                if (not (dr < 0 or dc < 0 or dr >= ROW or dc >= COL)
                and image[dr][dc] == orig_color):
                    dfs(dr, dc)
            
            return

        if orig_color == color:
            return image

        dfs(sr, sc)
        return image
