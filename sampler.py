import sys
from constraints import Constraint as c
import numpy as np

def main(Input_file,Output_file,samples):
    C = c(Input_file)
    dim = C.get_ndim()
    example = C.get_example()
    result = C.apply(example)
    if result == True:
        with open(Output_file, "a") as f:
            f.write(' '.join([str(i) for i in example])+'\n')
    n=1
    while n <= (samples-1):
        Example={}
        for j in range(dim):
            Example.update({j:np.random.uniform(-example[j],example[j],1)[0]})
        Example = list(Example.values())
        print(Example, result)
        result = C.apply(Example)
        if result == True:
            with open(Output_file, "a") as f:
                f.write(' '.join([str(i) for i in example])+'\n')
            print(Example)
            n+=1  
    return example

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],int(sys.argv[3]))