"""
https://practice.geeksforgeeks.org/contest/interview-series-google/problems/
Input:
A = "abcd"
B = "cdabcdab"
Output:
3
Explanation:
Repeating A three times (“abcdabcdabcd”),
B is a substring of it. B is not a substring
of A when it is repeated less than 3 times.
Input:
A = "ab"
B = "cab"
Output :
-1
Explanation:
No matter how many times we repeat A, we can't
get a string such that B is a substring of it.



Enter first string: abcde
Enter second string: ea
2
"""

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

min_repeats = 1

if len(str2) < len(str1):
    if str2 in str1:
        print(min_repeats)
    else:
        print(min_repeats + 1)
else:
    while len(str2) >= len(str1):
        min_repeats += 1
        str1 = str1 + str1
        if str2 in str1:
            print(min_repeats)
        elif len(str2) < len(str1):
            print("-1")
