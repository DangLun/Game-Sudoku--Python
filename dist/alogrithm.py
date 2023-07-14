
def checkvalid(a, x, y, k):
    for i in range(0, 9):
        if a[x][i] == k:
            return False
    for i in range(0, 9):
        if a[i][y] == k:
            return False
    start_x = int(x/3)*3
    start_y = int(y/3)*3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if a[i][j] == k:
                return False
    return True
def printsolve(a):
    for i in a:
        for j in i:
            print(j, end = ' ')
        print()
def solve(a, x, y):
    if y == 9:
        if x == 8:
            printsolve(a)
            exit()
        else:
            solve(a, x+1, 0)
    elif a[x][y] == 0:
        for i in range(1, 10):
            if checkvalid(a, x, y, i):
                a[x][y] = i
                solve(a, x, y + 1)
                a[x][y] = 0
    else:
        solve(a, x, y + 1)
cur = [[9,0,0,0,1,3,0,0,0],
    [0,0,0,0,0,0,0,0,6],
	[0,5,0,8,0,0,2,3,0],
	[0,0,0,0,5,0,0,0,9],
	[0,0,3,0,0,0,0,2,0],
	[0,7,0,9,8,0,0,0,1],
	[8,0,1,0,7,0,0,6,0],
	[0,0,0,0,2,0,0,0,0],
	[0,6,0,0,0,0,0,5,8]]

