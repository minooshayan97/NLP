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

def write_models_to_files(model, path):
    with open(path, 'w') as f:
        f.write('initial: 6\n')
        for p in model.pi:
            f.write('{}\t'.format(p))
        f.write('\n\ntransition: 6')
        for row in model.A:
            f.write('\n')
            for a in row:
                f.write('{}\t'.format(a))
        f.write('\n\nobservation: 6')
        for row in model.B:
            f.write('\n')
            for b in row:
                f.write('{}\t'.format(b)) 

A,B,pi = read_model(sys.argv[2])

f = open(sys.argv[3], "r")
train_data = [line.strip() for line in f.readlines()]


start = time.time()
print('Training HMM ...')
model = HMM(A,B,pi)
for iteration in range(int(sys.argv[1])):
    model.train_model(train_data)
end = time.time()
print('\nTime spent to train HMM in seconds : ', end-start)

write_models_to_files(model, sys.argv[4])
