#部分集合
def subset_from_vector(v, a_set):
    '''特性列と集合を元に，部分集合を返す関数．
    入力は特性列vと集合（のリスト表現）a_set，出力は特性列に対応する部分集合（のリスト表現）である．'''
    
    subset = [] # 部分集合を空のリストとする．
    if len(v) != len(a_set): # 特性列と集合の大きさが異なるならば，
        return subset # 空の集合（リスト）を返す．
    for vi, element in zip(v, a_set): # 特性列vと集合a_setのそれぞれの要素に関して，
        if vi == 1: # 特性列の要素が1ならば，
            subset.append(element) # 対応する要素を部分集合に加える．
    return subset
    

def power_set(a_set=['a', 'b', 'c']):
    '''べき集合を返す関数．
    深さ優先探索を基に部分集合の特性列（characteristic sequence）を列挙する．
    入力は集合（のリスト表現）a_set，出力はべき集合p_set（のリスト表現）である． '''
    
    p_set = [] # 部分集合を保存するためのリスト
    stack = [[]] # スタックという名のリスト，
    while len(stack) > 0: # スタックが空でない限り以下を繰り返す．
        v = stack.pop() # スタックから0-1列を1つ取り出す．
        if len(v) == len(a_set): # 0-1列が与えられた集合の要素数と同じ長さならば，
            p_set.append(subset_from_vector(v, a_set)) # その0-1ベクトルが特性列であると見なして，部分集合を作り，それをべき集合に加える．
        else: # 0-1列が集合の要素数よりも短いならば，
            stack += [v + [0]] # それに0を追加した列をスタックに加える．
            stack += [v + [1]] # それに1を追加した列もスタックに加える．
    return p_set # 最後にべき集合を返す．


#順列

def enumerate_all_permutations(sequence=['a', 'b', 'c']):
    '''順列を列挙する関数．
    深さ優先探索探索を元に順列を列挙する．
    '''
    
    permutations = [] # 順列を保存するためのリスト
    S = [([], sequence)] # 「順列の部分列」と「部分列で使われていない残り」の組をスタックに保存する．
    while len(S) > 0: # スタックが空でない限り以下を繰り返す．
        subsequence, remaining = S.pop() # スタックから（「部分列」，「残り」）を1つ取り出す．
        if len(remaining) == 0: # 「部分列で使われていない残り」が空ならば，部分列は順列になっているはずなので，
            permutations += [subsequence] # その部分列を順列に加える．
        else: # 「部分列で使われていない残り」があるならば
            for r in remaining: # その残りのそれぞれに関して，
                remaining_copy = remaining[:] 
                remaining_copy.remove(r) # 残りを1つ取り除いて，
                S += [(subsequence + [r], remaining_copy)] # それを部分列に追加した列と残りをスタックに入れる．
    return permutations # 最後にまとめて，全ての部分集合を返す．


print(power_set(['a', 'b', 'c']))