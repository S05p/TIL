h,m=map(int,input().split())
t = int(input())
m_1 = m+t
if m_1>=60:
    m_2 = m_1%60
    h_1 = h + (m_1//60)
    if h_1>=24:
        h_1 = h_1%24
else:
    h_1 = h
    m_2 = m_1
    
print(h_1,m_2)