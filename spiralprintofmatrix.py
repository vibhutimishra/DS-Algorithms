class Spiral:
    def spiralOrder(matrix):
        ans=[]
        r=len(matrix)
        if r==0:
            return ans
        c=len(matrix[0])
        for i in range(c):
            ans.append(matrix[0][i])
        if r==1 and c==1:
            return ans
        if r==1:
            return ans
        if c==1:
            for i in range(1,r):
                ans.append(matrix[i][0])
            return ans
        countr=r-1
        countc=c-1
        i=0
        j=countc
        repeat=0
        while countr>0 or countc>0:
            if repeat==0:
                if countr==0:
                    break
                for k in range(countr):
                    i+=1
                    ans.append(matrix[i][j])
                countr-=1
                repeat=1
            elif repeat==1:
                if countc==0:
                    break
                for k in range(countc):
                    j-=1
                    ans.append(matrix[i][j])
                countc-=1
                repeat=2
            elif repeat==2:
                if countr==0:
                    break
                for k in range(countr):
                    i-=1
                    ans.append(matrix[i][j])
                repeat=3
                countr-=1
            elif repeat==3:
                if countc==0:
                    break
                for k in range(countc):
                    j+=1
                    ans.append(matrix[i][j])
                repeat=0
                countc-=1
        return ans
