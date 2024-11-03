start = (1)
end = (51)
for i in range(start,end):
    num = 0
    for l in range(2,i):
        if i % l == 0:
            num = 1
            break
    if (num == 0):
        print(i)