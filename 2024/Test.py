data = """
XXMASs.
MMAMX.
AA..A.
SSASSS
AX..A.
MX..M.
XX..X.
xxxxx
s"""
x = 0
y = 0
flag = 0
counter = 0
data = data.strip().split("\n")

lines = len(data)
columns = len(data[0]) if lines > 0 else 0
print(lines, columns)
