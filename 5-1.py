with open("text.txt", 'w') as f:
    while True:
        s = input("Введите данные: ")
        if s == '': break
        f.write(s + '\n')
