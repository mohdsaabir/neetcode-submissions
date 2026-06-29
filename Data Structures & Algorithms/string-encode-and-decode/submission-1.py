class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in strs:
            encoded_string+=str(len(i))+'#'+i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        encoded_string=s
        while i<len(encoded_string):
            j=i
            while encoded_string[j] != '#':
                j+=1
            
            length=int(encoded_string[i:j])
            
            start_str=j+1
            end_str=start_str+length
            res.append(encoded_string[start_str:end_str])
            
            i=end_str
        return res
