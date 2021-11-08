def medians(nums1, nums2):
    print(nums1)
    print(nums2)
    nums3new = nums1 + [el2 for el2 in nums2 if el2 not in nums1]
    nums3new.sort()
    print(nums3new)
    if len(nums3new) % 2 == 1:
        print(format(nums3new[len(nums3new) // 2], '.5f'))
    else:
        k = (len(nums3new) // 2)
        print(format(nums3new[k - 1] + nums3new[k] / 2, '.5f'))

nums1 = []
print("Введите количество элементов num1")
n = int(input())
print("Вводите эти элементы")
for i in range(n):
    nums1.append(int(input()))
    print(nums1)

nums2 = []
print("Введите количество элементов num2")
n = int(input())
print("Вводите эти элементы")
for i in range(n):
    nums2.append(int(input()))
    print(nums2)

medians(nums1, nums2)