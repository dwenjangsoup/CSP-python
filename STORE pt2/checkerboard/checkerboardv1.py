checkerboard = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

x=0

def print_checkerboard(checkerboard):
    for i in range(8):
        print(checkerboard[i])
        
for j in range(8):
    for x in range(8):
        checkerboard[j][x] = 1
        # print("line",i,"num",n,checkerboard[i][x])
    if 3 <= j <= 4:
        for i in range(8):
            checkerboard[j][i] = 0
    if j==7:
        print_checkerboard(checkerboard)