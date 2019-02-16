def merge_the_tools(string, k):
    div = len(string) // k

    for i in range(div):
        u = ''

        for s in string[i * k : i * k + k]:
            if s not in u:
                u += s
        
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
