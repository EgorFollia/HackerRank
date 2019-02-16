def lists(n):
    l = []

    while (n > 0):
        s = input().split()
        cmd = s[0]
        args = s[1:]

        if (cmd == 'print'):
            print(l)
        else:
            eval('l.' + cmd + '(' + ','.join(args) + ')')
        
        n -= 1

if __name__ == '__main__':
    n = int(input())
    lists(n)
