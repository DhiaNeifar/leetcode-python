class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1, root2):
    list1, list2 = [], []

    def leaves(root, _list):
        if root and root.left is None and root.right is None:
            _list.append(root.val)
            return
        if root.left is not None:
            leaves(root.left, _list)
        if root.right is not None:
            leaves(root.right, _list)

    leaves(root1, list1)
    leaves(root2, list2)
    return list1 == list2


if __name__ == '__main__':
    # tree1 = TreeNode(3, TreeNode(5, TreeNode(6, None, None),
    #                              TreeNode(2, TreeNode(7, None, None), TreeNode(4, None, None)), ),
    #                  TreeNode(1, TreeNode(9, None, None), TreeNode(8, None, None)))
    # tree2 = TreeNode(3, TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None), ),
    #                  TreeNode(1, TreeNode(4, None, None),
    #                           TreeNode(2, TreeNode(9, None, None), TreeNode(8, None, None))), )
    tree1 = TreeNode(1, TreeNode(2, None, None), None)
    tree2 = TreeNode(2, TreeNode(2, None, None), None)
    leafSimilar(tree1, tree2)
