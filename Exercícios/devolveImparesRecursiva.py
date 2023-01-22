def encontra_impares(lista):
    if len(lista) == 0:
      return []
    numero = lista.pop(0)
    if numero % 2 != 0:
        return [numero] + encontra_impares(lista)
    return encontra_impares(lista)
