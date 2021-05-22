#https://icpc.iisf.or.jp/past-icpc/domestic2007/A_ja.html
#使用環境: VScode

import math

input_file = open('input.txt') #ここでインプットするファイル名を指定　ここではinput.txtとする
output_file = open('output.txt', 'w') #第一引数に出力結果を書き込むファイル名を指定 ここではoutput.txtとする。
l = input_file.readlines() #input_fileのサンプルデータの内容を変数lに格納する

#lに格納されたデータのうち、最後の0が残るまで処理をループさせる。
while len(l) > 1:
    # 審判の数
    n = int(l[0])
    #点数を格納するリスト
    score_list = []
    #リストの中に0だけが残ったらループ終了
    if n == 0:
        break
    for i in range(1, n + 1):
        score_list.append(int(l[i]))
        

    #スコアの最小値と最大値を除外
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))

    #平均をとる
    score = math.floor(sum(score_list) / len(score_list))

    output_file.write(str(score) + '\n')

    #スコア算出に使用した点数、及び審判の数を表す値をlから削除、ループの最初に戻る。
    del l[:n + 1]