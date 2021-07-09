#https://leetcode.com/problems/deepest-leaves-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        from collections import deque
        depth = 0 # 各階層を示す。rootにNoneがない場合、depth=0,1,2,3となるにつれ、leavesは1,2,4,8となる。
        #各階層のleavesの数は leaves + 2 ** depthとなる。なお、rootを格納したqueueをpopした値がNoneだった場合、次の階層の葉は２枚へる。
        leaves = 1 #最初は葉が1つなのでデフォルトは1
        node = [] #木構造を階層ごとにリストとして格納する(デバッグ用)

        queue = deque(root) #queueにrootの内容を格納、探索済みの要素はpopleftで消されていく。
        

        while queue:
            num_of_none = 0
            arr = []
            for _ in range(leaves):
                val = queue.popleft()
                if val == None:
                    #popされた値がNoneの場合、次の階層の葉は2つ減る
                    num_of_none += 2
                else:
                    arr.append(val)
                    
            print("------" + str(leaves)) 
            node.append(arr)
            print(arr, "現在の階層は", depth)
            leaves += 2 ** depth
            leaves -= num_of_none #ここで次の階層で有無を調査する葉の数が確定する。
            
            depth += 1

        print(node)
        #最後の階層のarrをreturnする
        return sum(arr)




example1 = [1,2,3,4,5,None,6,7,None,None,None,None,8]
example2 = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
print(Solution().deepestLeavesSum(example1))
print(Solution().deepestLeavesSum(example2))


