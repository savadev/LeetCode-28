# Minimum Path Sum

## Difficulty
Medium

## Question
<p>Given a <em>m</em> x <em>n</em> grid filled with non-negative numbers, find a path from top left to bottom right which <em>minimizes</em> the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; [1,3,1],
  [1,5,1],
  [4,2,1]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1&rarr;3&rarr;1&rarr;1&rarr;1 minimizes the sum.
</pre>


## Solution
### python
```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        for i in range(1, h):
            grid[i][0] += grid[i-1][0]
        for i in range(1, w):
            grid[0][i] += grid[0][i-1]
        for i in range(1, h):
            for j in range(1, w):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

```
### python3
```python3
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        for i in range(1, h):
            grid[i][0] += grid[i-1][0]
        for i in range(1, w):
            grid[0][i] += grid[0][i-1]
        for i in range(1, h):
            for j in range(1, w):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
```

## Author
EINDEX