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

def print_board(checkerboard):
    for r in range(8):
        if r%2==0:
            for n in range(8):
                if n%2==0:
                    checkerboard[r][n]=0
                else:
                    checkerboard[r][n]=1
        else:
            for n in range(8):
                if n%2==0:
                    checkerboard[r][n]=1
                else:
                    checkerboard[r][n]=0
    for j in range(8):
        if 3 <= j <= 4:
            for n in range(8):
                checkerboard[j][n] = 0
    for i in range(8):
        print(checkerboard[i])

print_board(checkerboard)