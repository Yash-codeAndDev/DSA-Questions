def lisDpAndBinarySearch(nums):
    n = len(nums)
    ans = [nums[0]]

    for i in range(1, n):
        if nums[i] > ans[-1]:
            ans.append(nums[i])
        else:
            # binary Search
            low = 0
            high = len(ans) - 1

            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            ans[low] = nums[i]
    return len(ans)


if __name__ == "__main__":
    nums = [10, 22, 9, 33, 21, 50, 41, 60]

    print("Length of LIS is", lisDpAndBinarySearch(nums))
