from hmm import *
import sys

def read_model(path):
    
    f = open(path, "r")
    lines = f.readlines()

    pi = []
    A = []
    B = [] 

    initial_f = False
    A_f = False
    B_f = False
    l_count = 0

    for line in lines:        
        if initial_f:
            initial_f = False
            pi = [float(i) for i in line.split()]
        if A_f:
            if l_count>0:
                A.append([float(i) for i in line.split()])
                l_count -= 1
            else:
                A_f = False
        if B_f:
            if l_count>0:
                B.append([float(i) for i in line.split()])
                l_count -= 1
            else:
                B_f = False
        if line.startswith('initial'):
            initial_f = True
        if line.startswith('transition'):
            l_count = int(line.split()[1])
            A_f = True
        if line.startswith('observation'):
            l_count = int(line.split()[1])
            B_f = True
    return np.array(A,dtype='double'), np.array(B,dtype='double'), np.array(pi,dtype='double')

def measure_p_o_lambda(models,test_data):
    p_o_lambda1 = {'model_0{}'.format(i):[] for i in range(1,6)}
    result1 = []
    for line in test_data:
        p_max = 0
        for i in range(1,6):
            dummy,p = models['HMM_model{}'.format(i)].backward(line)
            p_o_lambda1['model_0{}'.format(i)].append(p)
            if p >= p_max:
                p_max = p
                model_max = 'model_0{}.txt'.format(i)
        result1.append((model_max,p_max))
    return p_o_lambda1,result1

def write_results_to_file(models,test_data, path):
    pol,result = measure_p_o_lambda(models,test_data)
    with open(path, 'w') as f:
        for item in result:
            f.write(item[0]+' {}\n'.format(item[1]))

f = open(sys.argv[2], "r")
test_data = [line.strip() for line in f.readlines()]

models = {}
modellist = open(sys.argv[1], 'r').readlines()
for i,model in enumerate(modellist):
    A,B,pi = read_model("models\\"+model.strip())
    models['HMM_model{}'.format(i+1)] = HMM(A,B,pi)

write_results_to_file(models,test_data, sys.argv[3])
