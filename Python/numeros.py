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
        
    def _str_(self):
        
        return "{"+f"valor:{''.join(self._valor)},  base:{self._base}"+"}"
    
    
    def somar(self,soma):
        
        tamanho_s=len(soma)
        v=self.valor[::-1]
        while tamanho_s > len(v):
            v.append("0")

        soma=soma[::-1]
        t=0
        
        for i in range(len(v)):
           
            if tamanho_s > i:
                
                t+=self._decimal(soma[i],self.base)+self.decimal(v[i],self._base)
                if t < self.__base:
                    v[i]=self.lista_posicao(t)
                    
                    t=0
                else:
                    t-=self.__base
                    v[i]=self.lista_posicao(t)
                    t=1
        else:
            if t != 0:
                v.append(self.lista_posicao(t))
        
        return v[::-1]
        
    def _add_(self,*valores):
        for v in valores:
            if type(v) != int:
                valor=v.valor
            else:
                valor=[i for i in str(v)]
            self.__valor=self.somar(valor)
        return self
