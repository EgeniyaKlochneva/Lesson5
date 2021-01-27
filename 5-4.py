rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_four_new.txt', 'w+', encoding='utf-8') as new_f:
    with open('text_four.txt', 'r', encoding='utf-8') as f:
        for i in f:
            i = i.split(' ', 1)
            new_file.append(rus[i[0]] + '  ' + i[1])
        print(new_file)
        new_f.writelines(new_file)
