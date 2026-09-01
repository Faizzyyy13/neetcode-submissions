class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        l=0
        r=len(heights)-1
        while l<r:
            short=min(heights[l],heights[r])
            res=(r-l)*(short)
            if res>area:
                area=res
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return area
            
            