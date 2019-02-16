if __name__ == '__main__':
    _, M = int(input()), set(map(int, input().split()))
    _, N = int(input()), set(map(int, input().split()))

    print(*sorted(M ^ N, key = int), sep = '\n')


