"""
Question 1
(a)
s.find("N")
s.index("N")
(b) "PYTHON"
(c) "PYT"
(d) "PTO"
(e) s[:4]
(f) s[3::2]
(g) s[-1::-2]
"""


# Question 2
def fiblist(n):
    tmp_list = []
    for x in range(1, n + 1):
        if x == 1:
            tmp_list.append(1)
        elif x == 2:
            tmp_list.append(1)
        else:
            tmp_list.append(tmp_list[x - 2] + tmp_list[x - 3])
    return tmp_list


# Question 3
def ispartitionable(s):
    is_partitionable = False
    for x in range(1, len(s)):
        if sum(s[:x]) == sum(s[x:]):
            is_partitionable = True
            break
    return is_partitionable


# Question 4
def identity_matrix(n):
    matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    return matrix


def alternate_identity_matrix(n):
    m = [[0] * x + [1] + [0] * (n - x - 1) for x in range(n)]
    return m


# Question 5
m = [[1, 0, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 3, 0, 0], [1, 2, 3, 4, 0], [1, 2, 3, 4, 5]]
sums = [sum(x) for x in m]


# Question 6
def vowelcount(s):
    s = s.lower()
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")


# Question 7
def listfromcsv(s):
    return [x.split(",") for x in s.splitlines()]
