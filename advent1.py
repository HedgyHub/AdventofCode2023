#open advent file
a=0
b=0
c=0
d=0
with open('numbers.txt') as file:
	for line in list(file):
		print('Full line: ' +line)
		lowest=len(line)+1
		highest=-1
		lowest_num=0
		highest_num=0
		#dict=['one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9]
		#for each i in dict[i]
		if 'one' in line:
			if line.find('one')<lowest:
				lowest_num=1
				lowest=line.find('one')
			if line.rfind('one')>highest:
				highest_num=1
				highest=line.rfind('one')

		if 'two' in line:
			if line.find('two')<lowest:
				lowest_num=2
				lowest=line.find('two')
			if line.rfind('two')>highest:
				highest_num=2
				highest=line.rfind('two')

		if 'three' in line:
			if line.find('three')<lowest:
				lowest_num=3
				lowest=line.find('three')
			if line.rfind('three')>highest:
				highest_num=3
				highest=line.rfind('three')

		if 'four' in line:
			if line.find('four')<lowest:
				lowest_num=4
				lowest=line.find('four')
			if line.rfind('four')>highest:
				highest_num=4
				highest=line.rfind('four')

		if 'five' in line:
			if line.find('five')<lowest:
				lowest_num=5
				lowest=line.find('five')
			if line.rfind('five')>highest:
				highest_num=5
				highest=line.rfind('five')

		if 'six' in line:
			if line.find('six')<lowest:
				lowest_num=6
				lowest=line.find('six')
			if line.rfind('six')>highest:
				highest_num=6
				highest=line.rfind('six')

		if 'seven' in line:
			if line.find('seven')<lowest:
				lowest_num=7
				lowest=line.find('seven')
			if line.rfind('seven')>highest:
				highest_num=7
				highest=line.rfind('seven')

		if 'eight' in line:
			if line.find('eight')<lowest:
				lowest_num=8
				lowest=line.find('eight')
			if line.rfind('eight')>highest:
				highest_num=8
				highest=line.rfind('eight')

		if 'nine' in line:
			if line.find('nine')<lowest:
				lowest_num=9
				lowest=line.find('nine')
			if line.rfind('nine')>highest:
				highest_num=9
				highest=line.rfind('nine')
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


