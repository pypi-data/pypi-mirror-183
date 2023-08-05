def QSort(lst, left, right):
    if left >= right:
        return
    l, r, key = left, right, lst[left]
    while l < r:
        while l < r and lst[r] >= key:
            r -=1
        lst[l] = lst[r]
        while l < r and lst[l] < key:
            l += 1
        lst[r] = lst[l]
    lst[l] = key
    QSort(lst, left, l-1)
    QSort(lst, l+1, right)
    return lst