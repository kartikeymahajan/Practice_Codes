def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    bothlist = nums1 + nums2
    print(bothlist)
    bothlist.sort()
    n = len(bothlist)/2
    
    if len(bothlist)%2==0:
        temp = bothlist[int(n-1)] + bothlist[int(n)]
        ans = temp / 2
        return ans
    else:
        return bothlist[int(n)]

li1=[2, 3, 5, 8]
li2=[10, 12, 14, 16, 18, 20]

op = findMedianSortedArrays(li1, li2)
print("Median:",op)


