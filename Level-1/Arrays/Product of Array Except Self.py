nums = [-1,1]
n = len(nums)
pref_prod = [nums[0]]
post_prod = [nums[n - 1]]
for i in range(1, n):
    pref_prod.append(pref_prod[i - 1] * nums[i])
    post_prod.append(post_prod[i - 1] * nums[n - i - 1])

post_prod.reverse()
ans = []
for i in range(n):
    if i == 0:
        ans.append(post_prod[i + 1])
        continue
    if i == n - 1:
        ans.append(pref_prod[n - 2])
        continue

    ans.append(pref_prod[i - 1] * post_prod[i + 1])

print(ans)