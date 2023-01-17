a, b = map(str,input().split())

a = a[2] + a[1] + a[0]

b = b[2] + b[1] + b[0]

new_a = int(a)
new_b = int(b)


if new_a > new_b:
    print(new_a)
else:
    print(new_b)