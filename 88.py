def main(nums1, m, nums2, n):
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[i + j + 1] = nums1[i]
            i -= 1
        else:
            nums1[i + j + 1] = nums2[j]
            j -= 1
    while i >= 0:
        nums1[i + j + 1] = nums1[i]
        i -= 1
    while j >= 0:
        nums1[i + j + 1] = nums2[j]
        j -= 1


if __name__ == '__main__':
    nums1_ = [1, 2, 3, 0, 0, 0]
    m_ = 3
    nums2_ = [2, 5, 6]
    n_ = 3
    main(nums1_, m_, nums2_, n_)
