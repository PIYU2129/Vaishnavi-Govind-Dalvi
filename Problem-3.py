a = int(input("Enter a Number:"))
if a % 2 == 0:
    limit = a -1
else:
    limit = a
series = [2*i +1 for i in range(limit)]
print(",".join(map(str,series)))
