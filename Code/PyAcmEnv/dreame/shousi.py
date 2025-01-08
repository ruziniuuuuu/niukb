"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

class Tree:
    def __init__(self, value: int=0, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    

def func(p: Tree, q: Tree):

    if not p and not q:
        return True

    if not p and q:
        return False
    
    if not q and p:
        return False

    if p.value == q.value:
        return func(p.left, q.left) and func(p.right, q.right)
    else:
        return False
    


if __name__ == '__main__':
    p_l = Tree(1)
    p_r = Tree(2)
    p = Tree(0, p_l, p_r)
    q_l = Tree(1)
    q_r = Tree(2)
    q = Tree(0, q_l, q_r)
    print(func(p, q))