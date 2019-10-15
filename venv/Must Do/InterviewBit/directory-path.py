"""
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.
"""
class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        st = []
        new_A = A.split('/')
        new_A = filter(lambda x: x != '', new_A)
        i = 0
        while i < len(new_A):
            if new_A[i] == '.':
                pass
            elif new_A[i] == '..':
                st = st[:-1]
            else:
                st.append(new_A[i])
            i += 1
        s = '/'.join(st)
        return '/' + s