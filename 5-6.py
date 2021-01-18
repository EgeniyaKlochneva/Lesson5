s = {}
with open('text_six.txt', 'r') as f:
    for line in f:
        #subj, lec, pract, lab = line.split()
        print(line.split())
        for i in line:
            s = i[1] + i[3] + i[5]
print(f'{s}')

