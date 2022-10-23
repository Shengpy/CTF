import timeit
L=int(input())
U=int(input())
start = timeit.default_timer()
n=0
for i in range(L,U+1):
    s=str(i)
    check=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
             check=1
    if(check):
         continue
    n+=1
stop = timeit.default_timer()
print(n)
print('Time: ', stop - start)  