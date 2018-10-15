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
