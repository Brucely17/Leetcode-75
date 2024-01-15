class Solution:
    def compress(self, chars: List[str]) -> int:
        # chars=sorted(chars)
        count=1
        totalcount=0
        tcount=[]
        index=0
        for i in range(len(chars)-1):
            if chars[i] ==chars[i+1]:
                count+=1
            elif chars[i]!=chars[i+1]:
                print(chars[i],count)
                totalcount+=count
                chars[index]=chars[i]
                index+=1
                tcount.append(chars[i])
                if count>1:
                    if count>=10:
                                a=str(count)
                                print(a)
                                for i in range(len(a)):
                                    print(a[i])
                                    chars[index]=a[i]
                                    index+=1
                                    tcount.append(a[i])
                                count=1
                    else:

                        chars[index]=str(count)
                        index+=1
                        tcount.append(str(count))
                        count=1
        chars[index]=chars[-1]
        index+=1
        tcount.append(chars[-1])
        count=len(chars)-totalcount
        if count>1:
                    if count>=10:
                                a=str(count)
                                print(a)
                                for i in range(len(a)):
                                    print(a[i])
                                    chars[index]=a[i]
                                    index+=1
                                    tcount.append(a[i])
                    else:
                        chars[index]=str(count)
                        index+=1
                        tcount.append(str(count))
                    

        
        return len(tcount)