def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left,right=merge_sort(arr[:mid]),merge_sort(arr[mid:])
    return merge(left,right,arr.copy())

def merge(left,right,merged):
    left_cur,right_cur=0,0
    while left_cur<len(left) and right_cur<len(right):
         if left[left_cur]<=right[right_cur]:
             merged[left_cur+right_cur]=left[left_cur]
             left_cur+=1
         else:
             merged[left_cur + right_cur] = right[right_cur]
             right_cur+=1
    for left_cur in range(left_cur,len(left)):
        merged[left_cur+right_cur]=left[left_cur]
    for right_cur in range(right_cur, len(right)):
        merged[left_cur + right_cur] = right[right_cur]

    return merged



print(merge_sort([2, 5, 1, 3]))