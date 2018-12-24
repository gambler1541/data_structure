class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None


    def preorder(self, n):
        if n != None:
            print(str(n.item),' ', end=' ')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ', end=' ')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ',end=' ')

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item),' ',end=' ')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == '__main__':
    t = BinaryTree()
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)
    n5 = Node(500)
    n6 = Node(600)
    n7 = Node(700)
    n8 = Node(800)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    t.root = n1

    print('트리 높이:', t.height(t.root))
    print('전위 순회:\t', end='')
    t.preorder(t.root)
    print('\n중위 순회:\t', end='')
    t.inorder(t.root)
    print('\n후위 순회:\t', end='')
    t.postorder(t.root)
    print('\n레벨 순회:\t', end='')
    t.levelorder(t.root)
