n = str(input())

n_table = n.maketrans({
    'C':'',
    'A':'',
    'M':'',
    'B':'',
    'R':'',
    'I':'',
    'D':'',
    'G':'',
    'E':''})

print(n.translate(n_table))


