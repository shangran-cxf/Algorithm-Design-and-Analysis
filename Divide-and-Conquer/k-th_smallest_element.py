#查找第k小元素
def quick_select(arr,left,right,k):
    if left==right:
        return arr[left]
    pivot=arr[left]
    i=left
    j=right
    while i<j:
        while i<j and  arr[j]>=pivot:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<=pivot:
            i+=1
        arr[j]=arr[i]
    arr[i]=pivot

    #判断位置
    if k-1==i:
        return arr[i]
    elif k-1<i:
        return quick_select(arr,left,i-1,k)
    else:
        return quick_select(arr,i+1,right,k)
    
if __name__=="__main__":
    arr=list(map(int,input("请输入查找总数据:").split()))
    k=int(input("请问查找第几小的数据:"))
    print(f"第k小的数据为:{quick_select(arr,0,len(arr)-1,k)}")
