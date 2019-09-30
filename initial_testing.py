from timeit import default_timer as timer

def testo_funco(inp):
	print("currently at -> " + str(inp))

inp = range(0,1000)
time_list = []
for elem in inp:
	start = timer()
	testo_funco(elem)
	end = timer()
	time_list.append(end-start)
	print("This time:" + str(end - start))
print("Average time: " + str(sum(time_list)/len(time_list)))