def max_subarray(arr,left,right):
    if left == right:
        return arr[left]
    
    mid=(left+right)//2
    # 左边最大字段和
    left_max = max_subarray(arr, left, mid)

    # 右边最大字段和
    right_max = max_subarray(arr, mid + 1, right)

    # 横跨中点最大字段和
    left_sum=float('-inf')
    s=0
    for i in range(mid,left-1,-1):
        s+=arr[i]
        left_sum=max(left_sum,s)
    
    right_sum=float('-inf')
    s=0
    for i in range(mid+1,right+1):
        s+=arr[i]
        right_sum=max(right_sum,s)

    cross_max=left_sum+right_sum

    return max(left_max,right_max,cross_max)

if __name__=="__main__":
    arr=list(map(int,input("数据:").split()))
    print(f"最大字段和:{max_subarray(arr,0,len(arr)-1)}")

