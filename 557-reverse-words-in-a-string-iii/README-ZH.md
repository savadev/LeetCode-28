# Reverse Words in a String III

## Difficulty
Easy

## Question
<p>Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "Let's take LeetCode contest"
<b>Output:</b> "s'teL ekat edoCteeL tsetnoc"
</pre>
</p>

<p><b>Note:</b>
In the string, each word is separated by single space and there will not be any extra space in the string.
</p>

## Solution
### python
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(x[::-1] for x in s.split())
        


```

## Author
EINDEX