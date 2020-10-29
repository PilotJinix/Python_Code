m_a = [[2, 2, 2],
       [2, 7, 2],
       [2, 2, 2]
       ]
m_b = [[1, 1, 2],
       [1, 1, 1],
       [1, 1, 1]
       ]

isi   = []
m_c   = []
hasil = 0
 
for i in range( len(m_a)):
    for j in range(len(m_a[0])):
        for k in range(len(m_a)):
            hasil += m_a[i][k] * m_b[j][k]
        isi.append(hasil)
        hasil = 0
    m_c.append(isi)
    isi=[]

for i in range(len(m_c)):
    for j in range(len(m_c[0])):
        print (m_c[i][j], end=' ')
    print()
