class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.val)
    inorderTraversal(root.right)



if __name__ == '__main__':
    root_ = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
                     TreeNode(3, None, TreeNode(8, TreeNode(9))))
    inorderTraversal(root_)
