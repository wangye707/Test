result = 0
n = int(input())
a = list(input().split())
b = list(input().split())
a.sort(reverse=True)
b.sort(reverse=True)
c = []
for i in range(n):
    if a[i] >= b[0]:
        c.append(b.pop())
    else:
        c.append(b.pop())
for i in range(n):
    if a[i] <c[i]:
        result = result -1
    elif a[i] >c[i]:
        result = result + 1
    else:
        continue
print(result)