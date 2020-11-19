#question link
# https://www.hackerearth.com/practice/algorithms/searching/linear-search/tutorial/

if __name__=="__main__":
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    b=int(b)
    a=int(a)
    i=0
    p=[]
    for i in range(a):
        if arr[i]==b:
            p.append(i)
    print(max(p)+1)