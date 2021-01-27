with open('text_five.txt', 'w+', encoding='utf-8') as f:
    data = f.write('5 7 89 41 55 1 33')
    f.seek(0)

    print(sum(map(int, f.readline().split())))
