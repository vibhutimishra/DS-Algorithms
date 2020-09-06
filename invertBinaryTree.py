class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self,root):
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root
        root.left=self.invertTree(root.left)
        root.right=self.invertTree(root.right)
        temp=(root.left)
        (root.left)=(root.right)
        (root.right)=temp

        return root
    def createBinaryTree(self,arr,root,i,n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp

            # insert left child
            root.left = self.createBinaryTree(arr, root.left,
                                         2 * i + 1, n)
            # insert right child
            root.right = self.createBinaryTree(arr, root.right,
                                          2 * i + 2, n)
        return root
    def print(self,root):
        if root!=None:
            self.print(root.left)
            print(root.val,end=" ")
            self.print(root.right)

obj=Solution()
arr=[4,2,7,1,3,6,9]
l=len(arr)
root=None
root=obj.createBinaryTree(arr,root,0,l)
root=obj.invertTree(root)
obj.print(root)
