def longestCommonPrefix(strs):

    ans = ""
    for i in range(len(strs[0])):

        isCommon = True
        prefix = strs[0][:i + 1]
        # print(i + 1, "回目")
        for j in range(1, len(strs)):
            if strs[j][:i + 1] != prefix:
                isCommon = False
                break
        
        if isCommon:
            ans = prefix
        else:
            break

        # print("count:", count)

    return ans


def longestCommonPrefixMod(strs):
    pre = strs[0]
    
    for i in strs:
        while not i.startswith(pre):
            # 配列の一番最初の文字（pre）を後ろから削っていって、配列の各要素がpreから始まるかを照合するイメージ
            pre = pre[:-1]
            if not pre:
                return pre
    
    return pre 

strs = ["flower","flow","flight"]



print(longestCommonPrefix(strs))