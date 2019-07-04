import time
start = time.clock()
sum = 0
for i in range(100000000):
    sum += i
print(sum)
elapsed = (time.clock() - start)
print("Time used:",elapsed)