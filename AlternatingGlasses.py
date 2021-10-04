totaln = int(input("enter total number of glasses:" ))
n = int(totaln/2)
moves=0
lst = list(n*'1'+n*'0')
print(lst)
def AlternatingGlasses(n,lst,moves):
    for i in range(0,n):
        if i%2!=0:
            lst[i],lst[-i-1]=lst[-i-1],lst[i]
            moves+=1
    print("number of moves =",moves)
AlternatingGlasses(n,lst,moves)
print(lst)
