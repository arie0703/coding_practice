# 複数個のリストをマージする

from collections import deque

def mergeTwoLists(list1, list2):
    i, j = 0, 0
    merged = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged.append(list2[j])
            j += 1
            
        else:
            merged.append(list1[i])
            i += 1
            

    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

def mergeKLists(lists):
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 0:
        return lists


    queue = deque(lists)
    while len(queue) > 1:
        queue.appendleft(mergeTwoLists(queue.pop(), queue.pop()))


    return(queue.pop())
        
lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists))
lists = [[1,4,5],[1,3,4],[2,6],[-1, 0, 20, 50],[3,4,5,6,7,8,9]]
print(mergeKLists(lists))
lists = [[]]
print(mergeKLists(lists))
            
