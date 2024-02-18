sayı=8
for yüz in range(0,2):
    for elli in range(0,4):
        for yirmi in range(0,10):
            for on in range(0,20):
                for beş in range(0,40):
                    for iki in range(0,100):
                        for bir in range(0,200):
                            if 100*yüz+50*elli+20*yirmi+10*on+5*beş+2*iki+bir==200:
                                sayı+=1
print(sayı)                                

