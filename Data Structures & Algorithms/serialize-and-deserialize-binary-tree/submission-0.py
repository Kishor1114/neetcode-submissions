# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(node):
            if not node:
                return "None,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)

        return preorder(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def build_tree(values):
            if values[0] == "None":
                values.pop(0)
                return None

            root = TreeNode(int(values.pop(0)))
            root.left = build_tree(values)
            root.right = build_tree(values)

            return root

        values = data.split(",")
        return build_tree(values[:-1])
