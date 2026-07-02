class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low<high:
            currSum=numbers[low]+numbers[high]
            if currSum<target:
                low+=1
            elif currSum>target:
                high-=1
            elif currSum==target:
                return [low+1,high+1]
        return []