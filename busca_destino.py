
def busca_destino(caminho):

    # essa variável é instanciada para poder retornar o valor após o for
    destino = ''
    # essa variável é usada como uma flag para saber quando foi encontrado o destino final
    encontrado = False
    # o for percorre todos os destinos(cidades B) dos itens da lista 'caminho'
    for i in range(0, len(caminho)):
        j = 0
        # a variável 'destino' é usada para podermos comparar o destino em questão com os próximos
        destino = caminho[i][1]
        # o while vai percorrer as origens(cidades A) dos itens da lista 'caminho'
        # enquanto j for menor que a quantidade de itens na lista 'caminho',
        # destino não for igual a uma origem e
        # caso o destino final não tenha sido encontrado(representado pela variável do tipo bool 'encontrado').
        while j < len(caminho) and not (destino == caminho[j][0]) and not encontrado:
            j += 1
            # esse if verifica se estamos na última posição da lista e, se for esse o caso,
            # o valor de 'destino' no momento é o destino final do caminho e passamos o valor 'True' para 'encontrado'.
            if j == len(caminho):
                encontrado = True

        # saindo do while, caso 'encontrado' seja 'True', já retornamos o destino final.
        if encontrado:
            return destino


if __name__ == "__main__":

    # não sabia se os dados precisavam estar em ordem, daí coloquei eles desordenados,
    # para que a solução pudesse funcionar em qualquer cenário.
    caminho = [['Contagem', 'Belo Horizonte'], ['Barbacena', 'Ouro Preto'], ['Belo Horizonte', 'Congonhas'],
               ['Congonhas', 'Conselheiro Lafaiete'], ['Ouro Preto', 'Diamantina'],
               ['Conselheiro Lafaiete', 'Barbacena']]

    print(busca_destino(caminho))
