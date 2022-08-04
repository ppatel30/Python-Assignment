with open('doc.txt','r') as f:
    lineText = f.readlines()
for i in lineText:
    if ((len(i)-1)%2 == 0):
        print(i[:-1])
        