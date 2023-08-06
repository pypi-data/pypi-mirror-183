

# Imprime todos los valores de un diccionario de forma ordenada
def imprime_diccionario(titulo, dic):
    print("\n{}".format(titulo))
    for clave, valores in dic.items():
        print(clave, ": ", valores)

