if __name__ == '__main__':
    N = int(input())
    Liste = []
    for i in range(N):
        command = (input().split)
        if command[0] == "insert":
            Liste.insert(int(command[1]),int(command[2]))
        elif command[0] == "remove":
            Liste.remove(int(command[1]))
        elif command[0] == "append":
            Liste.append(int(command[1]))
        elif command[0] == "sort":
            Liste.sort()
        elif command[0] == "pop":
            Liste.pop()
        elif command[0] == "reverse":
            Liste.reverse
        elif command[0] == "print":
            print(Liste) 