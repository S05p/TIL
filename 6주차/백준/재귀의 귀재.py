def recursion(s, l, r, t):
    if l >= r: 
        t += 1
        return 1, t
    elif s[l] != s[r]: 
        t += 1
        return 0, t
    else: 
        t += 1
        return recursion(s, l+1, r-1, t)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

N = int(input())

for i in range(N):
    n = str(input())
    print(*isPalindrome(n))