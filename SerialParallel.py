#Serial Programming vs Parallel Programming

from threading import*;
from multiprocessing import*;
from time import*;
from os import*;

def Square(no):
	print(getpid());
	return no * no
	
def main():
	arr = [1,31,41,2,3,5,4,2]
	brr = []
	
	starttime1 = time()
	for i in range(len(arr)):
		brr.append(Square(arr[i]))
	endtime1 = time()
	
	print(brr)
	
	print("Serial",endtime1 - starttime1);
	
	pobj = Pool()
	
	starttime2 = time()
	crr = pobj.map(Square,arr)
	endtime2 = time()
	
	print(crr)
	
	print("Parallel",endtime2 - starttime2)
	print(getpid())
	
if __name__ == "__main__":
	main()