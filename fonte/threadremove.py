import threading

NULL = -1

class ThreadRemove(threading.Thread):

    def __init__(self, column, index):
        threading.Thread.__init__(self)
        self.column = column
        self.index = index

    def getData(self):
        return self.index, self.column


    def run(self):
        for i in xrange(1, len(self.column)):
            e = self.column[i]
            if e <> NULL:
                for j in xrange(i+1, len(self.column)):
                    e_2 = self.column[j]
                    if e_2 <> NULL:
                        if e == e_2:
                            self.column[i] = NULL
                            self.column[j] = NULL
                            e = NULL
                            e_2 = NULL
                            break
