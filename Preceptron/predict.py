w1 = 0
w2 = 0
b = 0
def  cal(x1,x2):
	global w1,w2,b
	if (w1*x1 + w2*x2 +b)>0 :
		return 1
	else:
		return -1

if __name__ == '__main__':
	model = open('/home/lz/workspace/ML algorithm achieve/Preceptron/model','r',0)
	test = open('/home/lz/workspace/ML algorithm achieve/Preceptron/test','r',0)
	lens = 0
	for line in model:
		parameter = line.strip().split(' ')
		global w1,w2,b
		w1 = int(parameter[0])
		w2 = int(parameter[1])
		b = int(parameter[2])
	for line in test:
		chunk = line.strip().split(' ')
		x1 = int(chunk[1])
		x2 = int(chunk[2])
		predict = cal(x1,x2)
		result = open('/home/lz/workspace/ML algorithm achieve/Preceptron/result','a',0)
		result.write(str(predict)+'\n')
		result.close()