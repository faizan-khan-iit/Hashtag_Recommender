file = open("Desktop/temp/a.txt", 'r')
w = open("Desktop/temp/final.txt", 'w')
ls = list()
for f in file:
    ls.append(str(f)[:-1])
    # print(f)

ls = set(ls)

for i in ls:
    w.write(i + "\n")
    
file.close()
w.close()