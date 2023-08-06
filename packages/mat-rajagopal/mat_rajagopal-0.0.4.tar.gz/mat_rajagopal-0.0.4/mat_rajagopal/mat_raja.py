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

def constant_mat(A,dim):
    mat1=[]
    for i in range(dim):
        a=[]
        for j in range(dim):
            s=A
            a.append(s)
        mat1.append(a)
    return mat1


def mat_multiple(x,y):
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

def mat_inverse(a):
    if len(a)==len(a[0])==2:
        l=det_2(a)
        if l!=0:
            x=adjoint(a)
            y=1/l
            z=constant_mat(y,2)
            inv_a=element_mul(z,x)
            return inv_a
        else:
            print('it is a singular matrix')


    if len(a)==len(a[0])==3:
        b=adjoint(a)
        m=det_3(a)
        if m!=0:
            n=1/m
            o=constant_mat(m,3)
            inv_a=element_mul(o,b)
            return inv_a
        else :
            print(' it is a singular matrix because det is 0')
    else:
        print('inverse not possible')

def element_mul(matrix_a,matrix_b):
    if len(matrix_a)==len(matrix_b):
        mat1=[]
        for i in range(len(matrix_a)):
            a=[]
            for j in range(len(matrix_b[0])):
                s=matrix_a[i][j]*matrix_b[i][j]
                a.append(s)
            mat1.append(a)
        return mat1
    else:
        print('multiplication not possible')

def mul_commutative(a,b):
    print('commutative property:a*b=b*a')
    c=mat_multiple(a,b)
    d=mat_multiple(b,a)
    print('a*b=',c)
    print('b*a',d)
    if c==d:
        print('commutaive property is true')
    else:
        print('commutative property is false')

def mul_assosiative(a,b,c):
    print('assosiative property: a*(b*c)=(a*b)*c')
    d=mat_multiple(b,c)
    e=mat_multiple(a,d)
    print('a*(b*c)=',e)
    f=mat_multiple(a,b)
    g=mat_multiple(f,c)
    print('(a*b)*c=',g)
    if g==e:
        print('assosiative property is true')
    else:
        print('assosiative property is false')

def distributive(a,b,c):
    print('distibutive property:a*(b+c)=(a*b)+(a*c)')
    d=mat_add(b,c)
    e=mat_multiple(a,d)
    print('a*(b+c)=',e)
    f=mat_multiple(a,b)
    g=mat_multiple(a,c)
    h=mat_add(f,g)
    print('(a*b)+(a*c)=',h)
    if e==h:
        print('distributive property is true')
    else:
        print('distributive property is false')

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

def add_commutative(a,b):
    print('commutative property for addition:a+b = b+a')
    c=matrix_addition(a,b)
    d=matrix_addition(b,a)
    print('a+b=',c)
    print('b+a=',d)
    if c==d:
        print('commutative property for addition is true')
    else:
        print('commutative property for addition is false')

def add_assosiative(a,b,c):
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
    print('multiplication transpose is (a*b)T=(b)T*(a)T')
    c=mat_multiple(a,b)
    d=mat_transpose(c)
    print('(a*b)T=',d)
    e=mat_transpose(b)
    f=mat_transpose(a)
    g=mat_multiple(e,f)
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

    b=mat_multiple(const,a)
    c=mat_transpose(b)
    print('(const*a)T=',c)
    d=mat_transpose(a)
    e=mat_multiple(const,d)
    print('const*(a)T=',e)
    if e==c:
        print('scalar multiplication transpose is true')   
    else:
        print('scalar multiplication transpose is false')
    
