intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [3,8]
flag = False

ans = []

for i in range(len(intervals)):
    start, end = intervals[i]

    if start > newInterval[1]:
        ans.append(newInterval)
        ans += intervals[i:]
        flag = True
        break
    elif end < newInterval[0]:
        ans.append(intervals[i])
    else:
        newInterval = [min(newInterval[0], start), max(end, newInterval[1])]
if flag==False:
    ans.append(newInterval)

print(ans)