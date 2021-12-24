def gale_shapley(men, women, m_ranking, w_ranking):
    woman_of_man_ranking = {}
    for m in men:
        woman_of_man_ranking[m] = {}
        for w in women:
            woman_of_man_ranking[m][m_ranking[m][w]] = w

    print(woman_of_man_ranking)
    
    '''
    Step 1: フリーな男性のリストfree_menを，男性リストからコピーして作る．
    '''
    free_men = men[:]

    print(free_men)
    
    '''
    Step 2: 男性が次にアプローチする順位の辞書next_womanを作り，初期値として0を入れる．
    '''
    next_woman = {m:0 for m in men}

    print(next_woman)
    
    '''
    Step 3: 女性のパートナーの辞書partnerを作り，初期値として空リスト[]を入れる．
    '''
    partner = {w: [] for w in women}
    
    '''
    Step 4: フリーな男性のリストfree_manが空でない限り繰り返す．
    '''
    while len(free_men) > 0:
        m = free_men.pop() # フリーな男性のリストから要素を1つ取り出しmとする．
        next_woman[m] += 1 # 男性mが次にアプローチするランキングを1増やす．
        w = woman_of_man_ranking[m][next_woman[m]] # 男性mが次にアプローチする女性をwとする．
        if partner[w] == []: # その女性wのパートナーがいないならば，
            partner[w] = m # 男性mを女性wのパートナーとする．
        else: # そうではなくて，その女性wにパートナーがすでにいるならば，
            if w_ranking[w][m] < w_ranking[w][partner[w]]: # 今のパートナーよりも良いならば
                free_men.append(partner[w]) # 今のパートナーをフリーな男性のリストに加え
                partner[w] = m # 男性mを新たなパートナーとする．
            else: # 今のパートナーの方が良いならば，
                free_men.append(m) # アプローチしてきた男性mは再びフリーな男性のリストに戻る．
    
    '''
    Step 5: 女性のパートナーの辞書を返す．
    '''
    return partner

men = ['A', 'B', 'C', 'D']
women = ['E', 'F', 'G', 'H']
m_ranking = { 
            'A': {'E': 1, 'F': 2, 'G': 3, 'H': 4},
            'B': {'E': 1, 'F': 4, 'G': 3, 'H': 2},
            'C': {'E': 2, 'F': 1, 'G': 3, 'H': 4},
            'D': {'E': 4, 'F': 2, 'G': 3, 'H': 1}
            }

w_ranking = {
            'E': {'A': 3, 'B': 4, 'C': 2, 'D': 1},
            'F': {'A': 3, 'B': 1, 'C': 4, 'D': 2},
            'G': {'A': 2, 'B': 3, 'C': 4, 'D': 1},
            'H': {'A': 3, 'B': 2, 'C': 1, 'D': 4}
            }

print(gale_shapley(men, women, m_ranking, w_ranking))