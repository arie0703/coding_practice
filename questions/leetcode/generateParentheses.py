#n個の括弧のパターンを考える→再帰関数を活用する

def helperfunc(openP, closeP, n, slate, result):

    if openP == closeP == n:
        result.append(''.join(slate))
        print(slate)
        return
    
    if openP < n+1:
        slate.append("(")
        print(openP, closeP, slate)
        helperfunc(openP+1, closeP, n, slate, result)
        slate.pop()
    if closeP < openP:
        slate.append(")")
        print(openP, closeP, slate)
        helperfunc(openP, closeP+1, n, slate, result)
        slate.pop()

    
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    slate = []
    result = []
    openP = closeP = 0
    helperfunc(openP, closeP, n, slate, result)
    return result


print(generateParenthesis(2))