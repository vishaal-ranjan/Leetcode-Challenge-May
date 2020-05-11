class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, newColor, original):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != original:
                return 0
            image[sr][sc] = newColor
            dfs(image, sr-1, sc, newColor, original)
            dfs(image, sr+1, sc, newColor, original)
            dfs(image, sr, sc-1, newColor, original)
            dfs(image, sr, sc+1, newColor, original)
        
        original = image[sr][sc]
        if original == newColor:
            return image
        dfs(image, sr, sc, newColor, original)
        return image