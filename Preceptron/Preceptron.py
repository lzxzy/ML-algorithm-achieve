import os
import sys

trainint_set = []

w = []
a = []
b = 0
lens = 0
n = 1
Gram = []

def calInnerProduct(i,j):
	global lens	
	res = 0
	for p in range(lens):
		res += trainint_set[i][0][p] * trainint_set[j][0][p]
	return res

def  AddVector(vec1,vec2):
	for i in range(lne(vec1)):
		vec1[i] = vec1[i] + vec2[i]
	return vec1
		
def  NumProduct(num,vec):
	for i in range(len(vec)):
		vec[i] *= num
	return vec

def  createGram():
	global lens
	for i in range(len(trainint_set)):
		tmp = []
		for j in range(0,len(trainint_set)):
			tmp.append(calInnerProduct(i,j))
		Gram.append(tmp)

#update paraments using stochastic gradint descent
def update(k):
	global a,b,n
	a[k] += n
	b = b + n*trainint_set[k][1]
	print a,b # you can uncomment this line to check the process of stochastic gradient descent

#calculate the functional discent between 'item' an the dicision surface
def cal(k):
	global a,b
	res = 0
	for i in range(len(trainint_set)):
		res += a[i] * int(trainint_set[i][1])*Gram[i][k]
	res += b
	res *= trainint_set[k][1]
	return res

#check if the hyperplane can classify the examples correctly
def  check():
	global w,a
	flag = False
	for i in range(len(trainint_set)):
		if cal(i)<= 0:
			flag = True
			update(i)
	if not flag: 
		for i in range(len(trainint_set)):
			w = addVector(w,NumProduct(a[i]*int(trainint_set[i][1]),trainint_set[i][0]))
		print "RUSELT: w:" ,w,"b:",b
		tmp = ''
		for keys in w:
			tmp += str(keys)+' '
		tmp = tmp.strip()
		modelFile.write(tmp + '\n')
		modelFile.write(str(b) + '\n')
        modelFile.write(str(lens) + '\n')
        modelFile.write(str(n) + '\n')
        modelFile.close()
        os._exit(0)
   	flag = False

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print "Usage: python perceptron_duality.py n trainFile modelFile"
		exit(0)
	trainFile = file(sys.argv[2])
	modelFile = file(sys.argv[3],'w')
	lens = 0
	a=0
	for line in trainFile:
		chunk = line.strip().split(' ')
		lens = len(chunk) - 1
		tmp_all = []
		tmp = []
		for i in range(1,lens+1):
			print chunk[i]
		 	tmp.append(int(chunk[i]))
		tmp_all.append(tmp)
		tmp_all.append(int(chunk[0]))
		trainint_set.append(tmp_all)
	trainFile.close()

	createGram()
	for i in range(len(trainint_set)):
		a.append(0)
	for i in range(lens):
		w.append(0)

	for i in range(1000):
		check()
	print "The training_set is not linear separable. "
