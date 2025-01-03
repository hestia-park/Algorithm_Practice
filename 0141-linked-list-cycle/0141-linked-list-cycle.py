class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:  # fast가 끝에 도달하면 사이클이 없음
                return False
            slow = slow.next  # slow는 한 칸 이동
            fast = fast.next.next  # fast는 두 칸 이동

        return True  # slow와 fast가 만났다면 사이클이 있음
