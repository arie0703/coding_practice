def merge(intervals):
    intervals = sorted(intervals)
    i = 0

    while i < len(intervals) - 1:

        next_min = intervals[i + 1][0]
        next_max = intervals[i + 1][1]
        now_min = intervals[i][0]
        now_max = intervals[i][1]

        if now_max >= next_min:
            merged = [min(now_min, next_min),max(now_max, next_max)]
            intervals[i] = merged
            del intervals[i + 1]
        else:
            i += 1

    return intervals

print(merge([[1,4],[4,5]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[0,2],[3,5]]))
print(merge([[1,4],[0,0]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))