def findSmallest(arr, n):
    ans = 1
    arr.sort()
    print(arr)
    for i in arr:
        if i > ans:
            return ans
        ans += 1
    return ans


arr1 = [1, 10, 3, 11, 6, 15]

n1 = len(arr1)

print(findSmallest(arr1, n1))
