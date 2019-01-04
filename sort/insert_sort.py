def insertion_sort(arr):
    """
    在每个循环迭代中，插入排序从数组中删除一个元素。
    然后，它在另一个排序数组中找到该元素所属的位置，并将其插入其中。
    它重复这个过程，直到没有输入元素
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        cur = arr[i]
        pos = i

        while pos>0 and arr[pos-1]>cur:
            arr[pos]=arr[pos-1]
            pos = pos -1
        arr[pos]=cur
    return arr
print(insertion_sort([8,5,34,7,3,1]))
