from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first = []
        second = []
        def BFS(root):

            if root is None:
                return 
            queue = deque([root])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node.val)
                # enqueue left child
                if node.left:
                    queue.append(node.left)
                # enqueue right child
                if node.right:
                    queue.append(node.right)
                else:
                    result.append(None)
            return result

        first = BFS(p)
        second = BFS(q)

        return first == second
