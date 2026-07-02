class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=-1
        low=0
        high=len(heights)-1
        while low<high:
            area=min(heights[low],heights[high])*(high-low)
            ans=max(ans,area)
            if heights[low]<=heights[high]:
                low+=1
            else:
                high-=1
        return ans
        