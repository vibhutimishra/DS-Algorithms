class Solution(object):
    def isSubsequence(self, s, t):
        l1=len(s)
        l2=len(t)
        p=""
        i=0
        j=0
        while i!=l1 and j!=l2:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==l1:
            return True
        else:
            return False
