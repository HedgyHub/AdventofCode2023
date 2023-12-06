with open("toy.txt") as file_in:
	race_record=[]
	for line in file_in:
		line=line.replace('\n','')
		race_record.append(line)
races=race_record[0].split(' ')
time=[eval(i) for i in races]
racez=race_record[1].split(' ')
record=[eval(i) for i in racez]
print(time)
print(record)
i=0
ile=len(time)
ostateczna_liczba=1
while i<ile:

	czas=1
	dlugosc=time[i]
	na_ile_sposobow=0
	while czas<dlugosc:
		szybkosc=czas*(dlugosc-czas)
		if szybkosc>record[i]:
			na_ile_sposobow=na_ile_sposobow+1
		czas=czas+1
	print(na_ile_sposobow)
	ostateczna_liczba=ostateczna_liczba*na_ile_sposobow
	i=i+1
print(ostateczna_liczba)
	
