with open("matrix.txt") as file_in:
    m = []
    for line in file_in:
        m.append(line)
m.insert(0,'............................................................................................................................................')
m.insert(len(m),'............................................................................................................................................')
for i in m:
    i='.'+i
    i=i.replace('\n','.')

for line in range(0, len(m)):
    m[line]='.'+m[line]
    m[line]=m[line].replace("\n",".")


final_result=0


number=0
i=0
print(m)
while i<len(m):
    j=0
    number=0
    while j<len(m[i]):
        if m[i][j].isnumeric():
            if m[i][j+1].isnumeric() and m[i][j+2].isnumeric():
                if m[i][j-1]!='.' or m[i][j+3]!='.' or m[i-1][j-1]!='.' or m[i-1][j]!='.' or m[i-1][j+1]!='.' or m[i-1][j+2]!='.' or m[i-1][j+3]!='.' or m[i+1][j-1]!='.' or m[i+1][j]!='.' or m[i+1][j+1]!='.' or m[i+1][j+2]!='.' or m[i+1][j+3]!='.':
                    number=int(m[i][j])*100+int(m[i][j+1])*10+int(m[i][j+2])
                    print(number)
                    final_result=final_result+number
                j=j+3
            else:
                if m[i][j+1].isnumeric():
                    if m[i][j-1]!='.' or m[i][j+2]!='.' or m[i-1][j-1]!='.' or m[i-1][j]!='.' or m[i-1][j+1]!='.' or m[i-1][j+2]!='.' or m[i+1][j-1]!='.' or m[i+1][j]!='.' or m[i+1][j+1]!='.' or m[i+1][j+2]!='.':
                        number=int(m[i][j])*10+int(m[i][j+1])
                        print(number)
                        final_result=final_result+number
                    j=j+2
                else:
                    if m[i][j-1]!='.' or m[i][j+1]!='.' or m[i-1][j-1]!='.' or m[i-1][j]!='.' or m[i-1][j+1]!='.' or m[i+1][j-1]!='.' or m[i+1][j]!='.' or m[i+1][j+1]!='.':
                        number=int(m[i][j])
                        print(number)
                        final_result=final_result+number
                    j=j+1
        else:
            j=j+1
    i+=1
print(final_result)
print('Koniec')