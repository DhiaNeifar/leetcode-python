class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root, low, high):
    if not root:
        return 0
    if root.val < low or root.val > high:
        return rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)


if __name__ == '__main__':
    tree = TreeNode(10, TreeNode(5, TreeNode(3, None, None), TreeNode(7, None, None)),
                    TreeNode(15, None, TreeNode(18, None, None)))

    _low, _high = 7, 15
    rangeSumBST(tree, _low, _high)
