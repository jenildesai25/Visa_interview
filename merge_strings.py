# VISA full time master's ph.D question.
def merge_string(a, b):
    if len(a) != len(b):
        result = ''.join(''.join(f for f in x) for x in zip(a, b))
        if len(a) > len(b):
            temp = len(b)
            result = result + a[temp:]
        elif len(b) > len(a):
            temp = len(a)
            result = result + b[temp:]
    else:
        result = ''.join(''.join(f for f in x) for x in zip(a, b))

    return result

