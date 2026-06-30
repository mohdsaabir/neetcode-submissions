class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in nums:
            count=1
            while True:
                if i+1 in nums:
                    count+=1
                    i+=1
                else:
                    res=max(res,count)
                    break
        return res


        
                        



        