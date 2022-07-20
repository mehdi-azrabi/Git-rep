
subnet = '192.168.1.'
for n in range(1, 20):
    print(subnet + str(n))

device = ['R1', 'R2', 'SW1', 'SW2']
dc = ['dc01.com', 'dc02.com']
for i in device:
    for j in dc:
        print(i + '.' + j)


