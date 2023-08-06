def matrix_addition(x,y):
    if len(x)==len(y) and len(x[0])==len(y[0]):
        r_add=[]
        for i in range(len(x)):
            a=[]
            for j in range(len(x[0])):
                s=x[i][j]+y[i][j]
                a.append(s)
            r_add.append(a)
        return r_add
    else:
        print('addition not possible')

def commutative(a,b):
    print('commutative property for addition:a+b = b+a')
    c=matrix_addition(a,b)
    d=matrix_addition(b,a)
    print('a+b=',c)
    print('b+a=',d)
    if c==d:
        print('commutative property for addition is true')
    else:
        print('commutative property for addition is false')

def assosiative(a,b,c):
    print('assosiative property for addition:a+(b+c)=(a+b)+c')
    d=matrix_addition(b,c)
    e=matrix_addition(a,d)
    print('a+b=',e)
    f=matrix_addition(a,b)
    g=matrix_addition(f,c)
    print('(a+b)+c=',g)
    if e==g:
        print('assosiative property for addition is true')
    else:
        print('assosiative property for addition is false')

def additive_identity(a):
    print(' matrix additive identity:a+o=a')

    mat1=[]
    for i in range(len(a)):
        x=[]
        for j in range(len(a[0])):
            s=0
            x.append(s)
        mat1.append(x)

    print('a=',a)
    b=matrix_addition(a,mat1)
    print(b)
    if a==b:
         print('additive identity for addition is true')
    else:
        print('additive identity for addition is false')

def additive_inverse(a,b):
    print(' matrix additive inverse:a+b=0')
    c=matrix_addition(a,b)
    print('a+b=',c)

    mat1=[]
    for i in range(len(a)):
        x=[]
        for j in range(len(a[0])):
            s=0
            x.append(s)
        mat1.append(x)
    
    if c==mat1:
        print('additive inverse is true')
    else :
        print('additive inverse is not true')

a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
c=[[1,2],[3,4]]

commutative(a,b)
assosiative(a,b,c)
additive_identity(a)
additive_inverse(a,b)


    
