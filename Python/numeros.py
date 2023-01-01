class numero:
    __lista=[str(i) for i in range(10)]
    for i in range(ord("A"),ord("Z")+1):
        __lista.append(chr(i))
        
    
    def _init_(self,valor=None,base=10):
        
        if 0 < base < 37:
            self.__base=base
            if valor == None:
                self.valor="0"
            else:
                self.valor=str(valor)
        else:
            raise ValueError(f"Base {base} invalida")
    
