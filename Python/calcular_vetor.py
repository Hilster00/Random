def calcular_pow(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    operador=None
    quantidade=0
    
    for i in operacao:
        if type(i) == str:
            if i != "^":
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            if operador == "^":
                resultado[quantidade-1]**=i
            else:
                resultado.append(i)
                quantidade+=1
            operador=None    
    return resultado
 
 
def calcular_multiplicacao(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    operador=None
    quantidade=0
    for i in operacao:
       
        if type(i) == str:
            if i != "*" and i != "/":
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            if operador == "*":
                resultado[quantidade-1]*=i
            elif operador == "/":
                resultado[quantidade-1]/=i
            else:
                resultado.append(i)
                quantidade+=1
            operador=None   
    return resultado
    
def calcular_soma(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    operador=None
    quantidade=0
    for i in operacao:
       
        if type(i) == str:
            if i != "+" and i != "-":
                resultado.append(i)
                quantidade+=1
            else:
                operador=i
        else:
            if operador == "+":
                resultado[quantidade-1]+=i
            elif operador == "-":
                resultado[quantidade-1]-=i
            else:
                resultado.append(i)
                quantidade+=1
            operador=None   
    return resultado

def calcular(operacao=[None]):
    if len(operacao) == 0:
        raise ValueError("ERRO")
    resultado=list()
    
    for i in operacao:
        temp=i
        if type(i)==list:
            temp=calcular(i)
        resultado.append(temp)
    
    resultado=calcular_pow(resultado) 
    resultado=calcular_multiplicacao(resultado)
    resultado=calcular_soma(resultado)  
  
    return resultado[0]
