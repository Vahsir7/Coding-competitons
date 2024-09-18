testcase= int(input())
for i in range(testcase):
    l=int(input())
    array = list(map(int, input().split()))
    if l==3:
        print(0)
    else:
        array.sort()
        mindiff = max(array)
        for i in range(l-1):
            diff = array[i+1]-array[i]
            if diff<mindiff:
                mindiff = diff
        print(mindiff)
