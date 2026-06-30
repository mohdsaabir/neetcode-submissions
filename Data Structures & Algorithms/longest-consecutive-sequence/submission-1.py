class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        res=0
        for i in nums:
            if i-1 in nums:
                continue
            else:
                start=i
                count=1
                while True:
                    if start+1 in nums:
                        count+=1
                        start+=1
                    else:
                        res=max(count,res)
                        break
        return res
                        



        