class Solution:
    def reverseWords(self, s: str) -> str:
        
        res=s.split(" ")
        res=res[::-1]
        string=''
        for i in res:
            if i!="":
                string+=i+" "
        return string.strip()





        