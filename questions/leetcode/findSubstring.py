# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

from collections import deque

def findSubstring(s, words):
    length = len(words[0])
    # start = 0
    # idx = 0 #調査開始位置
    ans = []

    def serach(length, start, idx, ans, d):
        while idx + (len(words) * length) <= len(s):
            end = start + length
            target = s[start:end]
            
            if target in d:
                d.remove(target)
                print(start, idx, target,d)
                if not d: # dから全て取り除いた
                    ans.append(idx)
                    d.append(s[idx:idx+length]) #idxから始まる最初の一単語だけをdequeに追加、ループ回数短縮
                    idx += length
                start += length
            else:
                d = deque(words) # reset
                start = idx = idx + length # スタートを調査開始位置の次の位置にずらす

        return ans
                
    for i in range(length): 
        """
        スタート位置をずらす 
        "abcabcabc"という文字列が与えられた時、 
        "abc","abc","abc"だけではなく "bca", "bca"といった調査方法も可能
        """
        ans = serach(length, i, i, ans, deque(words))
    return sorted(ans)
    


# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/1643759/python-solution-low-memory-usage
def betterSolution(s, words):
    res = []
    window = sum([len(w) for w in words])

    for i, c in enumerate(s[:len(s)-window+1]):
        sub_str = s[i:i+window] # sの開始位置iからwordsの要素数ぶんの部分文字列
        # 開始位置iを一個ずつずらしながらsub_strを設定、sub_strにwwの文字列が全て入っていればtrue
        fit=True
        ww=words[:] # wordsをコピー
        while ww:
            finds=False
            for w in ww:
                if sub_str.startswith(w):
                    sub_str=sub_str.replace(w,'',1)
                    ww.remove(w)
                    finds=True
                    break
            if not finds:
                fit=False
                break
            
        if fit:
            res.append(i)
    return res      

# print(findSubstring("barfoothefoobarman",["foo","bar"]))
# print(findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))
# print(findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
# print(findSubstring("aaa",["a", "a"]))
# print(findSubstring("bcabbcaabbccacacbabccacaababcbb",["c","b","a","c","a","a","a","b","c"]))
# print(findSubstring("aaaaaaaaaaaaaa",["aa", "aa"]))
# print(findSubstring("abababab",["ab", "ba"]))
