testcase = int(input())
for i in range(testcase):
    t,p = map(int, input().split())
    totalt = 0
    ws = 0
    #print("t\ttotalt\tws")
    while totalt<1000:
        if t>=299:
            break
        ws+=1
        t+=1
        totalt = p + ws*20 + t
        if totalt>=1000:
            ws-=1
            break
        #print(f"{t}\t{totalt}\t{ws}")

    print(ws)