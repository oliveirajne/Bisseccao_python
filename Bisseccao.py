
#variaveis
N, i = 0, 0
F, x, e, a_0, b_0, a_i, b_i, x_iml, fa, fb, fx, d_1 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

#atribuicoes
a_0 = 1.0e00
b_0 = 2.0e00
e = 1.0e-2
N = 3
a_i = a_0
b_i = b_0

#funcoes
def funcao(x):

    fx = x ** 3 - x - 1

    return fx

def format_notacao(x):
    
    fx = '{0:.4E}'.format(x)

    return fx 

file = open('Bi.sai', 'w')

for i in range(0, N+1):
    x_iml = 0.5e0 * (a_i + b_i)

    fa = funcao(a_i)
    fb = funcao(b_i)
    fx = funcao(x_iml)

    d_1 = b_i - a_i

    if ( abs(x_iml) != 0.0e0 ):
        d_1 = d_1 / abs(x_iml)
    
    if ( d_1 <= e ):
        if ( abs(fx) <= e ):
            file.write('{0:2}'.format(i) + '{0:16.4e}'.format(a_i) + '{0:16.4e}'.format(b_i) + '{0:16.4e}'.format(x_iml) 
            + '{0:16.4e}'.format(fa) + '{0:16.4e}'.format(fb) + '{0:16.4e}'.format(fx) + '{0:16.4e}'.format(d_1) +'\n')
 
    file.write('{0:2}'.format(i) + '{0:16.4e}'.format(a_i) + '{0:16.4e}'.format(b_i) + '{0:16.4e}'.format(x_iml) 
    + '{0:16.4e}'.format(fa) + '{0:16.4e}'.format(fb) + '{0:16.4e}'.format(fx) + '{0:16.4e}'.format(d_1) +'\n')       
            
    if ( fa*fx <= 0.0e0 ):
        b_i = x_iml
    else:
        a_i = x_iml

file.close()
