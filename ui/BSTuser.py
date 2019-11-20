class Node:
    def __init__(self,username_in,password_in):
        self.username = username_in
        self.password = password_in
        self.left = None
        self.right = None
    
class BST :
    def __init__(self):
        self.root = None

    def insert(self, new_node): 
        if (self.root is None):
            self.root = new_node
        else:
            self.__insert_node(self.root, new_node)

    def __insert_node(self, current_node, new_node):
        if (new_node.username <= current_node.username):
            if (current_node.left is not None): 
                self.__insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif (new_node.username > current_node.username): 
            if (current_node.right is not None):
                self.__insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node
        else :
            print("username already in tree")
    
    def find(self, username):
        return self.__find_node(self.root, username)
    
    def __find_node(self, current_node, username):
        try :
            if username > current_node.username and current_node.right:
                return self.__find_node(current_node.right,username)
            elif username < current_node.username and current_node.left:
                return self.__find_node(current_node.left,username)
            if username == current_node.username:
                return current_node.password
            else :
                return False
        except:
                return False
    def remove(self,username):
        parent = None
        node = self.root

        while node and node.username != username:
            parent = node
            if username < node.username:
                node = node.left
            elif username > node.username:
                node = node.right
        if node.left is None and node.right is None: # no left and no right
            if username < parent.username:
                parent.left = None
            else : 
                parent.right = None
            return True
        elif node.left is None and node.right: # remove node has right child only
            if username < parent.username:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        elif node.right is None and node.left: # remove node has left child only
            if username < parent.username:
                parent.left = node.left
            else :
                parent.right = node.left
            return True
        else : # left and right
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.leftchild

            node.username = delNode.username
            if delNode.right:
                if delNodeParent.username > delNode.username:
                    delNodeParent.left = delNode.right
                elif delNodeParent < delNode.username:
                    delNodeParent.right = delNode.right
            else:
                if delNode.username < delNodeParent.username:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None
            return True
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def preorder(self,node,lis=[]): # ROOT L R
        node1 = node
        left = node1.left
        right =  node1.right
        if node1:
            lis.append(node1.username)
            if node1.left:
                self.preorder(left,lis)
            if node1.right:
                self.preorder(right,lis)
        return lis
        
    def inorder(self,node, lis=[]): # L ROOT R
        node1 = node
        left = node1.left
        right =  node1.right
        if left is not None:
            self.inorder(left,lis)
        lis.append(node1.username)
        if right is not None:
            self.inorder(right,lis)
        
        return lis

    def postorder(self,node,lis=[]): # L R ROOT
        node1 = node
        left = node1.left
        right =  node1.right
        if node1:
            if node1.left:
                self.preorder(left,lis)
            if node1.right:
                self.preorder(right,lis)
            lis.append(node1.username)
        return lis
        
        
        return lis
    def print(self):
            return self.printT()

    def printT(self):
        self.printTree(self.root)

    def printTree(self, root, space=0, gap=[15]):

        if root == None:
            return
        
        space += gap[0]

        self.printTree(root.right, space)

        for i in range(gap[0], space):
            print(end=" ")
        print(root.username)

        self.printTree(root.left, space)
    def count(self,node):
        if node is None:
            return 0
        return self.count(node.left) + self.count(node.right) + 1
bst = BST()
# bst.insert(Node('25','dear123'))
# bst.insert(Node('50','123'))
# bst.insert(Node('15','1234'))


# while True:
#     user_input = input("insert cmd : ")
#     if user_input == 'insert':
#         name_in = input("username : ")
#         pass_in = input("password : ")
#         bst.insert(Node(name_in,pass_in))
#         bst.printT()
#     elif user_input == 'find':
#         user_in = input("insert username : ")
#         print(bst.find(user_in))
#     elif user_input == 'remove':
#         user_in = input("remove username : ")
#         bst.remove(user_in)
#         bst.printT()
#     elif user_input == 'print':
#         print(bst.print())
#         user_input = input("inorder or preorder or postorder : ")
#         if user_input == "inorder":
#             print(bst.inorder(bst.root))
#         elif user_input == "preorder":
#             print(bst.preorder(bst.root))
#         elif user_input == "postorder":
#             print(bst.postorder(bst.root))
#     elif user_input == 'login':
#         user_input = input("username : ")
#         if bst.find(user_input):
#             login_count = 0
#             while login_count <= 3:
#                 pass_input = input("password : ")
#                 password = bst.find(user_input)
#                 if pass_input == password :
#                     print("login sucess")
#                     break
#                 else :
#                     login_count +=1
#                     print("attempt ",login_count,"/3")
#                     if login_count == 4 :
#                         bst.remove(user_input)
#                         print("login fail, deleting username")
#         else : 
#             print("username was not found")
#     elif user_input == 'count':
#         print(bst.count(bst.root))
        