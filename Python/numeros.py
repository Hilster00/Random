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
    
    @classmethod
    def lista_posicao(cls,i):
        return cls.__lista[i]    
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self,valor):
        self.__valor=[i for i in str(valor)]
    
    @classmethod
    def __decimal(cls,valor,base):
        d=0
        for i,va in enumerate(valor[::-1]):
            d+=cls.__lista.index(va)base*i
        return d
        
    def decimal(self,valor=None,base=None):
        if valor == None:
            valor=self.valor
        if base == None:
            base=self.__base
        return self.__decimal(valor,base)
