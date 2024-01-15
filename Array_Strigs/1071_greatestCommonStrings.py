class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 ==str2 +str1:
            

            return str1[:gcd(len(str1),len(str2))]
        else:
            return ''

# give program for findidng greatest common strings between tow given strings 
# 1071_greatestCommonStrings.py

