exp = '1+2*3+4*5'

nums, opr = [], []
temp = ''
for x in exp:
    if x == '+' or x=='*':
        nums.append( int(temp))
        opr.append(x)
        temp = ''
    else:
        temp += x


nums.append(int(temp))
print('nums array : {}'.format(nums))
print('operand array : {}'.format(opr))

dp = [[() for _ in range(len(nums))] for _ in range(len(nums))]

for gap in range(0,len(nums)):
    for i,j in zip(range(len(nums)) , range(gap,len(nums))):
        if i == j:
            dp[i][j] = (nums[i],nums[i])
            continue
        else:
            min_value = float('inf')
            max_value = float('-inf')
            for cut in range(i, j):
                left = dp[i][cut]
                right = dp[cut+1][j]

                if(opr[cut] == '*'):
                    max_value = max(max_value, left[1]*right[1])
                    min_value = min(min_value, left[0]*right[0])
                else:
                    max_value = max(max_value, left[1] + right[1])
                    min_value = min(min_value, left[0] + right[0])

            dp[i][j] = (min_value,max_value)



for i in range(len(dp)):
    for j in range(len(dp[0])):
            print(dp[i][j],end= " ")
    print()


