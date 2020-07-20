import random
import timeit
import time

# start = timeit.timeit()
start = time.time()

rand_num1 = random.randrange(3,100000)
# print("rand_num1 : ", rand_num1)
count = rand_num1
# print("count : ", count)

i = 0
while i <= count:
    rand_num2 = random.randrange(3,100000)
    print(rand_num2)
    i = i + 1

# end = timeit.timeit()
end = time.time()

print('\n' + "[실행결과]")
print("[n = %d 개]" % count)
# print(end, "-", start, "= " + "경과시간 %s 초" % (end - start))
# print('\n' + "경과시간 %s 초" % (end - start))
result = round((end - start), 3)
print('\n' + "result =  %s (sec)" % result)

