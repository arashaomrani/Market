import sys
from constraints import Constraint as c
import numpy as np

def main(Input_file,Output_file,samples,limit=None):
    C = c(Input_file)
    dim = C.get_ndim()
    example = C.get_example()
    result = C.apply(example)
    if result == True:
        with open(Output_file, "a") as f:
            f.write(' '.join([str(i) for i in example])+'\n')
    n=1
    while n <= (samples-1):
        scale2=0.001
        for i in range(1,6):
            for d in range(dim):
                scale1=example[d] * scale2
                temp = example.copy()
                rand = np.random.uniform(-scale1,scale1,1)[0]
                if temp[d] != 0:
                    temp[d] = temp[d]+rand
                else: 
                    temp[d] = np.random.uniform(-scale2,scale2,1)[0]
                result = C.apply(temp)
                if limit:
                    if result == True and n<=(samples-1) and temp[d] > -1*limit and temp[d] < limit:
                        with open(Output_file, "a") as f:
                            f.write(' '.join([str(i) for i in example])+'\n')
                        print(temp)
                        example = temp.copy()
                        n+=1 
                else:
                    if result == True and n<=(samples-1):
                        with open(Output_file, "a") as f:
                            f.write(' '.join([str(i) for i in example])+'\n')
                        print(temp)
                        example = temp.copy()
                        n+=1 

            scale2 = scale2*10


if __name__=="__main__":
    if len(sys.argv) > 4:
        main(sys.argv[1],sys.argv[2],int(sys.argv[3]), float(sys.argv[4]))
    else:
        main(sys.argv[1],sys.argv[2],int(sys.argv[3]))
