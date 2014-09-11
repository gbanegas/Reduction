from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount

import threading
if __name__ == '__main__':
    red = Reduction()
    print red.reduction([16,12,8,4,0])