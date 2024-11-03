sum_even = 0
sum_odd = 0
for i in range(1,6):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("sum of even",sum_even)
print("sum of odd",sum_odd)
