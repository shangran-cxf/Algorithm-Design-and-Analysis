#归并排序
def merge_sort(arr):
    #递归终止条件
    if len(arr)<=1:
        return arr
    #分(Divide)
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    #合(Conquer)
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__=="__main__":
    arr = list(map(int, input("请输入待排序（空格分隔）: ").split()))
    print(f"排序后:{merge_sort(arr)}")