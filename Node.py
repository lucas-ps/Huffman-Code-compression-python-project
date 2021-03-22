# Tree node class for storage of characters
class Node:
    def __init__(self, left=None, right=None):
        """
         Constructor for a new node, creates a node in the tree with defined child nodes
        :param left:
        :param right:
        """
        self.left = left
        self.right = right

    def children(self):
        """
        Returns the node's child nodes
        :return: Node objects of the node's children
        """
        return self.left, self.right

    def getCharacter(self):
        """
        :return: The node object's character
        """
        return self.character

    def nodes(self):
        """
        #TODO: not 100% sure
        :return:
        """
        return self.left, self.right

    def __str__(self):
        return str(self.left), "--", str(self.right)
