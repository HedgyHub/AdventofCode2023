def assign(number,assigned_number,amount):
	i=0
	length=len(number)
	first_number_a=[]
	first_number_b=[]
	final_number_a=[]
	final_number_b=[]
	while i<length:
		first_number_a.append(int(number[i]))
		first_number_b.append(int(number[i])+amount[i]-1)
		final_number_a.append(int(assigned_number[i]))
		final_number_b.append(int(assigned_number[i])+amount[i]-1)
		i=i+1
	return first_number_a,first_number_b,final_number_a,final_number_b

def transform(m):
	result=[]
	designation=[]
	counter=[]
	for i in m:
		x=i.split(' ')
		result.append(int(x[0]))
		designation.append(int(x[1]))
		counter.append(int(x[2]))
	return result,designation,counter

def new_seed(seed,first_a,first_b,second_a,second_b):
	i=0
	j=len(second_a)
	check_position=0
	while i<j:
		if seed>=second_a[i] and seed<=second_b[i]:
			check_position=seed-second_a[i]
			seed=first_a[i]+check_position
			break			
		else:
			seed=seed
		i=i+1
	return seed



with open("seeds.txt") as file_in:
	seedy=[]
	for line in file_in:
		line=line.replace('\n','')
		seedy.append(line)
seedz=seedy[0].split(' ')
seeds=[eval(i) for i in seedz]
seedscopy=[]
seedsbig=seeds[0]+seeds[1]
i=seeds[0]
while i<seedsbig:
	seedscopy.append(i)
	i=+1
seeds=seedscopy
print(seeds)

with open("seed-soil.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)


result_s_s,designation_s_s,counter_s_s=transform(m)

first_no_ss_a,first_no_ss_b,second_no_ss_a,second_no_ss_b=assign(result_s_s,designation_s_s,counter_s_s)



with open("soil-fertilizer.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_s_f,designation_s_f,counter_s_f=transform(m)

first_no_sf_a,first_no_sf_b,second_no_sf_a,second_no_sf_b=assign(result_s_f,designation_s_f,counter_s_f)


with open("fertilizer-water.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_f_w,designation_f_w,counter_f_w=transform(m)

first_no_fw_a,first_no_fw_b,second_no_fw_a,second_no_fw_b=assign(result_f_w,designation_f_w,counter_f_w)

#print(first_no_fw_a,first_no_fw_b,second_no_fw_a,second_no_fw_b)

with open("water-light.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_w_l,designation_w_l,counter_w_l=transform(m)

first_no_wl_a,first_no_wl_b,second_no_wl_a,second_no_wl_b=assign(result_w_l,designation_w_l,counter_w_l)


with open("light-temperature.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_l_t,designation_l_t,counter_l_t=transform(m)

first_no_lt_a,first_no_lt_b,second_no_lt_a,second_no_lt_b=assign(result_l_t,designation_l_t,counter_l_t)

with open("temperature-humidity.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_t_h,designation_t_h,counter_t_h=transform(m)

first_no_th_a,first_no_th_b,second_no_th_a,second_no_th_b=assign(result_t_h,designation_t_h,counter_t_h)


with open("humidity-location.txt") as file_in:
	m=[]
	for line in file_in:
		line=line.replace('\n','')
		m.append(line)

result_h_l,designation_h_l,counter_h_l=transform(m)

first_no_hl_a,first_no_hl_b,second_no_hl_a,second_no_hl_b=assign(result_h_l,designation_h_l,counter_h_l)


soils=[]
fertilizers=[]
waters=[]
lights=[]
temperatures=[]
humiditys=[]
locations=[]



i=0
print(seeds)
print(first_no_ss_a,first_no_ss_b,second_no_ss_a,second_no_ss_b)
for seed in seeds:
	sprout=new_seed(seed,first_no_ss_a,first_no_ss_b,second_no_ss_a,second_no_ss_b)
	soils.append(sprout)
print('Problem starts here:')
print(soils)
print(first_no_sf_a,first_no_sf_b,second_no_sf_a,second_no_sf_b)
for soil in soils:
	sprout=new_seed(soil,first_no_sf_a,first_no_sf_b,second_no_sf_a,second_no_sf_b)
	fertilizers.append(sprout)
print('Problem ends here:')
print(fertilizers)
print(first_no_fw_a,first_no_fw_b,second_no_fw_a,second_no_fw_b)
for fertilizer in fertilizers:
	sprout=new_seed(fertilizer,first_no_fw_a,first_no_fw_b,second_no_fw_a,second_no_fw_b)
	waters.append(sprout)
print(waters)
for water in waters:
	sprout=new_seed(water,first_no_wl_a,first_no_wl_b,second_no_wl_a,second_no_wl_b)
	lights.append(sprout)
print(lights)
for light in lights:
	sprout=new_seed(light,first_no_lt_a,first_no_lt_b,second_no_lt_a,second_no_lt_b)
	temperatures.append(sprout)
for temperature in temperatures:
	sprout=new_seed(temperature,first_no_th_a,first_no_th_b,second_no_th_a,second_no_th_b)
	humiditys.append(sprout)
print(humiditys)
for humidity in humiditys:
	sprout=new_seed(humidity,first_no_hl_a,first_no_hl_b,second_no_hl_a,second_no_hl_b)
	locations.append(sprout)
print(locations)
print(min(locations))
































