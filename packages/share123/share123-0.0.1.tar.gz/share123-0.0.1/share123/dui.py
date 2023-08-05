def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j < high and li[j] < li[j + 1]:
            j = j + 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 建堆完成了
    for i in range(n - 1, -1, -1):
        # i指向堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        # i-1指向新的high
        sift(li, 0, i - 1)
    return li