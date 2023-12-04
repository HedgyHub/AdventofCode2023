r=0
b=0
g=0
place=0

def find_all(a_str, sub):
    start=0
    while True:
        start=a_str.find(sub, start)
        if start==-1: return
        yield start
        start+=len(sub) # use start += 1 to find overlapping matches


red=list(find_all('redzikred', 'red'))


final=0
with open('balls.txt') as file:
	row=1
	for line in list(file):
		r=0
		red=list(find_all(line, 'red')) # [0, 5, 10, 15]
		for i in red:
			temp=0
			place=i-2
			if line[place-1]=='1':
				temp=10
			temp=temp+int(line[place])
			if temp>int(r):
				r=temp

		print('Maximum red balls:' +str(r))

		b=0
		blue=list(find_all(line, 'blue')) # [0, 5, 10, 15]
		for i in blue:
			temp=0
			place=i-2
			if line[place-1]=='1':
				temp=10
			temp=temp+int(line[place])
			if temp>int(b):
				b=temp
		if b==100 or b==99:
			b=0
		print('Maximum blue balls:' +str(b))

		g=0
		green=list(find_all(line, 'green')) # [0, 5, 10, 15]
		for i in green:
			temp=0
			place=i-2
			if line[place-1]=='1':
				temp=10
			temp=temp+int(line[place])
			if temp>int(g):
				g=temp


		print(' Maximum green balls:' +str(g))
		print('Row: ' +str(row) +' ' +str(r*b*g))
		final=final+r*b*g
		row=row+1


print(str(final))









