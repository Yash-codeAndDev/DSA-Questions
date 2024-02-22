arr = [3,2,1,0,4]


def jump(nums, idx, end, memo):
    # We reached the end. No jumps to make further
    if idx == end:
        return 0

    if memo[idx] != -1:
        return memo[idx]

    min_jumps = float("inf")

    for j in range(nums[idx], 0, -1):

        if idx + j <= end:
            min_jumps = min(min_jumps, 1 + jump(nums, idx + j, end, memo))

    memo[idx] = min_jumps
    return memo[idx]


def min_jumps(nums):

    memo = [-1 for i in range(len(nums))]
    jump(nums, 0, len(nums) - 1, memo)
    return memo[0]

print(min_jumps(arr))
