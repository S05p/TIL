# h, m =map(int,input().split())

# m_1 = m - 45

# if m_1<=0:
#     m_2 = m_1 + 60 
#     h_1 = h - 1
# else:
#     m_2 = m_1
#     h_1 = h

# if h_1<=0:
#     h_2 = h_1 + 24
# else:
#     h_2 = h_1
    
# print(h_2,m_2)

H,M = map(int,input().split())
if M > 44:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1,M+15)
else:
    print(23,M+15)