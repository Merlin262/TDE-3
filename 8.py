def numeroL(string, letra):
    contador=0
    for item in string:
        if item==letra:
            contador+=1
    return contador
print(numeroL("Vou gabaritar a prova? ", 'a'))
