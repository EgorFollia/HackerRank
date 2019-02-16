from numpy import *

n, m = map(int,input().split())
arr = array([input().split() for _ in range(n)], int)

print(arr.transpose())
print(arr.flatten())
