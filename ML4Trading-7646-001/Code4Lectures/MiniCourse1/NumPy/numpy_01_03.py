
import numpy as np
import timeit

def test_run():
    np.random.seed(639)
    a = np.random.randint(0,10,size=(5,4))
    print a.sum(axis = 0)





if __name__ == "__main__":
    test_run()