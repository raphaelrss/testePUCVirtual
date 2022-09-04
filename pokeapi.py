from requests import get

api_url = "https://pokeapi.co/api/v2/"


def get_pokemon(pokemon_id):
    return get(api_url + '/pokemon/' + str(pokemon_id)).json()


def xp_rank(pokemons):

    # for do segundo elemento da lista até o último
    for i in range(1, len(pokemons)):
        # esse é o elemento no qual vamos buscar a posição correta
        key_item = pokemons[i]

        # instancia a variável que será usada para achar a posição correta do elemento em `key_item`
        j = i - 1

        # essas duas variáveis serão usadas como 'keys' para acessarmos os valores dos dicionários
        # dos pokemons
        keyj = str(list((pokemons[j].keys()))[0])
        keyi = str(list((pokemons[i].keys()))[0])

        # percorre a lista de itens (na porção esquerda da lista) e encontra a posição correta do elemento em 'key_item'
        # faz isso apenas se o 'base_experience' em 'key_item' for maior que o do item ao lado.
        while j >= 0 and pokemons[j][keyj] < key_item[keyi]:
            # troca o valor item com a posição à esquerda e
            # incrementa j para que ele aponte para o próximo elemento
            # (da direita pra esquerda)
            pokemons[j + 1] = pokemons[j]
            j -= 1
            keyj = str(list((pokemons[j].keys()))[0])

        # quando termina de trocar os elementos, é possível colocar
        # o elemento em 'key_item' na posição correta
        pokemons[j + 1] = key_item

    return pokemons


if __name__ == "__main__":

    pokemons = []

    for i in range(1, 25):
        pokemon = get_pokemon(i)

        # para executar a função 'xp_rank', preenchemos a lista 'pokemons',
        # aproveitando o for que busca na API cada um dos pokemons dentro do range.
        pokemons.append({pokemon['name']: pokemon['base_experience']})

        print('Nome: ', pokemon['name'])
        print('Altura: ', pokemon['height'])
        print('Peso: ', pokemon['weight'])
        print('Habilidades: ', pokemon['abilities'])
        print('Experiência base: ', pokemon['base_experience'])
        print('Link para foto: ', pokemon['sprites']['front_default'])
        print('\n')

    xp_rank(pokemons)
    for p in pokemons:
        print(list(p.keys())[0], " - ", list(p.values())[0])

