class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oricolor = image[sr][sc]
        # 针对要涂色的颜色和原颜色相同的情况
        if oricolor== newColor:
            return image
        def rc(r,c,oricolor,newcolor,im):
            w = len(im[0])
            h = len(im)
            im[r][c] = newcolor
            if r-1 >= 0 and im[r-1][c] == oricolor:
                rc(r-1,c,oricolor,newcolor,im)
            if r+1 <= h-1 and im[r+1][c] == oricolor:
                rc(r+1,c,oricolor,newcolor,im)
            if c-1 >= 0 and im[r][c-1] == oricolor:
                rc(r,c-1,oricolor,newcolor,im)
            if c+1 <= w-1 and im[r][c+1] == oricolor:
                rc(r,c+1,oricolor,newcolor,im)
            return
                                      
        rc(sr,sc,oricolor,newColor,image)
        return image
