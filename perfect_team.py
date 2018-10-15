# VISA full time master's Ph.D question.
def anything(a):
    l = list(a)

    l1 = []
    for i in l:
        l1.append(l.count(i))

    if len(l1) is 0:
        return 0

    else:
        return ((l1)[0])


print(anything("pcmbzpcmbz"))


