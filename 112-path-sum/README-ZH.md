# Path Sum

## Difficulty
Easy

## Question
<p>Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given the below binary tree and <code>sum = 22</code>,</p>

<pre>
      <strong>5</strong>
     <strong>/</strong> \
    <strong>4</strong>   8
   <strong>/</strong>   / \
  <strong>11</strong>  13  4
 /  <strong>\</strong>      \
7    <strong>2</strong>      1
</pre>

<p>return true, as there exist a root-to-leaf path <code>5-&gt;4-&gt;11-&gt;2</code> which sum is 22.</p>


## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (44.03%)
# Total Accepted:    10.4K
# Total Submissions: 23.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
#
#
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if sum-root.val == 0:
            if not root.right and not root.left:
                return True

        if self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val):
            return True
        else:
            return False


```

## Author
EINDEX