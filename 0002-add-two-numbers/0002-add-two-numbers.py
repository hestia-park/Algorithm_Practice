# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 결과를 저장할 더미 노드
        current = dummy
        carry = 0  # 자리 올림값 초기화

        while l1 or l2 or carry:
            # 각 노드의 값을 가져오거나, 없으면 0으로 설정
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 합 계산
            total = val1 + val2 + carry
            carry = total // 10  # 자리 올림
            current.next = ListNode(total % 10)  # 현재 노드에 값 추가

            # 다음 노드로 이동
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next