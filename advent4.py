with open("lottery.txt") as file_in:
	m=[]
	for line in file_in:
		line=''+line[10:]
		line=line.replace('\n','')
		m.append(line)

	winning_numbers=[]
	lottery_ticket=[]
	counter_pairs=0
	for i in m:
		j=0
		winning_numbers.append('')
		while i[j]!='|':
			winning_numbers[counter_pairs]=winning_numbers[counter_pairs]+i[j]
			j=j+1
		j=j+1
		lottery_ticket.append('')
		while j<len(i):
			lottery_ticket[counter_pairs]=lottery_ticket[counter_pairs]+i[j]
			j=j+1
		counter_pairs=counter_pairs+1

	j=0
	final_answer=0
	number_of_scratches=[]
	k=0
	while k<len(winning_numbers):
		number=1
		number_of_scratches.append(number)
		k=k+1

	while j<len(winning_numbers):
		a=winning_numbers[j].replace('  ',' ')
		b=lottery_ticket[j].replace('  ',' ')
		if a[0]==' ':
			a=''+a[1:]
		if b[0]==' ':
			b=''+b[1:]
		a=a[0:len(a)-1]
		x=a.split(' ')
		y=b.split(' ')
		z=set(x)&set(y)
		print(len(z))
		to_which=len(z)+j
		while to_which>j:
			if to_which>len(number_of_scratches)-1:
				to_which=to_which-1
			else:
				number_of_scratches[to_which]=number_of_scratches[to_which]+1*number_of_scratches[j]
				to_which=to_which-1
		#print(z)
		#print(len(z))
		j=j+1
	final_answer=0
	k=0
	while k<len(number_of_scratches):
		final_answer=final_answer+number_of_scratches[k]
		k=k+1
	print(number_of_scratches)
	print(final_answer)







