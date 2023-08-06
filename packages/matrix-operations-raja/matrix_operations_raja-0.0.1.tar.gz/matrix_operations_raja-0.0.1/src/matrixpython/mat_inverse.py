def mat_transpose(a):
    mat1t=[]
    for i in range(len(a[0])):
        b=[]
        for j in range(len(a)):
            t=a[j][i]
            b.append(t)
        mat1t.append(b)
    return mat1t


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

def adjoint(a):
    if len(a)==len(a[0])==2:
        b=[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]
        return b
    if len(a)==len(a[0])==3:
        b=[[a[1][1],a[1][2]],[a[2][1],a[2][2]]]
        c=[[a[1][0],a[1][2]],[a[2][0],a[2][2]]]
        d=[[a[1][0],a[1][1]],[a[2][0],a[2][1]]]
        e=[[a[0][1],a[0][2]],[a[2][1],a[2][2]]]
        f=[[a[0][0],a[0][2]],[a[2][0],a[2][2]]]
        g=[[a[0][0],a[0][1]],[a[2][0],a[2][1]]]
        h=[[a[0][1],a[0][2]],[a[1][1],a[1][2]]]
        i=[[a[0][0],a[0][2]],[a[1][0],a[1][2]]]
        j=[[a[0][0],a[0][1]],[a[1][0],a[1][1]]]

        bb=det_2(b)
        cc=(-1)*det_2(c)
        dd=det_2(d)
        ee=(-1)*det_2(e)
        ff=det_2(f)
        gg=(-1)*det_2(g)
        hh=det_2(h)
        ii=(-1)*det_2(i)
        jj=det_2(j)

        adja=[[bb,cc,dd],[ee,ff,gg],[hh,ii,jj]]
        adjat=mat_transpose(adja)
        return adjat

def constant_mat(A,dim):
    mat1=[]
    for i in range(dim):
        a=[]
        for j in range(dim):
            s=A
            a.append(s)
        mat1.append(a)
    return mat1 

def mat_mul(matrix_a,matrix_b):
    if len(matrix_a)==len(matrix_b):
        mat1=[]
        for i in range(len(matrix_a)):
            a=[]
            for j in range(len(matrix_b[0])):
                s=matrix_a[i][j]*matrix_b[i][j]
                a.append(s)
            mat1.append(a)
    return mat1

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

def mat_inverse(a):
    if len(a)==len(a[0])==2:
        l=det_2(a)
        if l!=0:
            x=adjoint(a)
            y=1/l
            z=constant_mat(y,2)
            inv_a=mat_mul(z,x)
            return inv_a
        else:
            print('it is a singular matrix')


    if len(a)==len(a[0])==3:
        b=adjoint(a)
        m=det_3(a)
        if m!=0:
            n=1/m
            o=constant_mat(m,3)
            inv_a=mat_mul(o,b)
            return inv_a
        else :
            print(' it is a singular matrix because det is 0')
    else:
        print('inverse not possible')

        



