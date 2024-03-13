def eliminar_espacios(lista):

    return [elemento.strip() for elemento in lista]


entrada_usuario = input(" ")
elementos = entrada_usuario.split()
elementos_sin_espacios = eliminar_espacios(elementos)
resultado = ''.join(elementos_sin_espacios)


print("Array sin los espacios:", resultado)
