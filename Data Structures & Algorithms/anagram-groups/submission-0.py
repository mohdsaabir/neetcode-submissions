class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output=[]
        hashmap={}
        for val in strs:
            k = "".join(sorted(val))
            if k in hashmap:
                hashmap[k].append(val)
            else:
                hashmap[k]=[val]
        for i in hashmap.values():
            final_output.append(i)
        return final_output




        