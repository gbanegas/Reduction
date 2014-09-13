def optimize(self, matrix, element):
        dic = {}
        for i in xrange(0, len(matrix)-1):
            row = matrix[i]
            for j in xrange(0, len(row)):
                if row[j] == element:
                    if matrix[i+1][j] <> -1:
                        if  matrix[i+1][j] in dic:
                            value = dic[ matrix[i+1][j]] +1
                        else:
                            dic[matrix[i+1][j]] = 1
        
        key = -1;
        app = 1
        for i in dic:
            if dic[i] > app:
                key = i
                app = dic[i]
        if key <> -1:
            for i in xrange(0, len(matrix)-1):
                row = matrix[i]
                for j in xrange(0, len(row)):
                    if row[j] == element:
                        if matrix[i+1][j] ==  key:
                            matrix[i+1][j] = 'T'
                            row[j] = 'T'
                            matrix[i] = row