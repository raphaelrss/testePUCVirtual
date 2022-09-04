
def nomes_unicos(l1, l2):
    res = []

    # esse for vai percorrer os itens da lista 'l1'
    for i in l1:
        # esse if testa se o item 'i' já existe na lista res, caso não, ele é adicionado através do método .append()
        if i not in res:
            res.append(i)

    # esse for vai percorrer os itens da lista 'l2'
    for i in l2:
        # esse if testa se o item 'i' já existe na lista res, caso não, ele é adicionado através do método .append()
        if i not in res:
            res.append(i)

    # aqui é feito a ordenação alfabética da lista 'res' através do método .sort()
    res.sort()
    return res


if __name__ == "__main__":

    lista1 = ['Ana', 'Maria', 'José', 'Julia', 'Antônio']
    lista2 = ['José', 'Luiz', 'Raphael', 'Maria', 'Ana', 'Carlos']

    print(nomes_unicos(lista1, lista2))
