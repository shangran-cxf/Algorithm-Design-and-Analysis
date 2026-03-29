#快速排序,原地修改
def quick_sort(arr,left,right):
    #终止条件:交汇
    if left>=right:
        return 
    #分(Divide)
    pivot=arr[left]
    i=left
    j=right
    while i<j:
        while i<j and arr[j]>=pivot:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<=pivot:
            i+=1
        arr[j]=arr[i]
    arr[i]=pivot
    quick_sort(arr,left,i-1)
    quick_sort(arr,i+1,right)
    
if __name__=="__main__":
    arr=list(map(int,input("请输入待排序数据:").split(' ')))
    quick_sort(arr,0,len(arr)-1)
    print(f"排序后:{arr}")
