#二分查找,前提:数据一定要是有序的
def binary_search(arr,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,mid+1,right,target)
    else:
        return binary_search(arr,left,mid-1,target)
if __name__=="__main__":
    arr=list(map(int,input("请输入有序数据:").split(' ')))
    target=int(input("请输入待查找数据:"))
    print(f"待查找数据的下标为:{binary_search(arr,0,len(arr)-1,target)}")