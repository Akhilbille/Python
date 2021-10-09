def maxSubarrayProduct(arr):
    n=len(arr)
    result = arr[0]
    for i in range(n):
        mul = arr[i]
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]
        result = max(result, mul)
    return result
 
# Driver code
arr = [ 2,0,-3,8,-4,-9]
n = len(arr)
print("Maximum Sub array product is" , maxSubarrayProduct(arr))