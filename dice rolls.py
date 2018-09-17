import random


num = []
def stuff(list):
	i = 0
	while i <=6:
		list.append(random.randint(1,6)+random.randint(1,6)+random.randint(1,6))
		i = i +1
	print(list)


def avg(list):
	t = 0
	for i in range(len(list)):
		t = t + list[i]
	print(t//len(list))

	
def main():
		stuff(num)
		avg(num)
		li = [7,10,9,15,12,12]
		random.shuffle(li)
		print(li)

if __name__ == "__main__":
    main()
	
