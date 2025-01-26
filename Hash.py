if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    x = list(integer_list)
    y = tuple(x)
    z = hash(y)
    print(z)