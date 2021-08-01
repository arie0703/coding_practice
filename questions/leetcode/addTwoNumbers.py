from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q = deque()
        carry = result = ListNode(0)
        while l1 or l2:
            if l1 != None and l2 != None:
                value = l1.val + l2.val
            elif l2 == None:
                value = l1.val
            elif l1 == None:
                value = l2.val
            
            if value > 9: #二つの数字を足した数の桁が2桁の場合
                if q: #前のnodeでの繰り上がりがある場合
                    #二つの一桁の数字の和が19になることはないので、value%10が９の時の処理は省いてオーケー
                    carry.val = (value % 10) + q.popleft()
                else:
                    carry.val = value % 10
                q.appendleft(1) #valueは２桁なので繰り上がりの桁をqに入れておく
                
                
            else: #二つの数字を足した数の桁が１桁の場合
                if q: #前のnodeでの繰り上がりがある場合
                    if value < 9: #一の位が9ではない時
                        value += q.popleft()
                    else: #９の時
                        value = 0
                        #本来はここで繰り上がりの桁ができてqに1をappendleftするはずだが、
                        #popleftによって前回の桁を消費してない
                        #ゆえに前回の繰り上がりを今回の繰り上がりとして次のループに持ち越す
                    carry.val = value
                else:
                    carry.val = value
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
            if l1 or l2:
                carry.next = ListNode(0)
                carry = carry.next

        if q: #最後に繰り上がり桁が残ってたらそれを加えてやる
            carry.next = ListNode(q.popleft())
            
        return result
'''
Memory Usage: 14.1MB
Run Time: 72ms
'''