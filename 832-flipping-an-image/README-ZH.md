# Flipping an Image

## Difficulty
Easy

## Question
<p>Given a binary matrix <code>A</code>, we want to flip the image horizontally, then invert it, and return the resulting image.</p>

<p>To flip an image horizontally means that each row of the image is reversed.&nbsp; For example, flipping&nbsp;<code>[1, 1, 0]</code>&nbsp;horizontally results in&nbsp;<code>[0, 1, 1]</code>.</p>

<p>To invert an image means&nbsp;that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.&nbsp;For example, inverting&nbsp;<code>[0, 1, 1]</code>&nbsp;results in&nbsp;<code>[1, 0, 0]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0],[1,0,1],[0,0,0]]
<strong>Output: </strong>[[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output: </strong>[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= A.length = A[0].length &lt;= 20</code></li>
	<li><code>0 &lt;= A[i][j]<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;&lt;=&nbsp;</font>1</code></li>
</ul>


## Solution
### python
```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if i==1 else 1 for i in line[::-1]] for line in A]
        

```
### python3
```python3
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if i==1 else 1 for i in line[::-1]] for line in A]
        
```

## Author
EINDEX