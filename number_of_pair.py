# visa full time master's ph.D question
def number_of_pair(a, k):
    # a = [1,1,3,3,9,46]
    # k = 47
    # answer = 1 -> (1,46)
    # a.sort()
    d = {}
    pair = 0
    i = 0
    if not a:
        return 0
    try:
        while i <= len(a):
            value = a[i]
            complement = k - value
            if complement in d:
                frequency = d.get(complement) - 1
                pair += 1
                if frequency == 0:
                    d.pop(complement, None)
                else:
                    d[complement] = frequency
            else:
                if value in d:
                    d[value] = d.get(value) + 1
                else:
                    d[value] = 1
            i += 1
        return d
    except Exception as e:
        print(e)


a = [1, 1, 3, 3, 9, 46]
k = 47
print(number_of_pair(a, k))


def numberOfPairs(a, k):
    """
    Runtime: O(n * log n)
    After sorting, I can iterate through the
    list from both sides in O(n) to find the pairs.
    """
    a.sort()
    if len(a) < 2:
        return []
    pairs = []
    start = 0
    end = len(a) - 1
    while start < end:
        n1 = arr[start]
        n2 = arr[end]
        pair = n1 + n2
        if pair < k:
            start += 1
        if pair > k:
            end -= 1
        if pair == k:
            pairs.append([n1, n2])
            start += 1
    container = {}
    for i in pairs:
        if i[1] not in container:
            key = i[0]
            value = i[1]
            container[key] = value
    if len(container) > 0:
        return len(container)
    else:
        return 0


k = 12
arr = [6, 6, 3, 9, 3, 5, 1]
print(numberOfPairs(arr, k))
