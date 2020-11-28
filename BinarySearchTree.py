#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.val = key 


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None: 
                root.right = node
            else:
                insert(root.right, node) 
        else: 
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node) 

def minValueNode( node): 
    current = node 
    while(current.left is not None): 
        current = current.left  
  
    return current  
  

def deleteNode(root, key): 

    if root is None: 
        return root  
    if key < root.val: 
        root.left = deleteNode(root.left, key) 
    elif(key > root.val): 
        root.right = deleteNode(root.right, key) 
    else: 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 
        root.val = temp.val 
        root.right = deleteNode(root.right , temp.val) 
  
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

b = 0
while True: 
    
    if b == 0 :
        choice = input("Insert/Exit (1/2): ")

        if choice == "1" :
            val = int(input("Enter number of inserting value: "))
            a = int(input("Insert the root: "))
            r = Node(a)
            i = 1
            while i < val: 
                no = int(input("Enter your value: "))
                insert(r, Node(no))
                inorder(r)
                i += 1
        else:
            break
    else:
        choice = input("Delete/Insert/Exit (0/1/2): ")

        if choice == "1" :
            val = int(input("Enter number of inserting value: "))
            a = int(input("Insert the root: "))
            r = Node(a)
            i = 1
            while i < val:
                no = int(input("Enter your value: "))
                insert(r, Node(no))
                inorder(r)
                i += 1
        elif choice == "0":
            val = int(input("Enter number to delete: "))
            if val == a:
                print("    Cannot delete root!!  ")
            else:
                root = deleteNode(r, val)
                inorder(r)
        else:
            break
    b += 1 


# In[ ]:




