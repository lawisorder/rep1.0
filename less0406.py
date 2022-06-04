n = int(input())
sp = []
for i in range(n):
    num = input()
    if num not in sp:
        sp.append(num)
print(*sp, sep='***')

a, b, c = 1, 2, 3
