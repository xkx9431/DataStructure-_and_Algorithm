def partition(array,begin,end):
    #选取最后一个元素为中转元素
    pivot=array[end]
    i=begin
    for j in range(begin,end):
        if array[j]< pivot:
            array[i],array[j]=array[j],array[i]
            i=i+1
    array[i],array[end]=array[end],array[i]
    return i

def quick_sort_recursion(array,begin,end):
    if begin >= end:
        return
    pivot_idx= partition(array,begin,end)
    quick_sort_recursion(array,begin,pivot_idx-1)
    quick_sort_recursion(array,pivot_idx+1,end)

def quick_sort(array):
    end =len(array)-1
    return quick_sort_recursion(array,0,end)

a=[2,5,1,3]
print(a)
quick_sort(a)
print(a)