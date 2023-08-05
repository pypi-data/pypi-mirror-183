from format import output

def aumento (valor, porcentagem, format=False):
    r = valor + (valor*(porcentagem/100))  

    if format == True:
        return output.real(r)
    else: 
        return r
 
def reducao (valor, porcentagem, format=False):
    r = valor - (valor*(porcentagem/100)) 
    
    if format == True:
        return output.real(r) 
    else: 
        return r