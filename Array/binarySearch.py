#question link
# https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/


def bst(arr,b,low,high):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==b:
            return mid+1
        elif arr[mid]>b:
            return bst(arr,b,low,mid-1)
        else:
           return bst(arr,b,mid+1,high)

if __name__=="__main__":
    n=int(input())
    queries=[]
    arr=list(map(int,input().split()))
    q=int(input())
    for i in range(q):
        queries.append(int(input()))
    arr.sort()
    for i in range(q):
        p=bst(arr,queries[i],0,n-1)
        print(p)
        

