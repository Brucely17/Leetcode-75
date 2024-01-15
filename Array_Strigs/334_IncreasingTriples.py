class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
            
        minim1=float("inf")
        minim2=float("inf")
        for i in nums:
            

            if i<=minim1:
                minim1=i
            elif i<=minim2:
                minim2=i
            else:
                return True
        return False
