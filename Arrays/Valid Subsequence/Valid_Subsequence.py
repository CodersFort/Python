#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:29:39 2020

@author: andrew
"""

'import Validate BST from Trees folder (had to add a "_" to call it)\
    I use Linux, this method works for me; your path call line 13 may be different'
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../../Trees/')
from Validate_BST import *
import random



'NodeinBST adapted from: https://www.geeksforgeeks.org/search-a-node-in-binary-tree/'
def NodeinBST(node, key):
 
    if (node == None): 
        return False
 
    if (node.value == key): 
        return True
 
    """ then recur on left sutree """
    res1 = NodeinBST(node.left, key) 
    # node found, no need to look further
    if res1:
        return True
 
    """ node is not found in left, 
    so recur on right subtree """
    res2 = NodeinBST(node.right, key) 
 
    return res2


'create a dictionary of the alphabet to assing numbers to letters'
import string as stringf
d={ch: n for n, ch in enumerate(stringf.ascii_lowercase)}


def Valid_Subseq(s,t):
    print('\n\nVALID SUBSEQUENCE')
    sl, tl = list(s), list(t)
    print("s: {}\nt: {}".format(s,t if len(tl) < 1000 \
                                else t[:100]+'.'*50+t[-100:]))
    print('\nIs "s" a subsequence of "t"?')
    
    'generate Tree of t (tree_t)'
    tree_t = BST( d[tl[0]] )
    for i in tl[1:]:
        tree_t.insert(d[i]) 
    
    'list of encoded letters of s'
    encoded_s = [ d[i] for i in sl]
    
    'loops over values of "s" until and if it finds a value not in tree_t'
    bool_func = True
    for vals in encoded_s:
        if not NodeinBST(tree_t, vals):
            print(False)
            bool_func = False
            break
    
    print(bool_func) if bool_func else None
    

'EXAMPLES'
'those in the readme'
s = "abc"
t = "ahbgdc"
Valid_Subseq(s,t)

s = "axc"
t = "ahbgdc"
Valid_Subseq(s,t)


'BONUS: t in its threshold of 10^4 letters'
inv_d = {v: k for k, v in d.items()}
s = "cyxz"
# s = "abs"
't is a string which has no "y" or "z" letters in it'
t = [inv_d[random.randint(0,23)] for i in range(10000)]
t=''.join(t)
Valid_Subseq(s,t)

