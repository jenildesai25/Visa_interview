# VISA full time bachelor question.
def numberOfWays(n):
    # Write your code here
    if n <= 1:
        return n
    d = {}
    index = 0
    temp = 2
    if n % 3 != 0:
        temp = 2
    for i in n:
        if n % 3 == 1:
            d[i] = 1
            index += 1
        if n % 1 == n:
            d[index] += 1
    return (len(d) + temp) % 1000000007

    # result = {}
    # arr = a
    # arr.sort()
    # for i in range(len(arr)):
    #     if k - arr[i] in arr[i + 1:] and k - arr[i] not in result:
    #         result[k - arr[i]] = (arr[i], k - arr[i])
    # return len(result)
