nums = [6, 4, 2, 14, 8, 10, 12, 16]

print("Array : ",nums)

elementPos = []
for i in range(len(nums)):
    elementPos.append((i,nums[i]))
print("Before Sorting element position array : ", elementPos)


elementPos.sort(key=lambda x: x[1])
print("After Sorting element position array :  ", elementPos)

vis = [False] * len(nums)
ans = 0
for i in range( len(nums)):
    if vis[i] == True or elementPos[i][0] == i:
        continue
    else:
        cycle_len = 0
        j = i
        while vis[j] == False:
            vis[j] = True
            cycle_len += 1
            j = elementPos[j][0]

        ans += (cycle_len-1)

print(ans)