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

number_trouble=[]
while i<len(m):
    j=0
    number=0
    while j<len(m[i]):
        number_trouble=[]
        proper_number=''
        if m[i][j]=='*':
            if m[i][j-1].isnumeric() or m[i][j+1].isnumeric() or m[i-1][j-1].isnumeric() or m[i-1][j].isnumeric() or m[i-1][j+1].isnumeric() or m[i+1][j-1].isnumeric() or m[i+1][j].isnumeric() or m[i+1][j+1].isnumeric():
                if m[i][j-1].isnumeric():
                    if m[i][j-2].isnumeric():
                        if m[i][j-3].isnumeric():
                            proper_number=''+m[i][j-3]+m[i][j-2]+m[i][j-1]
                            number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i][j-2]+m[i][j-1]
                            number_trouble.append(proper_number)
                    else:
                        proper_number=''+m[i][j-1]
                        number_trouble.append(proper_number)

                if m[i][j+1].isnumeric():
                    if m[i][j+2].isnumeric():
                        if m[i][j+3].isnumeric():
                            proper_number=''+m[i][j+1]+m[i][j+2]+m[i][j+3]
                            number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i][j+1]+m[i][j+2]
                            number_trouble.append(proper_number)
                    else:
                        proper_number=''+m[i][j+1]
                        number_trouble.append(proper_number)

                if m[i-1][j].isnumeric():
                    if m[i-1][j-1].isnumeric() and m[i-1][j+1].isnumeric():
                        proper_number=m[i-1][j-1] +m[i-1][j] +m[i-1][j+1]
                        number_trouble.append(proper_number)
                    else:
                        if m[i-1][j-1].isnumeric():
                            if m[i-1][j-2].isnumeric():
                                proper_number=''+m[i-1][j-2]+m[i-1][j-1]+m[i-1][j]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i-1][j-1]+m[i-1][j]
                                number_trouble.append(proper_number)    
                        if m[i-1][j+1].isnumeric():
                            if m[i-1][j+2].isnumeric():
                                proper_number=''+m[i-1][j]+m[i-1][j+1]+m[i-1][j+2]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i-1][j]+m[i-1][j+1]
                                number_trouble.append(proper_number)
                        if not m[i-1][j-1].isnumeric() and not m[i-1][j+1].isnumeric():
                            proper_number='' +m[i-1][j]
                            number_trouble.append(proper_number)
                if not m[i-1][j].isnumeric():
                    if m[i-1][j-1].isnumeric():
                        if m[i-1][j-2].isnumeric():
                            if m[i-1][j-3].isnumeric():
                                proper_number=m[i-1][j-3]+m[i-1][j-2]+m[i-1][j-1]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i-1][j-2]+m[i-1][j-1]
                                number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i-1][j-1]
                            number_trouble.append(proper_number)

                    if m[i-1][j+1].isnumeric():
                        if m[i-1][j+2].isnumeric():
                            if m[i-1][j+3].isnumeric():
                                proper_number=''+m[i-1][j+1]+m[i-1][j+2]+m[i-1][j+3]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i-1][j+1]+m[i-1][j+2]
                                number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i-1][j+1]
                            number_trouble.append(proper_number)

                    if not m[i-1][j-1].isnumeric() and not m[i-1][j+1].isnumeric():
                        final_result=final_result





                if m[i+1][j].isnumeric():
                    if m[i+1][j-1].isnumeric() and m[i+1][j+1].isnumeric():
                        proper_number=''+m[i+1][j-1] +m[i+1][j] +m[i+1][j+1]
                        number_trouble.append(proper_number)
                    else:
                        if m[i+1][j-1].isnumeric():
                            if m[i+1][j-2].isnumeric():
                                proper_number=''+m[i+1][j-2]+m[i+1][j-1]+m[i+1][j]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i+1][j-1]+m[i+1][j]
                                number_trouble.append(proper_number)    
                        if m[i+1][j+1].isnumeric():
                            if m[i+1][j+2].isnumeric():
                                proper_number=''+m[i+1][j]+m[i+1][j+1]+m[i+1][j+2]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i+1][j]+m[i+1][j+1]
                                number_trouble.append(proper_number)
                        if not m[i+1][j-1].isnumeric() and not m[i+1][j+1].isnumeric():
                            proper_number='' +m[i+1][j]
                            number_trouble.append(proper_number) 
                if not m[i+1][j].isnumeric():
                    if m[i+1][j-1].isnumeric():
                        if m[i+1][j-2].isnumeric():
                            if m[i+1][j-3].isnumeric():
                                proper_number=m[i+1][j-3]+m[i+1][j-2]+m[i+1][j-1]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i+1][j-2]+m[i+1][j-1]
                                number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i+1][j-1]
                            number_trouble.append(proper_number)

                    if m[i+1][j+1].isnumeric():
                        if m[i+1][j+2].isnumeric():
                            if m[i+1][j+3].isnumeric():
                                proper_number=''+m[i+1][j+1]+m[i+1][j+2]+m[i+1][j+3]
                                number_trouble.append(proper_number)
                            else:
                                proper_number=''+m[i+1][j+1]+m[i+1][j+2]
                                number_trouble.append(proper_number)
                        else:
                            proper_number=''+m[i+1][j+1]
                            number_trouble.append(proper_number)

                    if not m[i+1][j-1].isnumeric() and not m[i+1][j+1].isnumeric():
                        final_result=final_result





            else:
                final_result=final_result
        if len(number_trouble)>1:
            print(number_trouble)
            final_result=final_result+int(number_trouble[0])*int(number_trouble[1])
        j=j+1
    i+=1
print(final_result)
print('Koniec')