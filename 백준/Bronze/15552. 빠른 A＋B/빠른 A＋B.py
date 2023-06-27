import sys
z = int(input())

for i in range(z):
    num5, num6 = map(int,sys.stdin.readline().split())
    print(num5+num6)