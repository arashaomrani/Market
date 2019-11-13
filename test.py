import sys

def main(x,y):
    print(x+y)
    return x+y

if __name__=="__main__":
    main(int(sys.argv[1]),int(sys.argv[2]))