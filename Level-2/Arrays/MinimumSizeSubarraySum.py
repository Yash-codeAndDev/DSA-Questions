nums = [2, 3, 1, 2, 4, 3]
target = 7
shortest = float('inf')
prefix_sums = [0 for num in nums]
prefix_sums[0] = nums[0]
for i in range(1, len(nums)):
    prefix_sums[i] = prefix_sums[i - 1] + nums[i]


def binary_search(i, prefix_sums):

    l = i
    r = len(prefix_sums)
    # it has to be greater than last index or
    # if you have one element, you will return back
    # the wrong element. E.g. [10] target== 20
    # w/o correction l == r immediately and you return index 0
    # but that is not correct, by r out of range, you will
    # return a l that is out of range so you know what happened.
    while l < r:
        m = l + (r - l) // 2
        if prefix_sums[m] - prefix_sums[i] + nums[i] >= target:
            r = m
        else:
            l = m + 1

    return l


for i in range(0, len(nums)):
    j = binary_search(i, prefix_sums)
    if j < len(prefix_sums):  # you need this because the condition might not be satisfied
        shortest = min(shortest, j - i + 1)

        # brute force commented out. Notice how since the prefix_sums
        # is increasing, the brute force break condition becomes the
        # "find condition" in the binary search. Originally we had:
        # for j in range(0, len(nums)):
        #     if prefix_sums[j]-prefix_sums[i] + nums[i] >= target:
        #         shortest = min(shortest, j-i+1)
        #         break

print(shortest) if shortest != float('inf') else print("-1")
