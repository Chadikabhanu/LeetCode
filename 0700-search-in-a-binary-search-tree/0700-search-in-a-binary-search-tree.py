class Solution:
    def searchBST(self, root , key):

        while root:
            if root.val == key:
                return root
            elif key < root.val:
                root = root.left
            elif key > root.val:
                root = root.right
        return None