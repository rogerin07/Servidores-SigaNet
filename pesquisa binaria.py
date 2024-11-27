class Pesquisabinaria:

    def pesquisa_lista(self, lista, item):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            medio = (baixo + alto) // 2
            chute = lista[medio]

            if chute == item:
                return medio
            
            if chute > item:
                alto = medio - 1

            else:
                baixo = medio + 1
            
        return None
    
    def lista_repetida(self, lista, baixo, alto, item):

        if alto >= baixo:
            medio = (alto + baixo) // 2
            chute = lista[medio]

            if chute == item:
                return medio
            
            elif chute > item:
                return medio
            
            elif chute > item:
                return self.lista_repetida(lista, baixo, medio, - 1, alto, item)
            
            else:
                return self.lista_repetida(lista, medio, +1, alto, item)
        else:
            return None
if __name__ == '__main__':
    bs = Pesquisabinaria()
    minha_lista = [1,3,5,7,9]

    print(bs.pesquisa_lista(minha_lista, 3))
    print(bs.pesquisa_lista(minha_lista, -1)) 
        
    
    


