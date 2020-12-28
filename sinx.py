A1 = [0,2,4,6,8,10,12,14,16,18,20]
A2 = [0,3,6,9,12,15,18]
A3 = [0,1,2]
A4 = [0,1]
c = 0
for i in A1:
    for j in A2:
        for k in A3:
            for t in A4:
                if i+j+k+t == 20:
                    c += 1



print(c)                    
