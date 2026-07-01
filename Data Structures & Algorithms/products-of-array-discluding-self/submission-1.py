class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero_count=0

        for i in nums:
            if i==0:
                zero_count+=1
            else:
                product*=i

        result=[]
        for i in nums:
            if zero_count>1:
                result.append(0)
            elif zero_count==1:
                if i==0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product//i)
        return result


        

        


        