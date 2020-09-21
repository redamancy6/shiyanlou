a = 0
while a <100:
    a = a + 1
    if (a % 7 == 0) or ('7' in str(a)):
        continue
    print(a)
