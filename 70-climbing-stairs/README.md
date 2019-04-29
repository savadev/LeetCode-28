# Climbing Stairs

## Difficulty
Easy

## Question
<p>You are climbing a stair case. It takes <em>n</em> steps to reach to the top.</p>

<p>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</p>

<p><strong>Note:</strong> Given <em>n</em> will be a positive integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>


## Solution
### python
```python
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b

```
### python3
```python3
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return b

```

## Author
EINDEX