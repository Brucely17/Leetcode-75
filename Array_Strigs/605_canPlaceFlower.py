class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=n
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                if n<=1:
                    return True
                else:
                    return False
            else:
                return False

        

        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i==0:
                    if flowerbed[i+1]==0:
                        count-=1
                        flowerbed[i]=1
                elif i==len(flowerbed)-1:
                    if flowerbed[i-1]==0:
                        count-=1
                        flowerbed[i]=1
                else:
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                        count-=1
                        flowerbed[i]=1
        if count<=0:
            return True
        else:
            return False
