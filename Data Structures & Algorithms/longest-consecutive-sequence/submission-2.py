class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        res=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                count=1
                while True:
                    if i+1 in nums:
                        count+=1
                        i+=1
                    else:
                        res=max(count,res)
                        break
        return res
                        



        