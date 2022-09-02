def merge(nums1, m, nums2, n) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while 0 <= p1 and 0 <= p2:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]