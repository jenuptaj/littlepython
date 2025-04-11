#t = matrix([[1,2,3,4],[6,7,8,9],[4.5,5.4,6.3,3.6]])
class matrix:
    def __init__(self,lst):
        if type(lst[0]) != type([]):
            self.order = lst[0],lst[1]
            self.val = [[lst[2]]*lst[1] for x in range(lst[0])]
        else:
            self.order = (len(lst),len(lst[0]))
            self.val = list(lst)
    def __str__(self):
        a = ''
        for i in self.val:
            a += '|'
            for j in i:
                a += str(j) + '\t'
            a += '| \n'
        return a
    def transpose(self):
        l = self.val
        lst = [[l[x][y] for x in range(len(l))] for y in range(len(l[0]))]
        return matrix(lst)
    def __add__(self,other):
        return matrix([[self.val[i][j] + other.val[i][j] for j in range(len(self.val[0]))] for i in range(len(self.val))])
    def __sub__(self,other):
        return matrix([[self.val[i][j] - other.val[i][j] for j in range(len(self.val[0]))] for i in range(len(self.val))])
    def __mul__(self,other):
        A = self.val
        if type(other) == type(1):
            C = matrix([[A[x][y]*other for y in range(len(A[0]))] for x in range(len(A))])
            return C
        elif self.order[1] == other.order[0]:
            B = other.transpose().val
            C = [[sum([A[x][x1]*B[y][x1] for x1 in range(len(A[0]))]) for y in range(len(B))]for x in range(len(A))]
            return matrix(C)
        else:
            return None
if __name__ == '__main__': #Testing
    t = matrix([[1,2,3,4],[6,7,8,9],[4.5,5.4,6.3,3.6]])
    s = matrix([[0.1,0.2,0.3,0.4],[0.6,0.7,0.8,0.9],[1,2,3,4]])
    while True:
        exec(input('>>>'))