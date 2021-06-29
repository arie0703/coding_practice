import fractions as fr #分数を作ってくれる

def simple_solution(p, q, a, n):
    stack = [(fr.Fraction(p, q), ())] # (単位分数分解していない残り，単位分数分解のそれぞの分母を昇順でならべたタプル)というタプルで探索ノードを覚える．
    count = 0 # 単位分数分解の個数を0とする．
    
    while len(stack) > 0: # 探索していないノードがある限り以下を繰り返す．
        rest, denominators = stack.pop() # 最後に覚えた探索ノードを取り出し，単位分数分解の残りをrest，単位分数分解の分母の列をdenominatorsとする．
        if rest == 0: # 単位分数分解の残りが0ならば，単位分数分解が完了したということなので，
            count += 1 # 単位分数分解の個数を1増やし，
            continue # 以降の処理は省略する．
        if len(denominators) >= n: # （単位分数分解の残りがあって）単位分数分解の分母の列が，指定された個数上限n以上ならば
            continue # これ以上は探索しても条件に合わないので，以降の処理は省略する．
        denom_prods = 1 # これ以降の3行で，ここまでの単位分数分解の分母の積をdenom_prodsとする．
        for d in denominators:
            denom_prods *= d
        if len(denominators) > 0: # これ以降の4行で，これまでの単位分数分解の分母があれば
            start_denominator = denominators[-1] # その最後の（最大の）分母をstart_denominatorとし
        else: # そうでなくて，まだ1つも単位分数分解がなければ，
            start_denominator = 1 # 1をstart_denominatorとする．
        #start_denominator = max(start_denominator, math.ceil(rest.denominator/rest.numerator))
        #end_denominator = min(a, int(n / rest))
        end_denominator = a # 吟味する最大の分母はaで十分である．
        for x in range(start_denominator, end_denominator + 1): # start_denominatorからend_denominatorのそれぞれに関して，
            new_frac = fr.Fraction(1, x) # それを分母とする単位分数new_fracを作り，
            if new_frac > rest: # その新しい単位分数が，単位分数分解の残りより大きければ，
                continue # 単位分数分解の候補ではないので，以降の処理を省略する．
            if denom_prods * new_frac.denominator > a: # これまでの単位分数分解の分母の積と新しい分母の積がaよりも大きければ，
                break # 問題設定の単位分数分解の条件に当てはまらないので，以降の処理を省略する．
            #if (rest - new_frac).denominator * denom_prods * new_frac.denominator > a:
                #continue
            stack.append((rest - new_frac, denominators + (new_frac.denominator,))) # ここまでの条件を満たしているならば，単位分数分解の候補なので，その単位分数を加えたものを新たな探索ノードとしてスタックに加える．
    return count # 最後に単位分数分解の個数を返す．

import math

def better_solution(p, q, a, n):
    # 先程のsimple_solutionと同じコメントは省く．
    stack = [(fr.Fraction(p, q), ())]
    count = 0
    while len(stack) > 0:
        rest, denominators = stack.pop()
        if rest == 0:
            count += 1
            continue
        if len(denominators) >= n:
            continue
        denom_prods = 1
        for d in denominators:
            denom_prods *= d
        if len(denominators) > 0:
            start_denominator = denominators[-1]
        else:
            start_denominator = 1
        start_denominator = max(start_denominator, math.ceil(rest.denominator/rest.numerator)) # 分母の候補は，残りの逆数の切り上げから試せば十分である．
        #end_denominator = a # 吟味する最大の分母はaで十分であるが，吟味する分母の最大値がaは大きすぎる．
        end_denominator = min(a, int(n / rest)) # n - len(denominators)，すなわち許される残りの単位分数分解個数では「分解されていない残り」に到底及ばないほどの小さい分数は吟味する必要がない．
        for x in range(start_denominator, end_denominator + 1):
            new_frac = fr.Fraction(1, x)
            #if new_frac > rest: # start_denominatorを新しいものに置き換えたので，
                #continue # これら2行は必要なくなった．
            if denom_prods * new_frac.denominator > a:
                break
            if (rest - new_frac).denominator * denom_prods * new_frac.denominator > a: # 残りも含めて分数の積がaよりも大きければ吟味する必要はない．
                continue
            stack.append((rest - new_frac, denominators + (new_frac.denominator,)))
    return count


print(simple_solution(2, 3, 120, 3))
print(better_solution(2, 3, 120, 3))
