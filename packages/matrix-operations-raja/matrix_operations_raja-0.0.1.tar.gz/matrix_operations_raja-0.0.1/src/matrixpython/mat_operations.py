def mat_input(row,column):
    mat1=[]
    for i in range(row):
        a=[]
        for j in range(column):
            s=int(input('enter the matrix values'))
            a.append(s)
        mat1.append(a)
    return mat1 

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
        
    else:
        print('multiplication not possible')

def mat_add(matrix_a,matrix_b):
    if len(matrix_a)==len(matrix_b):
        mat1=[]
        for i in range(len(matrix_a)):
            a=[]
            for j in range(len(matrix_b[0])):
                s=matrix_a[i][j]+matrix_b[i][j]
                a.append(s)
            mat1.append(a)
    return mat1

def mat_sub(matrix_a,matrix_b):
    if len(matrix_a)==len(matrix_b):
        mat1=[]
        for i in range(len(matrix_a)):
            a=[]
            for j in range(len(matrix_a[0])):
                s=matrix_a[i][j]-matrix_b[i][j]
                a.append(s)
            mat1.append(a)
    return mat1

def mat_div(matrix_a,matrix_b):
    if len(matrix_a)==len(matrix_b):
        mat1=[]
        for i in range(len(matrix_a)):
            a=[]
            for j in range(len(matrix_b[0])):
                s=matrix_a[i][j]/matrix_b[i][j]
                a.append(s)
            mat1.append(a)
    return mat1

def mat_trace(matrix_a):
    trace=0
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            if i==j:
                trace=trace+matrix_a[i][j]
    return trace

def mat_transpose(matrix_a):
    mat1t=[]
    for i in range(len(matrix_a[0])):
        b=[]
        for j in range(len(matrix_a)):
            t=matrix_a[j][i]
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

def area(a,aa,b,bb,c,cc):
    print('please enter the three points of triangle as (x1,y1,x2,y2,x3,y3)')
    m=[[a,aa,1],[b,bb,1],[c,cc,1]]
    area=0.5*(det(m))
    if area>0:
       return area
    else:
        return (-1*area)
    
    
    







