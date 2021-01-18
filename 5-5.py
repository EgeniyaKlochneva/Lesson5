with open('text_five.txt', 'w') as f:
    data = f.write('5 7 89 41 55 1 33')
with open('text_five.txt', 'r') as f:
        s = f.readline()
        s = list(map(int, s.split()))
with open('text_five.txt', 'w') as f:
        f.write(str(s))
print(sum(s))

