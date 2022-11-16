def lista():
    palavra=[65]
    #lista com a primeira letra
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
            if  palavra[i] < 90:
                palavra[i]+=1
                break
                
            #volta para 65 a[i] e continua o laço para somar 1 nos próximos
            if  palavra[i] == 90:
                palavra[i]=65
        else:
            #caso todo o laço conclua é adicionado mais um elemento na lista
            palavra.append(65)
            a+=1#modifica o tamanho da lista

            
a=iter(lista())
for i in range(1000000):
    print(next(a))
