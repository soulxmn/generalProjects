class BinaryTree:
    def __init__(self, rootval):
        self.key = rootval
        self.left = None
        self.right = None
            
    def getRootValue(self):
        return self.key
    
    def getRightChild(self):
        return self.right
    
    def getLeftChild(self):
        return self.left
    
    def insertRightChild(self, val):
        t = BinaryTree(val)
        if self.right == None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def insertLeftChild(self, val):
        t = BinaryTree(val)
        if self.left == None:
            self.left = t
        else:
            t.left = self.left
            self.left = t
    
    def setLeftSubtree (self, t):
        self.left = t
  
    def setRightSubtree (self, t):
        self.right = t
              