import math
import time

suffixes = ["K", "M", "B", "T", "q", "Q", "s", "S", "O", "N", "d"]
increment = 999999999

# num = [0]
# i = 0
#
# while True:
#     if num[i] >= 1000:
#         i+=1
#         num.append(0)
#     num[i] += increment
#     print(str(num[i]) +
#     "\tIndex:" + str(i)
#     , end='\r')

a = 0
while True:
    a+=increment
    print(str(a)[0:(len(str(a))%3) if (len(str(a))%3)!=0 else 3] +
            "." + str(a)[((len(str(a))%3) if (len(str(a))%3)!=0 else 3):5] +
            suffixes[math.ceil((len(str(a))-3)/3)] +
            "\tlen(a)%3:" + str(len(str(a))%3) +
            "\ta:" + str(a) +
            "\tint:" + str(int((len(str(a))-3)/3)) +
            "\tfloat:" + str((len(str(a))-3)/3) +
            "\tlen:" + str(len(str(a)))
            , end='\r')
