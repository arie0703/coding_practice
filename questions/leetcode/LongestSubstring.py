# https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
一つの文字列の中で、一度も文字の被りがない最大の列の文字数を出力する

dvdf

d-v
  v-d-f
    d-f
      f

abcabca

a-b-c
  b-c-a
    c-a-b
      a-b-c
        b-c-a
          c-a
            c
'''


def lengthOfLongestSubstring(s: str):
    records = [0 for _ in range(len(s))] #文字数の数だけ空のリストを生成、n番目の文字の連続数はn番目の配列に記録される。
    char_list = [] #今まで登場した文字を格納
    position = 0 #どこまでのインデックスが連続記録終了しているか？
    i = 0 #ループ回数

    for char in s:
        
        while char in char_list[position:len(char_list)]:
            position += 1
    
        for p in range(position, i + 1): #もう文字の連続が終了したところの次の文字の位置から現在の文字の位置
            records[p] += 1
            #records[p].append(char)　デバッグは数字カウントじゃなくて、文字を１文字ずつ記録する形式でやるとやりやすい
        char_list.append(char)
        # print(char, ":", records, char_list)
        i += 1 
    
    if not records:
        return 0
    else:
        return max(records)



a = " "
b = "dvdf"
l = ["a","b","c"]

tes1 = "abcabcbb"
tes2 = "bbbbb"
tes3 = "pwwkew"
tes4 = ""
print(l[1:len(l)])


print(lengthOfLongestSubstring(b))
print(lengthOfLongestSubstring(tes1))
print(lengthOfLongestSubstring(tes2))
print(lengthOfLongestSubstring(tes3))
print(lengthOfLongestSubstring(tes4))
# print(l)