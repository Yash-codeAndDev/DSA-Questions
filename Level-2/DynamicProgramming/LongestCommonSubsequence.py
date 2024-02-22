str1 = 'aggtab'
str2 = 'gxtxayb'


def lcsTabulation(index1 , index2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(dp)-2,-1,-1):
        for j in range (len(dp[0])-2,-1,-1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])

    return dp[0][0]

def lcsMemoization(memo, index1, index2):
    if index1 < 0 or index2 < 0:
        return 0

    if memo[index1][index2] != -1:
        return memo[index1][index2]

    if str1[index1] == str2[index2]:
        memo[index1][index2] = 1+lcsMemoization(memo, index1 - 1, index2 - 1)
        return memo[index1][index2]
    else:
        memo[index1][index2] = max(
            lcsMemoization(memo, index1 - 1, index2),
            lcsMemoization(memo, index1, index2 - 1)
        )

    return memo[index1][index2]


def lcsRecurssion(index1, index2):
    if index1 < 0 or index2 < 0:
        return 0
    if str1[index1] == str2[index2]:
        return 1 + lcsRecurssion(index1 - 1, index2 - 1)

    return max(lcsRecurssion(index1 - 1, index2), lcsRecurssion(index1, index2 - 1))


print("LCS using Recurssion : ", lcsRecurssion(len(str1) - 1, len(str2) - 1))

# memoization
memo = [[-1] * len(str2) for _ in range(len(str1))]
print("LCS using Memoization : ", lcsMemoization(memo, len(str1) - 1, len(str2) - 1) )

# tabulation
print("LCS using Memoization : ", lcsTabulation(len(str1) - 1, len(str2) - 1) )

