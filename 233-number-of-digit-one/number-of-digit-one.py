class Solution(object):
    def count_1(self,n,c,s):
        m=0
        if n==1:
            return int(s[(len(s)-c+1):])+(((c-1)*(10**(c-2)))+1)
        elif n>1:
            m=(10**(c-1))
            return m+(n*(c-1)*(m/10))
        else:
            return 0
    def countDigitOne(self, n):
        if n==0:
            return 0
        count=0
        x=[]
        t=n
        while t>0:
            x.append(t%10)
            t//=10
        x=x[::-1]
        s=str(n)
        for i in range(len(x)-2,-1,-1):
            count+=self.count_1(x[i],len(x)-i,s)
        if x[(len(x))-1]>0:
            return count+1
        return count
        