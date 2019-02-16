from __future__ import division

def average(arr):
  arr = set(arr)
  return sum(arr)/len(arr)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
