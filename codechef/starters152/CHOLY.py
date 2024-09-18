w, d, l = map(int, input().split())
x,y,z = w,d,l
games = w+d+l
while games<4:
    d+=1
    games +=1
xpoints = w*1+d*0.5+l*0
ypoints = w*0+d*0.5+l*1    
ans = True if xpoints > ypoints else False
if not ans:
    w,d,l = x,y,z
    games = w+d+l
    #print(games)
    while games<4:
        w+=1
        games +=1
    xpoints = w*1+d*0.5+l*0
    #print(xpoints)
    ypoints = w*0+d*0.5+l*1
    ans = True if xpoints > ypoints else False
print("Yes") if ans else print("No")


    
