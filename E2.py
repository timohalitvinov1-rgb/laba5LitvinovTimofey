n = int(input())
otr = 0
pol = 0
sotr = 0
spol = 0
for i in range(n):
    i = int(input())
    if i < 0 and i % 2 == 0:
        otr += 1
        sotr += i
    elif i >= 0 and i % 2 != 0:
        pol += 1
        spol += i
print((spol/pol) -(sotr/otr))
