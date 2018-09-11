n,m = map(int, input().split())
a = list(map(int,input().split()))
s = 1
ans = 0

for i in a:
    if i >= s: ans += i-s
    else: ans += n - s + i
    s = i

print(ans)