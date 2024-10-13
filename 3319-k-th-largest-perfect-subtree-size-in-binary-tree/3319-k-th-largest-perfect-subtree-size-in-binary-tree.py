# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.perfect_subtree_sizes = []

        def is_perfect_tree(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_size = is_perfect_tree(node.left)
            right_size = is_perfect_tree(node.right)
            if left_size == -1 or right_size == -1 or left_size != right_size:
                return -1
            size = 1 + left_size + right_size
            self.perfect_subtree_sizes.append(size)
            return size

        is_perfect_tree(root)
        self.perfect_subtree_sizes.sort(reverse=True)
        
        return self.perfect_subtree_sizes[k-1] if k <= len(self.perfect_subtree_sizes) else -1
        
            
            
            
                
            