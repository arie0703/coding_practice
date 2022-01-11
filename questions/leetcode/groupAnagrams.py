# Find Anagrams from given array
# O(n*2) (It is not good)
def groupAnagrams(strs):
    res = []
    def findGroup(s):
        group = []
        start = strs.index(s)
        length = len(s)

        for i in range(start, len(strs)):

            if strs[i] == s:
                group.append(s)
                continue

            if len(strs[i]) != length:
                continue
            temp = strs[i]
            for j in range(length):
                if not s[j] in temp:
                    break
                temp = temp.replace(s[j], '', 1)   
                
            if not temp:
                group.append(strs[i])
                
        for g in group:
            strs.remove(g)
        return group
    

    while strs:
        res.append(findGroup(strs[0]))

    return res


# https://leetcode.com/problems/group-anagrams/discuss/1473638/python-hashmap

# Using Hashmap, O(n), it is better.
def solutionWithHashMap(strs):
    hashMap = {}

    if len(strs) == 1 and (strs[0] == "" or len(strs[0]) == 1):
        return [strs]

    for i in range(0,len(strs)):                  #iterate through the list
        ordered_key =''.join(sorted(strs[i]))     #sorting each character in the current str and joining them to a string
        print(ordered_key)
        if ordered_key not in  hashMap.keys():    #if this key is not in the dictionary/hash map
            hashMap[ordered_key] = [strs[i]]     # add the key and value
        else:
            hashMap[ordered_key].append(strs[i]) # or append the word to existing key
    return  hashMap.values()    

strs = ["eat","tea","tan","ate","nat","bat"]
print(solutionWithHashMap(strs))