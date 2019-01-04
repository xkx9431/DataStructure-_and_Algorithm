def selection_sort(arr):
    for i in range(len(arr)):
        mininum=i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[mininum]:
                mininum = j
        arr[mininum],arr[i]=arr[i],arr[mininum]
    return arr

print(selection_sort([0, 1, 8, 3, 9, 6,3,5]))