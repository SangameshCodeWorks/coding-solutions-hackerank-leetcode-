# Find a string

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

**NOTE:** String letters are case-sensitive.

**Input Format**  

The first line of input contains the original string. The next line contains the substring.

**Constraints**  

$1 \le len(string) \le 200$  
Each character in the string is an *ascii* character. 

**Output Format** 

Output the integer number indicating the total number of occurrences of the substring in the original string. 

**Sample Input**

	ABCDCDC
	CDC

**Sample Output**

	2

**Concept**
 
There are a couple of new concepts:  
In Python, the length of a string is found by the function `len(s)`, where $s$ is the string.  
To traverse through the length of a string, use a *for* loop:  

    for i in range(0, len(s)):
        print (s[i])

A range function is used to loop over some length: 

    range (0, 5)

Here, the range loops over $0$ to $4$. $5$ is excluded.

**Input Format**

 

**Constraints**

-

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T17:20:00.815Z  

```py
def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        s2=string[i:i+len(sub_string)]
        if s2==sub_string:
            count=count+1
        else:
            count=count+0
    return count
            


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/find-a-string/problem)