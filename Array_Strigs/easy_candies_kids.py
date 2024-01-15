class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        self.res=[False]*len(candies)
        
        for i in range(len(candies)):
            temp=candies[i]+extraCandies
            if i==0:
                if temp>=max(candies[i+1:]):
                    self.res[i]=True
                   
            elif i==len(candies)-1:
                if temp>=max(candies[:i]):
                 
                    self.res[i]=True
            if temp>=max(candies[:i]+candies[i+1:]):
              
                self.res[i]=True

           
        return self.res
