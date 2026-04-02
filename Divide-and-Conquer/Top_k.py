def Top_k(arr,k):
    def quick_select(left,right,k):
        if left>=right:
            return 
        pivot=arr[left]
        i=left
        j=right
        while i<j:
            while i < j and arr[j] <= pivot:
                j -= 1
            arr[i] = arr[j]

            while i < j and arr[i] >= pivot:
                i += 1
            arr[j] = arr[i]

        arr[i]=pivot

        count=i-left+1

        if count==k:
            return 
        elif count>k:
            quick_select(left,i-1,k)
        else:
            quick_select(i+1,right,k-count)
        
    quick_select(0,len(arr)-1,k)
    return arr[:k]

if __name__=="__main__":
    arr=list(map(int,input("请输入待查询数据:").split()))
    k=int(input("待查询K为:"))
    print(f"该数据的前K个数据为:{Top_k(arr,k)}")