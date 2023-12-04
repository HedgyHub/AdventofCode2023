#open advent file
a=0
b=0
c=0
d=0
with open('message.txt') as file:
	for line in list(file):
		print('Full line: ' +line)
		lowest=len(line)+1
		highest=-1
		lowest_num=0
		highest_num=0
		dict={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
		for key in dict:
			if key in line:
				if line.find(key)<lowest:
					lowest_num=dict[key]
					lowest=line.find(key)
				if line.rfind(key)>highest:
					highest_num=dict[key]
					highest=line.rfind(key)

		a=0
		a_position=len(line)+1
		b=0
		b_position=-1
		d=0
		i=0
		j=len(line)-1
		while i<len(line):
			if line[i].isdigit():
				a=int(line[i])
				a_position=i
				a*=10
				break
			i+=1
		while j>-1:
			if line[j].isdigit():
				b_position=j
				b=int(line[j])
				break
			j-=1
		print('Lowest written: ' +str(lowest_num))
		print('Highest written: '+str(highest_num))
		print('Lowest num: ' +str(a))
		print('Highest num:' +str(b))
		if a_position>lowest:
			a=lowest_num*10

		if b_position<highest:
			b=highest_num
		c=c+a+b
		d=a+b
		print('Value: ' +str(d))
		print(c)


