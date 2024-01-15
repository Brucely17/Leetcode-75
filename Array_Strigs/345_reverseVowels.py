class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        left=0
        right=len(l)-1
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        while left <right:
            if l[left] in vowels and l[right] in vowels :
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
            elif l[left] in vowels:
                right-=1
            else:
                left+=1
        return ''.join(l)
            