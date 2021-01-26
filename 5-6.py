subj = {}
with open('text_six.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        num_sum = sum(map(int, "".join([i for i in stats if i == '' or ('0' <= i <= '9')])))
    print(f'Общее количество часов по предмету - \n {subj}')

