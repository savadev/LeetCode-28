# Add Digits

## Difficulty
Easy

## Question
<p>Given a non-negative integer <code>num</code>, repeatedly add all its digits until the result has only one digit.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>38</code>
<strong>Output:</strong> 2 
<strong>Explanation: </strong>The process is like: <code>3 + 8 = 11</code>, <code>1 + 1 = 2</code>. 
&nbsp;            Since <code>2</code> has only one digit, return it.
</pre>

<p><b>Follow up:</b><br />
Could you do it without any loop/recursion in O(1) runtime?</p>

## Solution
### c
```c
int addDigits(int num) {
    if (num == 0)
        return num;
    return 1+(num-1)%9;
}


```
### python
```python
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        return 1+(num-1)%9
```

## Author
EINDEX