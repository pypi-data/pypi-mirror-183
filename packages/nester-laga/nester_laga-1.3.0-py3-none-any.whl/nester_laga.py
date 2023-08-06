"""Este eh o modulo "nester.py" e prove uma funcao chamada print_lol() que
imprime listas que podem ou nao incluir listas aninhadas. """

def print_lol(lista, indent = False, nivel = 0):
    """Esta funcao toma um argumento posicional chamado "lista", que eh qualquer
       lista Python (com -possivelmente - listas aninhadas). Cada item de dado na
        lista provida eh (recursivamente) impresso na tela em sua propria linha.
       Caso haja lista aninhada e indent seja verdadeiro, uma tabulacao eh
       feita para destacah-la."""

    for cada_item in lista:
        if isinstance (cada_item, list):
            print_lol(cada_item, indent, nivel + 1)
        else:
            if indent:
                for num in range(nivel):
                    print("\t", end='')
            print(cada_item)
    


