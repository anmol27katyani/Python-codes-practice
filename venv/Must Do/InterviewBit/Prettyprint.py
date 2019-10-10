def prettyPrint(self, A):
    return [[1 + max(abs(i), abs(j)) for j in range(-A + 1, A)] for i in range(-A + 1, A)]