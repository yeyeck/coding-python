
class TreeNode:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root
    

    def preOrderTraveral(self):
        print('pre order', end=': ')
        self.__preOrderTraveral(self.root)
        print()

    def __preOrderTraveral(self, node):
        if node is not None:
            print(node.val, end=', ')
            self.__preOrderTraveral(node.left)
            self.__preOrderTraveral(node.right)
            

    def levelOrderTraveral(self):
        print('level order', end=': ')
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.val, end=', ')           
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        print()


def buildBinaryTree(n: int = 15):
    root = TreeNode(1)
    queue = [root]
    i = 2
    while i <= n:
        node = queue.pop(0)
        node.left

    return BinaryTree(root)

if __name__ == '__main__':
    tree = buildBinaryTree(15)
    tree.levelOrderTraveral()
    tree.preOrderTraveral()



            
