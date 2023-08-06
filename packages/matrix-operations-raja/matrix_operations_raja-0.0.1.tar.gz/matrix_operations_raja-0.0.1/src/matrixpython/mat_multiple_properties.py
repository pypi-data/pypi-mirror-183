
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
        return 'addition not possible'
        
    


def matrix_multiply(x,y):
    if len(x)==len(y[0]):
        r=[]
        for i in range(len(x)):
            c=[]
            for j in range(len(y[0])):
                c.append(0)
            r.append(c)
        

        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                      r[i][j]=r[i][j]+x[i][k]*y[k][j]
        return r
        
    else:
        return 'multiplication not possible'

def commutative(a,b):
    print('commutative property:a*b=b*a')
    c=matrix_multiply(a,b)
    d=matrix_multiply(b,a)
    print('a*b=',c)
    print('b*a',d)
    if c==d:
        print('commutaive property is true')
    else:
        print('commutative property is false')

def assosiative(a,b,c):
    print('assosiative property: a*(b*c)=(a*b)*c')
    d=matrix_multiply(b,c)
    e=matrix_multiply(a,d)
    print('a*(b*c)=',e)
    f=matrix_multiply(a,b)
    g=matrix_multiply(f,c)
    print('(a*b)*c=',g)
    if g==e:
        print('assosiative property is true')
    else:
        print('assosiative property is false')

def distributive(a,b,c):
    print('distibutive property:a*(b+c)=(a*b)+(a*c)')
    d=matrix_addition(b,c)
    e=matrix_multiply(a,d)
    print('a*(b+c)=',e)
    f=matrix_multiply(a,b)
    g=matrix_multiply(a,c)
    h=matrix_addition(f,g)
    print('(a*b)+(a*c)=',h)
    if e==h:
        print('distributive property is true')
    else:
        print('distributive property is false')

