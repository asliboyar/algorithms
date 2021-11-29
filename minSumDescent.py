def minSumDescent(a):  
    b = []
    for i in range(len(a)):
      b.append(None)
    
    n = len(a) - 1
    for i in range(len(a[n])):
        b[i] = a[n][i]

    for i in range(n-1, -1,-1):
        for j in range(len(a[i])):
            b[j] = a[i][j] + min(b[j], b[j + 1])
    return b[0]

a = [[ 2 ], [4, 8 ],[1, 3, 6 ]]
print(minSumDescent(a))
