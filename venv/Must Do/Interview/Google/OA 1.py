"""
Question: You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?).
Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.
Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"
"""
def maxTime(s):
    r = ''
    for i in range(len(s)):
        if s[i] == '?':
            if i == 0:
                r = '2' if s[1] == '?' or int(s[1]) <= 3 else '1'
            elif i == 1:
                r = r + '3' if r[0] == '2' else r + '9'
            elif i == 3:
                r += '5'
            elif i == 4:
                r += '9'
        else:
            r += s[i]
    return r

print (maxTime('23:5?') )# 23:59
print (maxTime('2?:22')) # 23:22
print (maxTime('0?:??')) # 09:59
print (maxTime('1?:??')) # 19:59
print (maxTime('?4:??')) # 14:59
print (maxTime('?3:??') )# 23:59
print (maxTime('??:??')) # 23:59