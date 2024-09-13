n = int(input())
m = int(input())
t = int(input()) + n * 60 + m
n = (t // 60) % 24
m = t % 60
print(f'{n:0>2}:{m:0>2}')
