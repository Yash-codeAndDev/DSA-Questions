grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

row = len(grid)
col = len(grid[0])

score = 0

score = (1 << (col-1)) * row # for score to be maximum first col must be all 1's

for i in range(1,col):

    count_one_col = 0
    for j in range(row):
        if grid[j][0] == grid[j][i]:
            count_one_col += 1
    
    count_one_col = max(count_one_col,row-count_one_col)

    count_one_col = (1 << (col - i -1 )) * count_one_col

    score += count_one_col


print(score)