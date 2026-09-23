# What's Your Name?

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: 

>Hello `firstname` `lastname`! You just delved into python.

**Function Description**   

Complete the *print_full_name* function in the editor below.  

*print_full_name* has the following parameters:  

- *string first:* the first name   
- *string last:* the last name  

**Prints**   

- *string:* 'Hello $firstname$ $lastname$! You just delved into python' where $firstname$ and $lastname$ are replaced with $first$ and $last$. 

**Input Format**

The first line contains the first name, and the second line contains the last name.  

**Constraints**

The length of the first and last names are each &le; $10$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T16:58:07.885Z  

```py

# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
        print(f"Hello {first} {last}! You just delved into python.")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/whats-your-name/problem)