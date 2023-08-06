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

def deter(a):
    if len(a)==2==len(a[0]):
        x=det_2(a)
        return x
    if len(a)==3==len(a[0]):
        y=det_3(a)
        return y


def cramer(det,b):
    if len(det)==3:
        print('please enter the equation matrix [[a,b,c],[d,e,f],[g,h,i]] and equal to matrix as [[a],[b],[c]]')
       # det=[[det[0][0],det[0][1],det[0][2]]
        #    [det[1][0],det[1][1],det[1][2]]
         #   [det[2][0],det[2][1],det[2][2]]]
        x=[[b[0][0],det[0][1],det[0][2]],
            [b[1][0],det[1][1],det[1][2]],
            [b[2][0],det[2][1],det[2][2]]]
        y=[[det[0][0],b[0][0],det[0][2]],
            [det[1][0],b[1][0],det[1][2]],
            [det[2][0],b[2][0],det[2][2]]]
        z=[[det[0][0],det[0][1],b[0][0]],
            [det[1][0],det[1][1],b[1][0]],
            [det[2][0],det[2][1],b[2][0]]]
        
        dem=deter(det)
        detx=deter(x)
        dety=deter(y)
        detz=deter(z)
        if dem!=0:
            #cramers rule
            A=detx/dem        
            B=dety/dem      
            C=detz/dem 

            print('x=',A)
            print('y=',B)
            print('z=',C)
        else:
            print('cramers rule not possible because det is 0')

    if len(det)==2:
        print('please enter the equation matrix [[a,b],[d,e]] and equal to matrix as [[a],[b]]')
        l=[[b[0][0],det[0][1]],
            [b[1][0],det[1][1]]]
        m=[[det[0][0],b[0][0]],
            [det[1][0],b[1][0]]]
        dem_2=deter(det)
        detx_2=deter(l)
        dety_2=deter(m)
        
        if dem_2!=0:
            #cramers rule
            A=detx_2/dem_2        
            B=dety_2/dem_2      

            print('x=',A)
            print('y=',B)
        else:
            print('cramers rule not possible because det is 0')


        






