names = ['1.txt', '2.txt', '3.txt']

lst = []

for name in names:
    original_text = [line.strip() for line in open(name, 'r').readlines()]
    text = [name, str(len(original_text))] + original_text
    lst.append(text)

sortd = sorted(lst, key=lambda x:len(x))

out = ''
for lines in sortd:
    out += '\n'.join(lines) + '\n'

open('result.txt', 'w').write(out)
