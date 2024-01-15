class Solution:
    def productExceptSelf(self, nums):
        size=len(nums)
        if nums==[0]*size:
            return nums
        def product(arr):
            res=1
            for i in arr:
                if i!=0:
                    res*=i
            return res
        
        finalproduct=product(nums)


        if 0 in nums:
            count=0
            for i in range(size):
                if nums[i]==0:
                    count+=1
            if count<=1:
                for i in range(size):
                    if nums[i]!=0:
                        nums[i]=0
                    else:
                        nums[i]=finalproduct
            else:
                return [0]*size
            return nums


        
        for i in range(size):
            
            nums[i]=finalproduct//nums[i]
            
            
        return nums
