class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        pairs=[]
        for key in hashmap:
            pairs.append([key,hashmap[key]])
        
        n=len(pairs)

        for i in range(n):
            for j in range(n-i-1):
                if pairs[j][1]<pairs[j+1][1]:
                    pairs[j],pairs[j+1]=pairs[j+1],pairs[j]
        
        result=[]

        for i in range(k):
            result.append(pairs[i][0])
        
        return result
        
        