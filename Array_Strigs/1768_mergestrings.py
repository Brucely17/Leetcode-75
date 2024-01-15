class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        self.result=""
        self.minim=min(len(word1),len(word2))
        self.maxim=''
        if len(word1)>len(word2):
            self.maxim+= word1
        else:
            self.maxim+= word2
        for i in range(self.minim):
            self.result+=word1[i]+word2[i]
        if len(word1)==len(word2):
       
            return self.result
        else:
            self.result+=self.maxim[self.minim:]
            return self.result