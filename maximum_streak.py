# VISA full time bachelor question.
# Complete the 'maxStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. STRING_ARRAY data
#
from odbc import dataError


def maxStreak(m, data):
    # Write your code here
    temp = 0
    if not data:
        return 0
    if m == 0 or not m:
        return 0
    for i in range(len(data)):
        if data[i].count('Y') == m:
            temp += 1
    return temp


m = 2
data = ['YY', 'NY']
print(maxStreak(m, data))
