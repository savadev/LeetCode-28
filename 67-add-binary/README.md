# Add Binary

## Difficulty
Easy

## Question
<p>Given two binary strings, return their sum (also a binary string).</p>

<p>The input strings are both <strong>non-empty</strong> and contains only characters <code>1</code> or&nbsp;<code>0</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;11&quot;, b = &quot;1&quot;
<strong>Output:</strong> &quot;100&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = &quot;1010&quot;, b = &quot;1011&quot;
<strong>Output:</strong> &quot;10101&quot;</pre>


## Solution
### python
```python
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2))).replace('0b', '')



```
### python3
```python3
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2))).replace('0b', '')


```

## Author
EINDEX