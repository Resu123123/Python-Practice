word = 'hello dear'
print(word.title())
print(word.capitalize())
print(word.upper())
print(word.lower())

def solve(s):
    word = s.split(' ')
    print(word)
    word1 = (i.capitalize() for i in word)
    print(word1)
    return ' '.join(word1)

s = input()
result = solve(s)
print(result)