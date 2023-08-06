def mat_transpose(a):
    mat1t=[]
    for i in range(len(a[0])):
        b=[]
        for j in range(len(a)):
            t=a[j][i]
            b.append(t)
        mat1t.append(b)
    return mat1t

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

def double_transpose(a):
    print('tranpose of a tranpose matrix:((a)T)T=a')
    b=mat_transpose(a)
    c=mat_transpose(b)
    print('a=',a)
    print('((a)T)T=',c)
    if a==c:
        print('double_transpose of the matrix is true')

def sum_transpose(a,b):
    print('transpose of sum of two matrix=sum of two transpose matrix')
    print('                (a+b)T=(a)T+(b)T')
    c=matrix_addition(a,b)
    d=mat_transpose(c)
    print('(a+b)T=',d)
    e=mat_transpose(a)
    f=mat_transpose(b)
    g=matrix_addition(e,f)
    print('(a)T+(b)T',g)
    if d==g:
        print('sum transpose is true')
    else:
        print('sum transpose is false')

def mul_transpose(a,b):
    print('multiplication trancepose is (a*b)T=(b)T*(a)T')
    c=matrix_multiply(a,b)
    d=mat_transpose(c)
    print('(a*b)T=',d)
    e=mat_transpose(b)
    f=mat_transpose(a)
    g=matrix_multiply(e,f)
    print('(b)T*(a)T=',g)
    if d==g:
        print('multiplication of transpose is true')
    else:
        print('multiplication of transpose is false')

def scalar_mul_transpose(a):
    print('multiplication of constant with a matrix whole transpose = multiplication of a constant with the transpose of matrix')
    print('(const*a)T=const*(a)T')
    con=float(input('enter the constant'))
    const=[]
    for i in range(len(a)):
        x=[]
        for j in range(len(a[0])):
            l=con
            x.append(l)
        const.append(x)
    print(const)

    b=matrix_multiply(const,a)
    c=mat_transpose(b)
    print('(const*a)T=',c)
    d=mat_transpose(a)
    e=matrix_multiply(const,d)
    print('const*(a)T=',e)
    if e==c:
        print('scalar multiplication transpose is true')   
    else:
        print('scalar multiplication transpose is false')
     


    