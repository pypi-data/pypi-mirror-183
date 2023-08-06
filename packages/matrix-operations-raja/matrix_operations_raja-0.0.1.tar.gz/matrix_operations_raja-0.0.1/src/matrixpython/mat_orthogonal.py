def unit_mat(dim):
        mat1=[]
        for i in range(dim):
            a=[]
            for j in range(dim):
                if i==j:
                    s=1
                else :
                    s=0
                a.append(s)
            mat1.append(a)
        return mat1

def det_2(mat1):
    #determinant of matrix 2x2
    a=1
    b=1
    for i in range(2):
        for j in range(2):
            if i==j:
                a=a*mat1[i][j]
            if i!=j:
                b=b*mat1[i][j]
    return a-b


def det_3(a):
    x=a[0][0]
    y=a[1][0]
    z=a[2][0]
    l=[[a[1][1],a[1][2]],[a[2][1],a[2][2]]]
    m=[[a[0][1],a[0][2]],[a[2][1],a[2][2]]]
    n=[[a[0][1],a[0][2]],[a[1][1],a[1][2]]]
    a=det_2(l)
    b=det_2(m)
    c=det_2(n)
    return (x*a)-(y*b)+(z*c)

def det(a):
    if len(a)==2==len(a[0]):
        x=det_2(a)
        return x
    if len(a)==3==len(a[0]):
        y=det_3(a)
        return y

def mat_multiple(matrix_a,matrix_b):
    if len(matrix_a[0])==len(matrix_b):
        r=[]
        x=0
        for i in range(len(matrix_a)):
            b=[]
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                      x+=matrix_a[i][k]*matrix_b[k][j]
                b.append(x)
            r.append(b)
        return r

def mat_transpose(matrix_a):
    mat1t=[]
    for i in range(len(matrix_a[0])):
        b=[]
        for j in range(len(matrix_a)):
            t=matrix_a[j][i]
            b.append(t)
        mat1t.append(b)
    return mat1t

def unitnum_mat(m,dim):
    mat1=[]
    for i in range(dim):
        a=[]
        for j in range(dim):
            if i==j:
                s=m
            else :
                s=0
            a.append(s)
        mat1.append(a)
    return mat1

def mat_ortho(a):
    print('orthogonal property (A)*(A)T=(A)T*(A)=Det(A)*I')
    print('given matrix = ',a)
    b=unit_mat(len(a))
    c=det(a)
    d=mat_transpose(a)
    e=mat_multiple(a,d)
    f=mat_multiple(d,a)
    g=unitnum_mat(c,len(a))
    if e==f==g:
        print('orthohonal property is true')
        print(e,'=',f,'=',g)
    else:
        print('orthogonal property is false')
        print(e,'!=',f,'!=',g)

