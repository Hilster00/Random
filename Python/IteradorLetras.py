def lista(palavra='A',upper=None,lower=False,upper_and_lower=False):
    
    #if upper and lower is equal
    if upper == lower :
        
        #if both are False, upper is activate
        if lower == False:
            first_letter = [65]
            last_letter = [90]
            upper = True
            
        #else, upper and lower are inactivate, and upper_and_lower is activate
        else:
            
            first_letter = [65,97]
            last_letter = [90,122]
            
            upper_and_lower=True
            upper = lower = False
    
    #when upper is not specified and lower isn't declared, upper is activate
    elif upper == None:
        
        first_letter = [65]
        last_letter = [90]
        
        upper = True
        
    else:
        first_letter = [97]
        last_letter = [122]
        
    palavra=[ord(i) for i in palavra[::-1]]
    #lista com a primeira letra
    a=len(palavra)
    #tamanho da lista
    a=1
    #tamanho da lista
    
    while True:
        retorno=''#str de retorno
        
        #as letras são adicionados de trás para frente
        for i in palavra[::-1]:
            retorno+=chr(i)
        
        yield retorno
        
        
        #incrementa em um o ultimo valor significativo
        for i in range(a):
          
            #incrementa em 1 caso a[i] seja o ultimo valor incrementavel
            if  palavra[i] not in last_letter:
                palavra[i]+=1
                break
                
            #volta para 65 a[i] e continua o laço para somar 1 nos próximos
            if  palavra[i] in last_letter:
                if upper_and_lower == False:
                    palavra[i] = first_letter[0]
                else:
                    palavra[i]=122 if palavra[i] == 90 else 65
        else:
            #caso todo o laço conclua é adicionado mais um elemento na lista
            palavra.append(first_letter[0])
            a+=1#modifica o tamanho da lista

            
a=iter(lista(lower=True,upper=True))
for i in range(53):
    print(next(a))
    
