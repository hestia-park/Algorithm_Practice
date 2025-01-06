class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 더미 노드를 사용하여 결과 리스트의 시작을 추적
        dummy = ListNode()
        current = dummy

        # 두 리스트를 순회하며 병합
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 남아 있는 노드를 결과 리스트에 추가
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
