def happiness(n, m):
    arr = input().split()
    A = set(map(str, input().split()))
    B = set(map(str, input().split()))

    total = 0

    for i in arr:
        if i in A:
            total += 1
        if i in B:
            total -= 1

    return total
    
if __name__ == '__main__':
    n, m = map(int, input().split())

    total = happiness(n, m)
    print(total)
