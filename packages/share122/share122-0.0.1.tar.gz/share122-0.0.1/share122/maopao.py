def bubble_sort(alist):
    # j表示每次遍历需要比较的次数，是逐渐减小的
    for j in range(len(alist)-1,0,-1):
        # i表示一次比较要比较多少次
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
