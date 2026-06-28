class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleared=""
        for char in s:
            if char.isalnum():
                cleared+=char.lower()
        
        low=0
        high=len(cleared)-1

        while low<=high:
            if cleared[low]==cleared[high]:
                low+=1
                high-=1
                continue
            else:
                return False
        return True