def mergeTwoLists(list1, list2):
    i, j = 0, 0
    merged = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged.append(list2[j])
            print(list2[j])
            j += 1
            
        else:
            merged.append(list1[i])
            print(list1[i])
            i += 1
            

    if i < len(list1):
        merged.extend(list1[i:])
    if j < len(list2):
        merged.extend(list2[j:])

    return merged

print(mergeTwoLists([1,2,4],[1,3,4]))
            

            
            

